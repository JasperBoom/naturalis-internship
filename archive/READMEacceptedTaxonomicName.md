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
