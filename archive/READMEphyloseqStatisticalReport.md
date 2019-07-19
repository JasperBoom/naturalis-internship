# galaxy-tool-phyloseq-statistical-report
Use Phyloseq to a statistical analysis resulting in multiple plots.  
The Statistical Analysis tool will utilize the Phyloseq R package to create multiple plots based on a OTU table.

Sample names can not start with a "#".  
All columns in a OTU table should have a header starting with "#".

Edit the following file in order to make galaxy display the tool.
```
/path/to/folder/galaxy/config/tool_conf.xml
```
```
<tool file="pathtofolder/getInformation.xml"/>
```
