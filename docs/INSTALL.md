# Naturalis Internship docs INSTALL
## Galaxy With Containers
Every tool XML file names a public BioContainers image, so Galaxy only needs
to run jobs in Docker or Singularity containers. Nothing else has to be
installed on the Galaxy server. Three images still have to be built; see
[TODO.md](../TODO.md).

To add the tools to Galaxy:
1. Copy the [tools](../tools/) folder into Galaxy's tool directory, for
   example as `naturalis`.
2. Add the XML files to Galaxy's `tool_conf.xml`:
   ```xml
   <section id="naturalis" name="Naturalis">
     <tool file="naturalis/cutadapt.xml" />
     <tool file="naturalis/fastq-to-fasta.xml" />
     <tool file="naturalis/fastqc.xml" />
     <tool file="naturalis/metadata.xml" />
     <tool file="naturalis/phyloseq-analysis.xml" />
     <tool file="naturalis/prinseq-analysis.xml" />
     <tool file="naturalis/prinseq-trimmer.xml" />
     <tool file="naturalis/read-count.xml" />
     <tool file="naturalis/scientific-name.xml" />
     <tool file="naturalis/taxonomic-accumulator.xml" />
     <tool file="naturalis/umi-isolation.xml" />
   </section>
   ```
3. Enable Docker for the job destination in Galaxy's job configuration, with
   `docker_enabled` set to `true`.

The Metadata and Scientific Name tools call online APIs, so their containers
need network access. Do not set `docker_net` to `none` for these tools.

## Internship Server (2018)
This section is kept for reference only; the containers above replace it.
The server used for Galaxy during the internship was a basic machine with
Galaxy installed directly on the host machine. Conda was not yet used for
everything, so a large part of the tools relied on the host machine having the
correct software installed. The following software was installed on the host
machine to make sure the tools worked correctly.

Download and install the following software:
```bash
apt-get install python3 # Python3
apt-get install python3-pip # Python3 pip
pip3 install pandas # Python3 pandas
pip3 install xlrd # Python3 xlrd
pip3 install xlsxwriter # Python3 xlsxwriter
apt-get install python3-pip # Python3 pip
pip3 install cutadapt # CutAdapt
wget https://sourceforge.net/projects/prinseq/files/ # PRINSEQ
wget https://www.bioinformatics.babraham.ac.uk/projects/download.html#fastqc # FastQC
apt-get install r-base # R
apt-get install libcurl4-gnutls-dev # R required libraries
apt-get install libssl-dev # R required libraries
R -e 'biocLite("phyloseq")' # R packages
R -e 'biocLite("optparse")' # R packages
apt-get install default-jre # Java
cpan JSON # JSON
```

Make sure both PRINSEQ and FastQC are added to the system's PATH (CutAdapt
should take care of that automatically).

--------------------

Copyright 2025-2026 Jasper Boom. All rights reserved. See LICENSE.md.