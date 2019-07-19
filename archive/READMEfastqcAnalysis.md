# galaxy-tool-fastqc-analysis
Use FastQC to do quality control checks on raw sequence data.  
The FastQC tool will do quality control checks on raw sequence data. These checks include summary graphs and tables.

Files in fastQ format should always have a .fastq extension.

## Getting started

### Prerequisites
Download and install the following software according to the following steps.
* [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/download.html#fastqc)

The FastQC folder should be moved to the following file and renamed to "Fastqc".
```
sudo mkdir -m 755 /path/to/folder/Tools
/path/to/folder/Tools <-- Move FastQC to this directory
sudo chmod -R 755 /path/to/folder/Tools/Fastqc
```
The following file in the FastQC folder should be made avaible from any location.
```
sudo ln -s /path/to/folder/Tools/Fastqc/fastqc /usr/local/bin/fastqc
```
Make sure java is installed on your system.
```
sudo apt-get install default-jre
```

### Installing
Download and install the tool according to the following steps.
```
cd /path/to/folder/Tools
sudo git clone https://github.com/JasperBoom/galaxy-tool-fastqc-analysis
sudo chmod -R 755 galaxy-tool-fastqc-analysis
```
```
sudo mkdir -m 755 /path/to/folder/galaxy/tools/directoryname
sudo cp /path/to/folder/Tools/galaxy-tool-fastqc-analysis/runFastQC.sh /path/to/folder/galaxy/tools/directoryname/runFastQC.sh
sudo cp /path/to/folder/Tools/galaxy-tool-fastqc-analysis/runFastQC.xml /path/to/folder/galaxy/tools/directoryname/runFastQC.xml
```
Edit the following file in order to make galaxy display the tool.
```
/path/to/folder/galaxy/config/tool_conf.xml
```
```
<tool file="pathtofolder/runFastQC.xml"/>
```
Edit the following file in order to prevent galaxy from blocking html output.
```
/path/to/folder/galaxy/config/galaxy.yml
```
```
sanitize_all_html: false
```

## Source(s)
* __Andrews S__, FastQC: A quality control tool for high throughput sequence data.  
  Babraham Bioinformatics. 2010.  
  [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)
* __Giardine B, Riemer C, Hardison RC, Burhans R, Elnitski L, Shah P__,  
  Galaxy: A platform for interactive large-scale genome analysis.  
  Genome Research. 2005; 15(10) 1451-1455 __doi: 10.1101/gr.4086505__  
  [GALAXY](https://www.galaxyproject.org/)
  
## Author(s)
* [Jasper Boom](https://github.com/JasperBoom)

## Citation
* __Boom J__, galaxy-tool-fastqc-analysis. 2018.  
  Github repositry: https://github.com/JasperBoom/galaxy-tool-fastqc-analysis
