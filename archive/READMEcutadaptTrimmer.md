# galaxy-tool-cutadapt-trimmer
Use CutAdapt to trim and discard reads and read sections.  
The CutAdapt tool will trim and discard reads and read sections based on user input and quality thresholds.

Files in fastQ format should always have a .fastq extension.

## Getting started

### Prerequisites
Download and install the following software according to the following steps.
```
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip3 install cutadapt
```

### Installing
Download and install the tool according to the following steps.
```
sudo mkdir -m 755 /path/to/folder/Tools
cd /path/to/folder/Tools
sudo git clone https://github.com/JasperBoom/galaxy-tool-cutadapt-trimmer
sudo chmod -R 755 galaxy-tool-cutadapt-trimmer
```
```
sudo mkdir -m 755 /path/to/folder/galaxy/tools/directoryname
sudo cp /path/to/folder/Tools/galaxy-tool-cutadapt-trimmer/runCutAdapt.sh /path/to/folder/galaxy/tools/directoryname/runCutAdapt.sh
sudo cp /path/to/folder/Tools/galaxy-tool-cutadapt-trimmer/runCutAdapt.xml /path/to/folder/galaxy/tools/directoryname/runCutAdapt.xml
```
Edit the following file in order to make galaxy display the tool.
```
/path/to/folder/galaxy/config/tool_conf.xml
```
```
<tool file="pathtofolder/runCutAdapt.xml"/>
```
