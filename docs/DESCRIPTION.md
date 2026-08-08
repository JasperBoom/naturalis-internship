# NATURALIS-INTERNSHIP DOCS


## Taxonomic accumulator
The TaxonomicAccumulator tool will count all occurrences of the identifications
for every taxonomic level, for every file used as input.

The tool will handle either a BLAST file, OTU file with old BLAST output, OTU
file with new BLAST output, a zip file containing multiple BLAST files or a
OTU file with LCA processing added to it.

Sample names can not start with a "#".  
All columns in a OTU table should have a header starting with "#".

## Accepted taxonomic name
The AcceptedTaxonomicName tool will utilize either the Global Names API or
the Taxonomic Name Resolution Service API to collect accepted taxonomic names
based on BLAST identifications.

Global Names is for every kingdom.  
TNRS is for plants only.

Sample names can not start with a "#".  
All columns in a OTU table should have a header starting with "#".

## Metadata
The MetaData tool will utilize the Naturalis, BOLD and ALA API's to collect
meta data such as occurrence status and images based on BLAST identifications
or accepted taxonomic names.

Definitions for all occurrence status codes can be found on this [page](https://www.nederlandsesoorten.nl/content/occurrence-status).

Sample names can not start with a "#".  
All columns in a OTU table should have a header starting with "#".

## Phyloseq visual reporter
The Statistical Analysis tool will utilize the Phyloseq R package to create
multiple plots based on a OTU table.

Sample names can not start with a "#".  
All columns in a OTU table should have a header starting with "#".

## FastQC analysis
The FastQC tool will do quality control checks on raw sequence data. These
checks include summary graphs and tables.

Files in fastq format should always have a .fastq extension.

## PRINSEQ analysis
The PRINSEQ tool will do quality control checks on raw sequence data. These
checks include summary graphs and tables.

Files in fasta format should always have a .fasta extension.  
Files in fastq format should always have a .fastq extension.

## PRINSEQ trimmer
The PRINSEQ tool will trim and discard reads and read sections based on user
input and quality thresholds.

Files in fastq format should always have a .fastq extension.

## CutAdapt trimmer
The CutAdapt tool will trim and discard reads and read sections based on user
input and quality thresholds.

Files in fastq format should always have a .fastq extension.

## Read counter
The ReadCount tool will count the number of reads in a file or multiple [zip]
files and output these numbers to a text file.

Files in fasta format should always have a .fasta extension.  
Files in fastq format should always have a .fastq extension.

## FastQ to fastA
The FastqToFasta tool will convert one or multiple [zip] fastq files to fasta
files using sed.

Files in fastq format should always have a .fastq extension.

```text
Copyright (C) 2025 Jasper Boom. All rights reserved.

Proprietary and confidential. Unauthorized use, copying, modification,
distribution, reverse engineering, disclosure, or creation of derivative
works is strictly prohibited without prior written permission from
Jasper Boom.
```