# galaxy-tool-metadata
Use a python script to utilize the Naturalis, BOLD and ALA api's to collect meta data.  
The MetaData tool will utilize the Naturalis, BOLD and ALA api's to collect meta data such as occurrence status and images based on BLAST identifications or accepted taxonomic names.

Definitions for all occurrence status codes can be found on this page:  
https://www.nederlandsesoorten.nl/content/occurrence-status

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
sudo git clone https://github.com/JasperBoom/galaxy-tool-metadata
sudo chmod -R 755 galaxy-tool-metadata
```
The following file in the galaxy-tool-metadata folder should be made avaible from any location.
```
sudo ln -s /path/to/folder/Tools/galaxy-tool-metadata/getMetaData.py /usr/local/bin/getMetaData.py
```
Continue with the tool installation.
```
sudo mkdir -m 755 /path/to/folder/galaxy/tools/directoryname
sudo cp /path/to/folder/Tools/galaxy-tool-metadata/getMetaData.sh /path/to/folder/galaxy/tools/directoryname/getMetaData.sh
sudo cp /path/to/folder/Tools/galaxy-tool-metadata/getMetaData.xml /path/to/folder/galaxy/tools/directoryname/getMetaData.xml
```
Edit the following file in order to make galaxy display the tool.
```
/path/to/folder/galaxy/config/tool_conf.xml
```
```
<tool file="pathtofolder/getMetaData.xml"/>
```
