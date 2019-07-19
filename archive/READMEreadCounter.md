# galaxy-tool-read-counter
Use a bash script to count the reads of fastQ or fastA files.  
The ReadCount tool will count the number of reads in a file or multiple [zip] files and output these numbers to a text file.

Files in fastA format should always have a .fasta extension.  
Files in fastQ format should always have a .fastq extension.

## Getting started

### Installing
Download and install the tool according to the following steps.
```
sudo mkdir -m 755 /path/to/folder/Tools
cd /path/to/folder/Tools
sudo git clone https://github.com/JasperBoom/galaxy-tool-read-counter
sudo chmod -R 755 galaxy-tool-read-counter
```
```
sudo mkdir -m 755 /path/to/folder/galaxy/tools/directoryname
sudo cp /path/to/folder/Tools/galaxy-tool-read-counter/getReadCount.sh /path/to/folder/galaxy/tools/directoryname/getReadCount.sh
sudo cp /path/to/folder/Tools/galaxy-tool-read-counter/getReadCount.xml /path/to/folder/galaxy/tools/directoryname/getReadCount.xml
```
Edit the following file in order to make galaxy display the tool.
```
/path/to/folder/galaxy/config/tool_conf.xml
```
```
<tool file="pathtofolder/getReadCount.xml"/>
```

## Source(s)
* __Giardine B, Riemer C, Hardison RC, Burhans R, Elnitski L, Shah P__,  
  Galaxy: A platform for interactive large-scale genome analysis.  
  Genome Research. 2005; 15(10) 1451-1455 __doi: 10.1101/gr.4086505__  
  [GALAXY](https://www.galaxyproject.org/)

## Author(s)
* [Jasper Boom](https://github.com/JasperBoom)

## Citation
* __Boom J__, galaxy-tool-read-counter. 2018.  
  Github repositry: https://github.com/JasperBoom/galaxy-tool-read-counter
