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
