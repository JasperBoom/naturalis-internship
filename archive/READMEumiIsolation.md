# galaxy-tool-UMI-isolation
Use a python script to cluster all UMIs and output a tabular file, a BLAST file and a zip file.  
Use a python script to accumulate all UMIs and output a tabular file, a BLAST file and a zip file.

The tabular file will contain all unique UMI nucleotides, a count of the number of reads that are associated with that umi and a unique identifier for every UMI.

The BLAST file can be used to identify all UMI clusters.

The zip file will contain fastA files for every unique UMI and contain reads associated with that UMI, this zip file is created before VSEARCH is used for a final check.

Files in fastA format should always have a .fasta extension.  
Files in fastQ format should always have a .fastq extension.
