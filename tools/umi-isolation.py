#!/usr/bin/env python3
# Copyright (C) 2025 Jasper Boom. All rights reserved.
#
# Proprietary and confidential. Unauthorized use, copying, modification,
# distribution, reverse engineering, disclosure, or creation of derivative
# works is strictly prohibited without prior written permission from
# Jasper Boom.

"""
UMI isolation utility.

This script:
1. Parses reads from fasta/fastq input.
2. Extracts UMI codes based on selected search strategy.
3. Writes one fasta file per unique UMI.
4. Runs vsearch dereplication/sort/clustering.
5. Builds tabular and blast outputs.

Note:
- ZIP creation is intentionally not handled here.
- The wrapper can zip UMI files from the -z directory.
"""

# Imports.
from __future__ import annotations

import argparse
import os
import re
import subprocess
import pandas as pd
from pathlib import Path
from typing import Dict, Iterator, Optional, Tuple, Union

UmiCode = Union[str, Tuple[str, str]]


def create_output_files(
    cluster_directory: Path,
    output_blast_file: Path,
    tabular_file: Path,
) -> None:
    """
    Create tabular and blast output files from clustered fasta files.
    """
    output = pd.DataFrame(
        columns=["UMI ID", "UMI SEQ", "READ COUNT", "CENTROID READ"]
    )
    row_count = 0

    # Truncate blast output before appending.
    output_blast_file.write_text("", encoding="utf-8")

    for cluster_file in sorted(cluster_directory.iterdir()):
        if not cluster_file.is_file():
            continue
        if cluster_file.suffix.lower() != ".fasta":
            continue

        name_without_ext = cluster_file.stem
        if "_" not in name_without_ext:
            continue

        umi_number, umi_string = name_without_ext.split("_", 1)
        records = list(iter_fasta_records(cluster_file))
        if not records:
            continue

        for version_index, (header, read) in enumerate(records, start=1):
            if len(records) == 1:
                umi_id = umi_number
            else:
                umi_id = f"{umi_number}.{version_index}"

            read_count = extract_read_count(header)
            centroid_read = read.upper()

            output.loc[row_count] = [
                umi_id,
                umi_string,
                read_count,
                centroid_read,
            ]
            row_count += 1

            with output_blast_file.open("a", encoding="utf-8") as blast_out:
                blast_out.write(f">{umi_id}\n")
                blast_out.write(f"{centroid_read}\n")

    output = output.set_index("UMI ID")
    output.to_csv(tabular_file, sep="\t", encoding="utf-8")


def extract_read_count(header: str) -> str:
    """
    Extract read count from fasta header.

    Expected pattern includes '=' in header.
    """
    if "=" in header:
        return header.split("=", 1)[1].strip()
    return ""


def iter_fasta_records(file_path: Path) -> Iterator[Tuple[str, str]]:
    """
    Yield (header, sequence) tuples from fasta files.

    This keeps the original assumption that each sequence is on one line.
    """
    with file_path.open("r", encoding="utf-8") as handle:
        while True:
            header = handle.readline()
            if not header:
                break
            sequence = handle.readline()
            if not sequence:
                break
            if not header.startswith(">"):
                continue
            yield header.strip(), sequence.strip()


