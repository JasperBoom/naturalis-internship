# galaxy-tool-fastq-to-fasta
Use a bash script to convert fastQ files to fastA files.  
The FastqToFasta tool will convert one or multiple [zip] fastQ files to fastA files using sed.

Files in fastQ format should always have a .fastq extension.

## Getting started

### Installing
Download and install the tool according to the following steps.
```
sudo mkdir -m 755 /path/to/folder/Tools
cd /path/to/folder/Tools
sudo git clone https://github.com/JasperBoom/galaxy-tool-fastq-to-fasta
sudo chmod -R 755 galaxy-tool-fastq-to-fasta
```
```
sudo mkdir -m 755 /path/to/folder/galaxy/tools/directoryname
sudo cp /path/to/folder/Tools/galaxy-tool-fastq-to-fasta/getFastqToFasta.sh /path/to/folder/galaxy/tools/directoryname/getFastqToFasta.sh
sudo cp /path/to/folder/Tools/galaxy-tool-fastq-to-fasta/getFastqToFasta.xml /path/to/folder/galaxy/tools/directoryname/getFastqToFasta.xml
```
Edit the following file in order to make galaxy display the tool.
```
/path/to/folder/galaxy/config/tool_conf.xml
```
```
<tool file="pathtofolder/getFastqToFasta.xml"/>
```

## Source(s)
* Stackoverflow user Owen - [Page](https://stackoverflow.com/questions/1542306/converting-fastq-to-fasta-with-sed-awk)
* __Giardine B, Riemer C, Hardison RC, Burhans R, Elnitski L, Shah P__,  
  Galaxy: A platform for interactive large-scale genome analysis.  
  Genome Research. 2005; 15(10) 1451-1455 __doi: 10.1101/gr.4086505__  
  [GALAXY](https://www.galaxyproject.org/)

## Author(s)
* [Jasper Boom](https://github.com/JasperBoom)

## Citation
* __Boom J__, galaxy-tool-fastq-to-fasta. 2018.  
  Github repositry: https://github.com/JasperBoom/galaxy-tool-fastq-to-fasta
