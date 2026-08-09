# NATURALIS-INTERNSHIP DOCS
Below is a description of all tools created during the Naturalis internship.
These tools are designed for use in Galaxy, but can also be used from the
command line.

## Taxonomic accumulator
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

## Accepted taxonomic name
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

## Phyloseq visual reporter
The StatisticalAnalysis tool uses the Phyloseq R package to generate multiple
plots from an OTU table.

Sample names cannot start with #. All columns in an OTU table must have a
header that starts with #.

## FastQC analysis
The FastQC tool performs quality control checks on raw sequence data. These
checks include summary graphs and tables.

Fastq files must use the .fastq extension.

## PRINSEQ analysis
The PRINSEQ analysis tool performs quality control checks on raw sequence data.
These checks include summary graphs and tables.

Fasta files must use the .fasta extension. Fastq files must use the .fastq
extension.

## PRINSEQ trimmer
The PRINSEQ trimmer tool trims and discards reads or read sections based on
user input and quality thresholds.

Fastq files must use the .fastq extension.

## CutAdapt trimmer
The CutAdapt tool trims and discards reads or read sections based on user input
and quality thresholds.

Fastq files must use the .fastq extension.

## Read counter
The ReadCount tool counts the number of reads in one file or multiple zip
files and writes these counts to a text file.

Fasta files must use the .fasta extension. Fastq files must use the .fastq
extension.

## Fastq to fasta
The FastqToFasta tool converts one or multiple zip fastq files to fasta files
using sed.

Fastq files must use the .fastq extension.

```text
Copyright (C) 2025 Jasper Boom. All rights reserved.

Proprietary and confidential. Unauthorized use, copying, modification,
distribution, reverse engineering, disclosure, or creation of derivative
works is strictly prohibited without prior written permission from
Jasper Boom.
```