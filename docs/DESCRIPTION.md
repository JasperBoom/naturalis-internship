# Naturalis Internship docs DESCRIPTION
Below is a description of all tools created during the Naturalis internship.
These tools are designed for use in Galaxy, but can also be used from the
command line.

## Taxonomic Accumulator
The TaxonomicAccumulator tool counts occurrences of identifications at each
taxonomic level for every input file.

The tool can process:
- a BLAST file.
- an OTU file with old BLAST output.
- an OTU file with new BLAST output.
- a zip file containing multiple BLAST files.
- an OTU file with LCA processing added.

Sample names cannot start with #. All columns in an OTU table must have a
header that starts with #.

## Accepted Taxonomic Name
The AcceptedTaxonomicName tool uses either the Global Names API or the
Taxonomic Name Resolution Service API to retrieve accepted taxonomic names
based on BLAST identifications.

Global Names supports all kingdoms. TNRS supports plants only.

Sample names cannot start with #. All columns in an OTU table must have a
header that starts with #.

## Metadata
The Metadata tool uses the Naturalis, BOLD, and ALA APIs to collect metadata,
such as occurrence status and images, based on BLAST identifications or
accepted taxonomic names.

Definitions for all occurrence status codes can be found on
this [page](https://www.nederlandsesoorten.nl/content/occurrence-status).

Sample names cannot start with #. All columns in an OTU table must have a
header that starts with #.

## Phyloseq Visual Reporter
The StatisticalAnalysis tool uses the Phyloseq R package to generate multiple
plots from an OTU table.

Sample names cannot start with #. All columns in an OTU table must have a
header that starts with #.

## FastQC Analysis
The FastQC tool performs quality control checks on raw sequence data. These
checks include summary graphs and tables.

Fastq files must use the .fastq extension.

## PRINSEQ Analysis
The PRINSEQ analysis tool performs quality control checks on raw sequence data.
These checks include summary graphs and tables.

Fasta files must use the .fasta extension. Fastq files must use the .fastq
extension.

## PRINSEQ Trimmer
The PRINSEQ trimmer tool trims and discards reads or read sections based on
user input and quality thresholds.

Fastq files must use the .fastq extension.

## CutAdapt Trimmer
The CutAdapt tool trims and discards reads or read sections based on user input
and quality thresholds.

Fastq files must use the .fastq extension.

## Read Counter
The ReadCount tool counts the number of reads in a single file, or in
multiple files inside a zip file, and writes these counts to a text file.

Fasta files must use the .fasta extension. Fastq files must use the .fastq
extension.

## Fastq To Fasta
The FastqToFasta tool converts a single fastq file, or multiple fastq files
inside a zip file, to fasta files using sed.

Fastq files must use the .fastq extension.

## UMI Isolation
The UMI isolation tool reads a fastq or fasta file, extracts UMIs using the
selected search settings, groups reads by UMI, and clusters each group with
vsearch.

The Python script produces:
- A tabular file containing the UMI identifier, UMI sequence, read count, and
  centroid read for each retained cluster.
- A fasta file containing the centroid reads, ready for a separate BLAST
  search. The tool does not run BLAST itself.

The Galaxy XML wrapper also creates a zip file containing the original
per-UMI read files. It packages these files after clustering, but their
contents are from before dereplication, abundance filtering, and clustering.
When running the Python script directly, archive the per-UMI files in the
directory passed to `-z` separately if a zip file is needed.

Every read in a fasta file must have a header that starts with >, and every
read in a fastq file must have a header that starts with @. Every read must
be on a single line, so files that wrap reads every 80 characters are not
supported.

--------------------

Copyright 2025-2026 Jasper Boom. All rights reserved. See LICENSE.md.