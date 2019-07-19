# galaxy-tool-prinseq-analysis
Use PRINSEQ to do quality control checks on raw sequence data.  
The PRINSEQ tool will do quality control checks on raw sequence data. These checks include summary graphs and tables.

Files in fastA format should always have a .fasta extension.  
Files in fastQ format should always have a .fastq extension.

## Getting started

### Prerequisites
Download and install the following software according to the following steps.
* [PRINSEQ](https://sourceforge.net/projects/prinseq/files/)

The PRINSEQ folder should be moved to the following file and renamed to "Prinseq".
```
sudo mkdir -m 755 /path/to/folder/Tools
/path/to/folder/Tools <-- Move PRINSEQ to this directory
sudo chmod -R 755 /path/to/folder/Tools/Prinseq
```
The following three files in the Prinseq folder should be made avaible from any location.
```
sudo ln -s /path/to/folder/Tools/Prinseq/prinseq-lite.pl /usr/local/bin/prinseq-lite.pl
sudo ln -s /path/to/folder/Tools/Prinseq/prinseq-graphs.pl /usr/local/bin/prinseq-graphs.pl
sudo ln -s /path/to/folder/Tools/Prinseq/prinseq-graphs-noPCA.pl /usr/local/bin/prinseq-graphs-noPCA.pl
```
Make sure your system can handle JSON files.
```
sudo cpan JSON
```

### Installing
Download and install the tool according to the following steps.
```
cd /path/to/folder/Tools
sudo git clone https://github.com/JasperBoom/galaxy-tool-prinseq-analysis
sudo chmod -R 755 galaxy-tool-prinseq-analysis
```
```
sudo mkdir -m 755 /path/to/folder/galaxy/tools/directoryname
sudo cp /path/to/folder/Tools/galaxy-tool-prinseq-analysis/getPrinseqAnalysis.sh /path/to/folder/galaxy/tools/directoryname/getPrinseqAnalysis.sh
sudo cp /path/to/folder/Tools/galaxy-tool-prinseq-analysis/getPrinseqAnalysis.xml /path/to/folder/galaxy/tools/directoryname/getPrinseqAnalysis.xml
```
Edit the following file in order to make galaxy display the tool.
```
/path/to/folder/galaxy/config/tool_conf.xml
```
```
<tool file="pathtofolder/getPrinseqAnalysis.xml"/>
```
Edit the following file in order to prevent galaxy from blocking html output.
```
/path/to/folder/galaxy/config/galaxy.yml
```
```
sanitize_all_html: false
```
