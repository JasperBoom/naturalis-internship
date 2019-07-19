# galaxy-tool-fastqc-analysis
Use FastQC to do quality control checks on raw sequence data.  
The FastQC tool will do quality control checks on raw sequence data. These checks include summary graphs and tables.

Files in fastQ format should always have a .fastq extension.

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
