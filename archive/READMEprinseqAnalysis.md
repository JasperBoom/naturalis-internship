# galaxy-tool-prinseq-analysis
Use PRINSEQ to do quality control checks on raw sequence data.  
The PRINSEQ tool will do quality control checks on raw sequence data. These checks include summary graphs and tables.

Files in fastA format should always have a .fasta extension.  
Files in fastQ format should always have a .fastq extension.

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
