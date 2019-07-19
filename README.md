# galaxy-tools-naturalis-internship
These tools were made for the Naturalis Galaxy instance with a main focus on metabarcoding analysis.

## Tool descriptions

### Accepted Taxonomic Name

## Getting started

### Prerequisites
Download and install the following software:
```
Python3 (apt-get install python3)
Python3 pip (apt-get install python3-pip)
Python3 pandas (pip3 install pandas)
Python3 xlrd (pip3 install xlrd)
Python3 xlsxwriter (pip3 install xlsxwriter)
CutAdapt (pip3 install cutadapt)
PRINSEQ (https://sourceforge.net/projects/prinseq/files/)
FastQC (https://www.bioinformatics.babraham.ac.uk/projects/download.html#fastqc)
R (apt-get install r-base)
R required libraries (apt-get install libcurl4-gnutls-dev & apt-get install libssl-dev)
R packages (biocLite("phyloseq") & biocLite("optparse"))
Java (apt-get install default-jre)
JSON (cpan JSON)
VSEARCH required libraries (apt-get install libargtable2-dev)
VSEARCH (https://github.com/torognes/vsearch)
```
Make sure both PRINSEQ and FastQC are added to the systems PATH. (CutAdapt should take care of that automatically)

### Galaxy configuration
The galaxyXML files and the bashWrapper files should either be copied to the Galaxy tool shed folder or be symbolically linked there.  
The tool files should be reachable by the bashWrappers, either by being present in the same folder or by adding the tool files to the systems PATH.  
Edit the Galaxy tool_conf.xml file to add the tools to the Galaxy tool shed.

## Source(s)
* __Giardine B, Riemer C, Hardison RC, Burhans R, Elnitski L, Shah P__,  
  Galaxy: A platform for interactive large-scale genome analysis.  
  Genome Research. 2005; 15(10) 1451-1455 __doi: 10.1101/gr.4086505__  
  [GALAXY](https://www.galaxyproject.org/)
* __Andrews S__, FastQC: A quality control tool for high throughput sequence data.  
  Babraham Bioinformatics. 2010.  
  [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)
* __Schmieder R, Edwards R__, Quality control and preprocessing of metagenomic datasets.  
  Bioinformatics. 2011; 27(6): 863-864. __doi: 10.1093/bioinformatics/btr026__  
  [PRINSEQ](http://prinseq.sourceforge.net/)
* __Martin M__, Cutadapt Removes Adapter Sequences From High-throughput Sequencing Reads.  
  EMBnet.journal. 2011. __doi: 10.14806/ej.17.1.200__  
  [CutAdapt](http://cutadapt.readthedocs.io/en/stable/guide.html)
* __McMurdie PJ, Holmes S__, Phyloseq: An R Package for Reproducible Interactive Analysis and Graphics of Microbiome Census Data.  
  PLOS One. 2013; 8(4). __doi: 10.1371/journal.pone.0061217__  
  [Phyloseq](https://joey711.github.io/phyloseq/)
* __Rognes T, Flouri T, Nichols B, Quince C, Mahe F__, VSEARCH: a versatile open source tool for metagenomics.  
  Peerj. 2016. __doi: 10.7717/peerj.2584__  
  [VSEARCH](https://github.com/torognes/vsearch)
* __Ratnasingham S, Hebert PDN__, BOLD: The Barcode of Life Data System.  
  Molecular Ecology Notes. 2007; 7(3). __doi: 10.1111/j.1471-8286.2007.01678.x__  
  [BOLD](http://www.boldsystems.org/index.php/resources/api)
* __Pyle RL__, Towards a Global Names Architecture: The future of indexing scientific names.  
  ZooKeys. 2016; 550: 261-281. __doi: 10.3897/zookeys.550.10009__  
  [Global Names](https://resolver.globalnames.org/api)
* __Boyle B, Hopkins N, Lu Z, Garay JAR, Mozzherin D, Rees T__,  
  The taxonomic name resolution service: an online tool for automated standardization of plant names.  
  BMC Bioinformatics. 2013; 14(16). __doi: 10.1186/1471-2105-14-16__  
  [TNRS](http://tnrs.iplantcollaborative.org/api.html)
* Naturalis API website at http://docs.biodiversitydata.nl/en/latest/introduction/
* Nederlands Soortenregister website at https://www.nederlandsesoorten.nl/
* Atlas of Living Australia API website at https://api.ala.org.au/

## Author(s)
* [Jasper Boom](https://github.com/JasperBoom)

## Citation
* __Boom J__, galaxy-tools-naturalis-internship. 2019.  
  Github repository: https://github.com/JasperBoom/galaxy-tools-naturalis-internship
