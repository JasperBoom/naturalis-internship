# Naturalis Internship tools
This folder contains the Galaxy tools created during the 2018 Naturalis
internship. Every tool has a Galaxy tool XML file, which defines the inputs,
outputs, command, and help text that Galaxy shows. Tools that need custom
logic also have a Python or R script with the same name. The other tools call
existing software directly from the XML file, which replaced the Bash
wrappers used during the internship.

Every XML file names a public BioContainers image, so Galaxy runs each tool
in a container and nothing has to be installed on the Galaxy server. The XML
files follow the structure and style of the tools in infra-docker-galaxy.
Three images still have to be built; see [TODO.md](../TODO.md).

Tool                  | XML file                                               | Script                                               | Software
--------------------- | ------------------------------------------------------ | ---------------------------------------------------- | --------------------------
CutAdapt              | [cutadapt.xml](cutadapt.xml)                           |                                                      | CutAdapt
FASTQ to FASTA        | [fastq-to-fasta.xml](fastq-to-fasta.xml)               |                                                      | GNU Awk
FastQC                | [fastqc.xml](fastqc.xml)                               |                                                      | FastQC
Metadata              | [metadata.xml](metadata.xml)                           | [metadata.py](metadata.py)                           | Python, pandas, curl
Phyloseq Analysis     | [phyloseq-analysis.xml](phyloseq-analysis.xml)         | [phyloseq-analysis.r](phyloseq-analysis.r)           | R, Phyloseq
PRINSEQ Analysis      | [prinseq-analysis.xml](prinseq-analysis.xml)           |                                                      | PRINSEQ
PRINSEQ Trimmer       | [prinseq-trimmer.xml](prinseq-trimmer.xml)             |                                                      | PRINSEQ
Read Count            | [read-count.xml](read-count.xml)                       |                                                      | GNU Awk
Scientific Name       | [scientific-name.xml](scientific-name.xml)             | [scientific-name.py](scientific-name.py)             | Python, pandas
Taxonomic Accumulator | [taxonomic-accumulator.xml](taxonomic-accumulator.xml) | [taxonomic-accumulator.py](taxonomic-accumulator.py) | Python, pandas, XlsxWriter
UMI isolation         | [umi-isolation.xml](umi-isolation.xml)                 | [umi-isolation.py](umi-isolation.py)                 | Python, VSEARCH

Galaxy collections replace the zip files that the internship tools used.
FastQC, PRINSEQ Analysis, Read Count, and Taxonomic Accumulator accept a
list collection and combine its files into one result. Galaxy runs the other
tools once for every file in a collection.

This codebase reflects 2018 internship work and should be interpreted as
student-quality, strongly learning-oriented implementation. The main objective
during development was to gain practical experience with scripting and Galaxy
tool integration workflows rather than to deliver production-level software
architecture.

Special note on UMI isolation: the UMI isolation tool was developed further
outside this repository after the internship period. Development later stopped,
and the tool was brought back into this repository so all related internship
tooling remains available in one place for reference and continuity.

--------------------

Copyright 2025-2026 Jasper Boom. All rights reserved. See LICENSE.md.