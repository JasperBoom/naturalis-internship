# galaxy-tool-metadata
Use a python script to utilize the Naturalis, BOLD and ALA api's to collect meta data.  
The MetaData tool will utilize the Naturalis, BOLD and ALA api's to collect meta data such as occurrence status and images based on BLAST identifications or accepted taxonomic names.

Definitions for all occurrence status codes can be found on this page:  
https://www.nederlandsesoorten.nl/content/occurrence-status

Sample names can not start with a "#".  
All columns in a OTU table should have a header starting with "#".

Edit the following file in order to make galaxy display the tool.
```
/path/to/folder/galaxy/config/tool_conf.xml
```
```
<tool file="pathtofolder/getMetaData.xml"/>
```
