# galaxy-tool-taxonomic-accumulator
Use a python script to accumulate all identifications based on taxonomy.  
The TaxonomicAccumulator tool will count all occurrences of the identifications for every taxonomic level, for every file used as input.

The tool will handle either a BLAST file, OTU file with old BLAST output, OTU file with new BLAST output, a zip file containing multiple BLAST files or a OTU file with LCA processing added to it.

Sample names can not start with a "#".  
All columns in a OTU table should have a header starting with "#".

# Getting started

### Prerequisites
Download and install the following software according to the following steps.
```
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip3 install pandas
sudo pip3 install xlsxwriter
sudo pip3 install xlrd
```

### Installing
Download and install the tool according to the following steps.
```
sudo mkdir -m 755 /path/to/folder/Tools
cd /path/to/folder/Tools
sudo git clone https://github.com/JasperBoom/galaxy-tool-taxonomic-accumulator
sudo chmod -R 755 galaxy-tool-taxonomic-accumulator
```
The following file in the galaxy-tool-taxonomic-accumulator folder should be made avaible from any location.
```
sudo ln -s /path/to/folder/Tools/galaxy-tool-taxonomic-accumulator/runTaxonomicAccumulator.py /usr/local/bin/runTaxonomicAccumulator.py
```
Continue with the tool installation.
```
sudo mkdir -m 755 /path/to/folder/galaxy/tools/directoryname
sudo cp /path/to/folder/Tools/galaxy-tool-taxonomic-accumulator/runTaxonomicAccumulator.sh /path/to/folder/galaxy/tools/directoryname/runTaxonomicAccumulator.sh
sudo cp /path/to/folder/Tools/galaxy-tool-taxonomic-accumulator/runTaxonomicAccumulator.xml /path/to/folder/galaxy/tools/directoryname/runTaxonomicAccumulator.xml
```
Edit the following file in order to make galaxy display the tool.
```
/path/to/folder/galaxy/config/tool_conf.xml
```
```
<tool file="pathtofolder/runTaxonomicAccumulator.xml"/>
```
## Source(s)
* __Giardine B, Riemer C, Hardison RC, Burhans R, Elnitski L, Shah P__,  
  Galaxy: A platform for interactive large-scale genome analysis.  
  Genome Research. 2005; 15(10) 1451-1455 __doi: 10.1101/gr.4086505__  
  [GALAXY](https://www.galaxyproject.org/)

## Author(s)
* [Jasper Boom](https://github.com/JasperBoom)

## Citation
* __Boom J__, galaxy-tool-taxonomic-accumulator. 2018.  
  Github repositry: https://github.com/JasperBoom/galaxy-tool-taxonomic-accumulator
