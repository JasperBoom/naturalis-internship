# NATURALIS-INTERNSHIP INSTALL
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

Make sure both PRINSEQ and FastQC are added to the systems PATH (CutAdapt
should take care of that automatically).

```text
Copyright (C) 2025 Jasper Boom. All rights reserved.

Proprietary and confidential. Unauthorized use, copying, modification,
distribution, reverse engineering, disclosure, or creation of derivative
works is strictly prohibited without prior written permission from
Jasper Boom.
```