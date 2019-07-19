# galaxy-tool-phyloseq-statistical-report
Use Phyloseq to a statistical analysis resulting in multiple plots.  
The Statistical Analysis tool will utilize the Phyloseq R package to create multiple plots based on a OTU table.

Sample names can not start with a "#".  
All columns in a OTU table should have a header starting with "#".

# Getting started

### Prerequisites
Download and install the following software according to the following steps.
```
sudo apt-get install r-base
sudo apt-get install libcurl4-gnutls-dev
sudo apt-get install libssl-dev
```
These packages should be installed in R.
```
source("http://bioconductor.org/biocLite.R")
biocLite("phyloseq")
biocLite("optparse")
```

### Installing
Download and install the tool according to the following steps.
```
sudo mkdir -m 755 /path/to/folder/Tools
cd /path/to/folder/Tools
sudo git clone https://github.com/JasperBoom/galaxy-tool-phyloseq-statistical-report
sudo chmod -R 755 galaxy-tool-phyloseq-statistical-report
```
The following file in the galaxy-tool-phyloseq-statistical-report folder should be made avaible from any location.
```
sudo ln -s /path/to/folder/Tools/galaxy-tool-phyloseq-statistical-report/getInformation.R /usr/local/bin/getInformation.R
```
Continue with the tool installation.
```
sudo mkdir -m 755 /path/to/folder/galaxy/tools/directoryname
sudo cp /path/to/folder/Tools/galaxy-tool-phyloseq-statistical-report/getInformation.sh /path/to/folder/galaxy/tools/directoryname/getInformation.sh
sudo cp /path/to/folder/Tools/galaxy-tool-phyloseq-statistical-report/getInformation.xml /path/to/folder/galaxy/tools/directoryname/getInformation.xml
```
Edit the following file in order to make galaxy display the tool.
```
/path/to/folder/galaxy/config/tool_conf.xml
```
```
<tool file="pathtofolder/getInformation.xml"/>
```
