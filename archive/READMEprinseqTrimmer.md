# galaxy-tool-prinseq-trimmer
Use PRINSEQ to trim and discard reads and read sections.  
The PRINSEQ tool will trim and discard reads and read sections based on user input and quality thresholds.

Files in fastQ format should always have a .fastq extension.

Edit the following file in order to make galaxy display the tool.
```
/path/to/folder/galaxy/config/tool_conf.xml
```
```
<tool file="pathtofolder/runPrinseqTrimmer.xml"/>
```
