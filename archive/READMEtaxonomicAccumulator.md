# galaxy-tool-taxonomic-accumulator
Use a python script to accumulate all identifications based on taxonomy.  
The TaxonomicAccumulator tool will count all occurrences of the identifications for every taxonomic level, for every file used as input.

The tool will handle either a BLAST file, OTU file with old BLAST output, OTU file with new BLAST output, a zip file containing multiple BLAST files or a OTU file with LCA processing added to it.

Sample names can not start with a "#".  
All columns in a OTU table should have a header starting with "#".

Edit the following file in order to make galaxy display the tool.
```
/path/to/folder/galaxy/config/tool_conf.xml
```
```
<tool file="pathtofolder/runTaxonomicAccumulator.xml"/>
```
