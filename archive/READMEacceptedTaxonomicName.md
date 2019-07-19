# galaxy-tool-accepted-taxonomic-name
Use a python script to utilize either the Global Names api or the TNRS api to collect accepted taxonomic names.  
The AcceptedTaxonomicName tool will utilize either the Global Names api or the Taxonomic Name Resolution Service api to collect accepted taxonomic names based on BLAST identifications.

Global Names is for every kingdom.  
TNRS is for plants only.

Sample names can not start with a "#".  
All columns in a OTU table should have a header starting with "#".

Edit the following file in order to make galaxy display the tool.
```
/path/to/folder/galaxy/config/tool_conf.xml
```
```
<tool file="pathtofolder/getScientificName.xml"/>
```
