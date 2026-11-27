# Naturalis Internship docs DESCRIPTION
Below is a description of all tools created during the Naturalis internship.
These tools are designed for use in Galaxy. The tools with a Python or R
script can also be used from the command line.

## Taxonomic Accumulator
The Taxonomic Accumulator tool counts occurrences of identifications at each
taxonomic level for every input file, and writes the counts to an Excel
file with one sheet per taxonomic level.

The tool can process:
- a BLAST file.
- an OTU file with old BLAST output.
- an OTU file with new BLAST output.
- a collection of BLAST files.
- an OTU file with LCA processing added.

Sample column names must not start with #. Other OTU column headers should
start with #, except for the optional `OccurrenceStatus` column.

## Scientific Name
The Scientific Name tool uses either the Global Names API or the Taxonomic
Name Resolution Service (TNRS) API to retrieve accepted taxonomic names based
on BLAST identifications.

Global Names supports all kingdoms. TNRS supports plants only.

Sample column names must not start with #. Other OTU column headers should
start with #, except for the optional `OccurrenceStatus` column.

## Metadata
The Metadata tool uses the Naturalis, BOLD, and ALA APIs to collect metadata,
such as occurrence status and images, based on BLAST identifications or
accepted taxonomic names. The occurrence status is written to a tabular file
and the images to a zip file.

Definitions for all occurrence status codes can be found on
this [page](https://www.nederlandsesoorten.nl/content/occurrence-status).

Sample column names must not start with #. Other OTU column headers should
start with #, except for the optional `OccurrenceStatus` column.

## Phyloseq Analysis
The Phyloseq Analysis tool uses the Phyloseq R package to generate abundance
bar plots, a richness plot, and heatmaps from an OTU table, as PDF files.

Sample column names must not start with #. Other OTU column headers should
start with #, except for the optional `OccurrenceStatus` column.

## FastQC
The FastQC tool performs quality control checks on raw sequence data. These
checks include summary graphs and tables.

The tool accepts a single fastq, BAM, or SAM file, or a collection of fastq
files, which it analyses as one file.

## PRINSEQ Analysis
The PRINSEQ Analysis tool performs quality control checks on raw sequence data.
These checks include summary graphs and tables.

The tool accepts a single fasta or fastq file, or a collection of files in
one of these formats, which it analyses as one file.

## PRINSEQ Trimmer
The PRINSEQ Trimmer tool trims and discards reads or read sections based on
user input and quality thresholds.

The tool accepts a fastq file.

## CutAdapt
The CutAdapt tool trims and discards reads or read sections based on user input
and quality thresholds.

The tool accepts a fastq file.

## Read Count
The Read Count tool counts the number of reads in a single fasta or fastq
file, or in every file of a collection, and writes these counts to a text
file. For a collection, it also writes the total.

Every fastq read must be on four lines.

## FASTQ To FASTA
The FASTQ to FASTA tool converts a fastq file to a fasta file using GNU Awk.
Every read must be on four lines: header, sequence, plus line, and quality.

## UMI Isolation
The UMI isolation tool reads a fastq or fasta file, extracts UMIs using the
selected search settings, groups reads by UMI, and clusters each group with
vsearch.

The Python script produces:
- A tabular file containing the UMI identifier, UMI sequence, read count, and
  centroid read for each retained cluster.
- A fasta file containing the centroid reads, ready for a separate BLAST
  search. The tool does not run BLAST itself.

The Galaxy tool also creates a zip file containing the original per-UMI read
files. It packages these files after clustering, but their contents are from
before dereplication, abundance filtering, and clustering. When running the
Python script directly, archive the per-UMI files in the directory passed to
`-z` separately if a zip file is needed.

Every read in a fasta file must have a header that starts with >, and every
read in a fastq file must have a header that starts with @. Every read must
be on a single line, so files that wrap reads every 80 characters are not
supported.

--------------------

Copyright 2025-2026 Jasper Boom. All rights reserved. See LICENSE.md.