def run_vsearch_cluster_size(
    work_directory: Path,
    cluster_directory: Path,
    identity_score: str,
) -> None:
    """
    Cluster sorted fasta files with vsearch --cluster_size.
    """
    for file_name in os.listdir(work_directory):
        if not file_name.startswith("sorted"):
            continue

        input_path = work_directory / file_name
        output_path = cluster_directory / file_name[11:]

        subprocess.run(
            [
                "vsearch",
                "--cluster_size",
                str(input_path),
                "--fasta_width",
                "0",
                "--id",
                identity_score,
                "--sizein",
                "--minseqlength",
                "1",
                "--centroids",
                str(output_path),
                "--sizeout",
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )


def run_vsearch_sort_by_size(
    work_directory: Path,
    minimal_size_abundance: str,
) -> None:
    """
    Sort dereplicated fasta files by abundance with vsearch.
    """
    for file_name in os.listdir(work_directory):
        if not file_name.startswith("derep"):
            continue

        input_path = work_directory / file_name
        output_path = work_directory / f"sorted{file_name}"

        subprocess.run(
            [
                "vsearch",
                "--sortbysize",
                str(input_path),
                "--output",
                str(output_path),
                "--minseqlength",
                "1",
                "--minsize",
                minimal_size_abundance,
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )


def run_vsearch_derep(work_directory: Path) -> None:
    """
    Dereplicate UMI fasta files with vsearch.
    """
    for file_name in os.listdir(work_directory):
        if not file_name.endswith(".fasta"):
            continue
        if not file_name.startswith("UMI#"):
            continue

        input_path = work_directory / file_name
        output_path = work_directory / f"derep{file_name}"

        subprocess.run(
            [
                "vsearch",
                "--derep_fulllength",
                str(input_path),
                "--output",
                str(output_path),
                "--minseqlength",
                "1",
                "--sizeout",
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )


def write_umi_fasta(
    header: str,
    read: str,
    umi_code: str,
    unique_umi_map: Dict[str, int],
    work_directory: Path,
) -> None:
    """
    Append a read to the fasta file associated with one unique UMI.
    """
    file_identifier = f"UMI#{unique_umi_map[umi_code]}_{umi_code}.fasta"
    file_path = work_directory / file_identifier

    with file_path.open("a", encoding="utf-8") as output_file:
        output_file.write(header)
        output_file.write(read)


def get_target_zero(
    read: str,
    umi_length: int,
    search_method: str,
    forward: str,
    reverse: str,
) -> Optional[UmiCode]:
    """
    Extract UMI based on zero-position logic.
    """
    check_forward_primer = re.search(forward, read)
    if check_forward_primer is None:
        return None

    check_reverse_primer = re.search(reverse, read)
    if check_reverse_primer is None:
        return None

    if search_method == "umi5":
        return read[0:umi_length]
    if search_method == "umidouble":
        return read[0:umi_length], read[-umi_length:]
    if search_method == "umi3":
        return read[-umi_length:]
    return None


def get_target_front(
    read: str,
    umi_length: int,
    search_method: str,
    forward: str,
    reverse: str,
) -> Optional[UmiCode]:
    """
    Extract UMI using scaffold(adapter)-front logic.
    """
    if search_method in {"umi5", "umidouble"}:
        forward_position = re.search(forward, read).end()
        umi_forward_position = forward_position + umi_length
        forward_umi_code = read[forward_position:umi_forward_position]

        if search_method == "umi5":
            check_reverse_primer = re.search(reverse, read)
            if check_reverse_primer is not None:
                return forward_umi_code
            return None

        reverse_position = re.search(reverse, read).start()
        umi_reverse_position = reverse_position - umi_length
        reverse_umi_code = read[umi_reverse_position:reverse_position]
        return forward_umi_code, reverse_umi_code

    if search_method == "umi3":
        check_forward_primer = re.search(forward, read)
        if check_forward_primer is None:
            return None
        reverse_position = re.search(reverse, read).start()
        umi_reverse_position = reverse_position - umi_length
        reverse_umi_code = read[umi_reverse_position:reverse_position]
        return reverse_umi_code

    return None


def get_target_behind(
    read: str,
    umi_length: int,
    search_method: str,
    forward: str,
    reverse: str,
) -> Optional[UmiCode]:
    """
    Extract UMI using primer-behind logic.
    """
    if search_method in {"umi5", "umidouble"}:
        forward_position = re.search(forward, read).start()
        umi_forward_position = forward_position - umi_length
        forward_umi_code = read[umi_forward_position:forward_position]

        if search_method == "umi5":
            check_reverse_primer = re.search(reverse, read)
            if check_reverse_primer is not None:
                return forward_umi_code
            return None

        reverse_position = re.search(reverse, read).end()
        umi_reverse_position = reverse_position + umi_length
        reverse_umi_code = read[reverse_position:umi_reverse_position]
        return forward_umi_code, reverse_umi_code

    if search_method == "umi3":
        check_forward_primer = re.search(forward, read)
        if check_forward_primer is None:
            return None
        reverse_position = re.search(reverse, read).end()
        umi_reverse_position = reverse_position + umi_length
        reverse_umi_code = read[reverse_position:umi_reverse_position]
        return reverse_umi_code

    return None


def create_reverse_complement(sequence: str) -> str:
    """
    Return reverse complement for IUPAC-supported sequence.
    """
    complement_codes = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G",
        "M": "K",
        "R": "Y",
        "W": "W",
        "S": "S",
        "Y": "R",
        "K": "M",
        "V": "B",
        "H": "D",
        "D": "H",
        "B": "V",
        "N": "N",
    }
    sequence_list = list(sequence)
    for index, base in enumerate(sequence_list):
        sequence_list[index] = complement_codes[base]
    return "".join(sequence_list)


def generate_regex(sequence: str) -> str:
    """
    Convert IUPAC ambiguity sequence into regex.
    """
    ambiguity_codes = {
        "M": "[AC]",
        "R": "[AG]",
        "W": "[AT]",
        "S": "[CG]",
        "Y": "[CT]",
        "K": "[GT]",
        "V": "[ACG]",
        "H": "[ACT]",
        "D": "[AGT]",
        "B": "[CGT]",
        "N": "[GATC]",
    }
    sequence_list = list(sequence)
    for index, base in enumerate(sequence_list):
        if base not in {"A", "T", "G", "C"}:
            sequence_list[index] = ambiguity_codes[base]
    return "".join(sequence_list)


def get_umi_code(
    read: str,
    process: str,
    umi_length: int,
    search_method: str,
    forward: str,
    reverse: str,
) -> Optional[UmiCode]:
    """
    Control UMI extraction mode and return extracted UMI code(s).
    """
    read = read.strip("\n")
    forward_regex = generate_regex(forward)
    reverse_complement_regex = generate_regex(
        create_reverse_complement(reverse[::-1])
    )

    if process == "primer":
        try:
            return get_target_behind(
                read,
                umi_length,
                search_method,
                forward_regex,
                reverse_complement_regex,
            )
        except AttributeError:
            return None

    if process == "scaffold":
        try:
            return get_target_front(
                read,
                umi_length,
                search_method,
                forward_regex,
                reverse_complement_regex,
            )
        except AttributeError:
            return None

    if process == "zero":
        try:
            return get_target_zero(
                read,
                umi_length,
                search_method,
                forward_regex,
                reverse_complement_regex,
            )
        except AttributeError:
            return None

    return None


def get_umi_collection(
    input_file: Path,
    cluster_directory: Path,
    tabular_file: Path,
    work_directory: Path,
    output_blast_file: Path,
    process: str,
    umi_length: int,
    search_method: str,
    forward: str,
    reverse: str,
    operand: str,
    identity_score: str,
    minimal_size_abundance: str,
) -> None:
    """
    Parse reads, collect UMI bins, run vsearch, create final outputs.
    """
    unique_umi_map: Dict[str, int] = {}
    count_unique_umis = 1

    with input_file.open("r", encoding="utf-8") as input_handle:
        for line in input_handle:
            if not line.startswith(operand):
                continue
            if not re.match("[A-Za-z0-9]", line[1:2]):
                continue

            header = line
            try:
                read = next(input_handle)
            except StopIteration:
                break

            umi_code = get_umi_code(
                read.upper(),
                process,
                umi_length,
                search_method,
                forward.upper(),
                reverse.upper(),
            )
            if umi_code is None:
                continue

            if search_method == "umidouble":
                umi_code = f"{umi_code[0]}{umi_code[1]}"

            if umi_code not in unique_umi_map:
                unique_umi_map[umi_code] = count_unique_umis
                count_unique_umis += 1

            write_umi_fasta(
                header,
                read,
                umi_code,
                unique_umi_map,
                work_directory,
            )

    run_vsearch_derep(work_directory)
    run_vsearch_sort_by_size(work_directory, minimal_size_abundance)
    run_vsearch_cluster_size(work_directory, cluster_directory, identity_score)
    create_output_files(cluster_directory, output_blast_file, tabular_file)


def set_format_and_run(
    input_file: Path,
    cluster_directory: Path,
    tabular_file: Path,
    work_directory: Path,
    output_blast_file: Path,
    process: str,
    format_string: str,
    umi_length: int,
    search_method: str,
    forward: str,
    reverse: str,
    identity_score: float,
    minimal_size_abundance: int,
) -> None:
    """
    Select header operand by file format and start collection workflow.
    """
    if format_string == "fasta":
        operand = ">"
    elif format_string == "fastq":
        operand = "@"
    else:
        raise ValueError("Unsupported format. Use fasta or fastq.")

    cluster_directory.mkdir(parents=True, exist_ok=True)
    work_directory.mkdir(parents=True, exist_ok=True)

    get_umi_collection(
        input_file=input_file,
        cluster_directory=cluster_directory,
        tabular_file=tabular_file,
        work_directory=work_directory,
        output_blast_file=output_blast_file,
        process=process,
        umi_length=umi_length,
        search_method=search_method,
        forward=forward,
        reverse=reverse,
        operand=operand,
        identity_score=str(identity_score),
        minimal_size_abundance=str(minimal_size_abundance),
    )


def parse_argvs() -> argparse.Namespace:
    """
    Parse command-line arguments.
    """
    description = (
        "Accumulate all UMIs and output a tabular file and blast file."
    )
    epilog = "Dependencies: pandas and vsearch."
    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-i",
        dest="input_file",
        required=True,
        help="Location of input file.",
    )
    parser.add_argument(
        "-c",
        dest="cluster_directory",
        required=True,
        help="Directory for vsearch cluster output files.",
    )
    parser.add_argument(
        "-o",
        dest="output_tabular_file",
        required=True,
        help="Location of tabular output file.",
    )
    parser.add_argument(
        "-z",
        dest="work_directory",
        required=True,
        help="Working directory for UMI and intermediate fasta files.",
    )
    parser.add_argument(
        "-q",
        dest="output_blast_file",
        required=True,
        help="Location of blast output file.",
    )
    parser.add_argument(
        "-p",
        dest="process",
        choices=["primer", "scaffold", "zero"],
        required=True,
        help="UMI search approach.",
    )
    parser.add_argument(
        "-f",
        dest="format",
        choices=["fasta", "fastq"],
        required=True,
        help="Input format.",
    )
    parser.add_argument(
        "-l",
        dest="umi_length",
        type=int,
        required=True,
        help="Length of UMI sequence.",
    )
    parser.add_argument(
        "-s",
        dest="search_method",
        choices=["umi5", "umi3", "umidouble"],
        required=True,
        help="UMI search method.",
    )
    parser.add_argument(
        "-a",
        dest="forward",
        required=True,
        help="5-prime search nucleotides.",
    )
    parser.add_argument(
        "-b",
        dest="reverse",
        required=True,
        help="3-prime search nucleotides.",
    )
    parser.add_argument(
        "-d",
        dest="identity_score",
        type=float,
        required=True,
        help="Identity score for final vsearch clustering.",
    )
    parser.add_argument(
        "-u",
        dest="abundance",
        type=int,
        required=True,
        help="Minimum read abundance for vsearch sorting.",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s [1.0]",
    )
    return parser.parse_args()


def main() -> None:
    """
    Run the UMI isolation workflow.
    """
    argvs = parse_argvs()

    set_format_and_run(
        input_file=Path(argvs.input_file),
        cluster_directory=Path(argvs.cluster_directory),
        tabular_file=Path(argvs.output_tabular_file),
        work_directory=Path(argvs.work_directory),
        output_blast_file=Path(argvs.output_blast_file),
        process=argvs.process,
        format_string=argvs.format,
        umi_length=argvs.umi_length,
        search_method=argvs.search_method,
        forward=argvs.forward,
        reverse=argvs.reverse,
        identity_score=argvs.identity_score,
        minimal_size_abundance=argvs.abundance,
    )


if __name__ == "__main__":
    main()
