# galaxy-tool-fastq-to-fasta
Use a bash script to convert fastQ files to fastA files.  
The FastqToFasta tool will convert one or multiple [zip] fastQ files to fastA files using sed.

Files in fastQ format should always have a .fastq extension.

```
Edit the following file in order to make galaxy display the tool.
```
/path/to/folder/galaxy/config/tool_conf.xml
```
```
<tool file="pathtofolder/getFastqToFasta.xml"/>
```
