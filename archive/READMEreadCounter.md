# galaxy-tool-read-counter
Use a bash script to count the reads of fastQ or fastA files.  
The ReadCount tool will count the number of reads in a file or multiple [zip] files and output these numbers to a text file.

Files in fastA format should always have a .fasta extension.  
Files in fastQ format should always have a .fastq extension.

Edit the following file in order to make galaxy display the tool.
```
/path/to/folder/galaxy/config/tool_conf.xml
```
```
<tool file="pathtofolder/getReadCount.xml"/>
```
