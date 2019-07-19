# galaxy-tool-accepted-taxonomic-name
Use a python script to utilize either the Global Names api or the TNRS api to collect accepted taxonomic names.  
The AcceptedTaxonomicName tool will utilize either the Global Names api or the Taxonomic Name Resolution Service api to collect accepted taxonomic names based on BLAST identifications.

Global Names is for every kingdom.  
TNRS is for plants only.

Sample names can not start with a "#".  
All columns in a OTU table should have a header starting with "#".

# Getting started

### Prerequisites
Download and install the following software according to the following steps.
```
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip3 install pandas
```

### Installing
Download and install the tool according to the following steps.
```
sudo mkdir -m 755 /path/to/folder/Tools
cd /path/to/folder/Tools
sudo git clone https://github.com/JasperBoom/galaxy-tool-accepted-taxonomic-name
sudo chmod -R 755 galaxy-tool-accepted-taxonomic-name
```
The following file in the galaxy-tool-accepted-taxonomic-name folder should be made avaible from any location.
```
sudo ln -s /path/to/folder/Tools/galaxy-tool-accepted-taxonomic-name/getScientificName.py /usr/local/bin/getScientificName.py
```
Continue with the tool installation.
```
sudo mkdir -m 755 /path/to/folder/galaxy/tools/directoryname
sudo cp /path/to/folder/Tools/galaxy-tool-accepted-taxonomic-name/getScientificName.sh /path/to/folder/galaxy/tools/directoryname/getScientificName.sh
sudo cp /path/to/folder/Tools/galaxy-tool-accepted-taxonomic-name/getScientificName.xml /path/to/folder/galaxy/tools/directoryname/getScientificName.xml
```
Edit the following file in order to make galaxy display the tool.
```
/path/to/folder/galaxy/config/tool_conf.xml
```
```
<tool file="pathtofolder/getScientificName.xml"/>
```

## Source(s)
* __Pyle RL__, Towards a Global Names Architecture: The future of indexing scientific names.  
  ZooKeys. 2016; 550: 261-281. __doi: 10.3897/zookeys.550.10009__  
  [Global Names](https://resolver.globalnames.org/api)
* __Boyle B, Hopkins N, Lu Z, Garay JAR, Mozzherin D, Rees T__,  
  The taxonomic name resolution service: an online tool for automated standardization of plant names.  
  BMC Bioinformatics. 2013; 14(16). __doi: 10.1186/1471-2105-14-16__  
  [TNRS](http://tnrs.iplantcollaborative.org/api.html)
* __Giardine B, Riemer C, Hardison RC, Burhans R, Elnitski L, Shah P__,  
  Galaxy: A platform for interactive large-scale genome analysis.  
  Genome Research. 2005; 15(10) 1451-1455 __doi: 10.1101/gr.4086505__  
  [GALAXY](https://www.galaxyproject.org/)

## Author(s)
* [Jasper Boom](https://github.com/JasperBoom)

## Citation
* __Boom J__, galaxy-tool-accepted-taxonomic-name. 2018.  
  Github repositry: https://github.com/JasperBoom/galaxy-tool-accepted-taxonomic-name
