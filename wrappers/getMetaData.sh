#!/usr/bin/env bash
# Copyright 2025-2026 Jasper Boom. All rights reserved. See LICENSE.md.

# Prerequisites:
# - Conda environment with Python >= 3.7
# - conda install -c anaconda pandas

# The getFormatFlow function.
# This function creates a temporary storage directory in the output directory.
# It then calls the getMetaData.py script with the correct input values.
# After the script is finished, output is sent to the expected location and
# the temporary storage directory is deleted.
getFormatFlow() {
    strDirectory=${fosOutput::-4}
    mkdir -p "${strDirectory}_temp"
    if [ "${disProcess}" = "occurrences" ]
    then
        getMetaData.py -i ${fisInput} -o ${strDirectory}_temp/ \
                       -p ${disProcess} -f ${disFormat}
        cat ${strDirectory}_temp/flNewOutput.tabular > ${fosOutput}
        rm -rf ${strDirectory}_temp
    elif [ "${disProcess}" = "pictures" ]
    then
        getMetaData.py -i ${fisInput} -o ${strDirectory}_temp/ \
                       -p ${disProcess} -f ${disFormat}
        zip -jqr ${strDirectory}_temp/flImageZip.zip ${strDirectory}_temp/*
        cat ${strDirectory}_temp/flImageZip.zip > ${fosOutput}
        rm -rf ${strDirectory}_temp
    fi
}

# The main function.
main() {
    getFormatFlow
}

# The getopts function.
while getopts ":i:o:p:f:vh" opt; do
    case ${opt} in
        i)
            fisInput=${OPTARG}
            ;;
        o)
            fosOutput=${OPTARG}
            ;;
        p)
            disProcess=${OPTARG}
            ;;
        f)
            disFormat=${OPTARG}
            ;;
        v)
            echo ""
            echo "getMetaData.sh [0.1.0]"
            echo ""

            exit
            ;;
        h)
            echo ""
            echo "Usage: getMetaData.sh [-h] [-v] [-i INPUT] [-o OUTPUT]"
            echo "                      [-p PROCESS] [-f FORMAT]"
            echo ""
            echo "Optional arguments:"
            echo " -h                    Show this help page and exit"
            echo " -v                    Show the software's version number"
            echo "                       and exit"
            echo " -i                    The location of the input file(s)"
            echo " -o                    The location of the output file(s)"
            echo " -p                    The metadata process"
            echo "                       type [occurrences/pictures]"
            echo " -f                    The format of the input"
            echo "                       file(s) [otu_old/otu_new/lca/"
            echo "                       accepted/blast]"
            echo ""
            echo "The MetaData tool will utilise the Naturalis, BOLD and ALA"
            echo "APIs to collect metadata such as occurrence status and"
            echo "images based on BLAST identifications or accepted taxonomic"
            echo "names."
            echo ""
            echo "Definitions for all occurrence status codes can be found"
            echo "on this page:"
            echo "https://www.nederlandsesoorten.nl/content/occurrence-status"
            echo ""
            echo "Sample names cannot start with a '#'."
            echo "All columns in an OTU table should have a header starting"
            echo "with '#'."
            echo ""
            echo "Source(s):"
            echo " - Naturalis website at"
            echo "   http://docs.biodiversitydata.nl/en/latest/introduction/"
            echo " - Nederlands Soortenregister website at"
            echo "   https://www.nederlandsesoorten.nl/"
            echo " - Ratnasingham S, Hebert PDN, BOLD: The Barcode of Life"
            echo "   Data System."
            echo "   Molecular Ecology Notes. 2007; 7(3)."
            echo "   doi: 10.1111/j.1471-8286.2007.01678.x"
            echo "   http://www.boldsystems.org/index.php/resources/api"
            echo " - Atlas of Living Australia website at"
            echo "   https://api.ala.org.au/"
            echo ""

            exit
            ;;
        \?)
            echo ""
            echo "You've entered an invalid option: -${OPTARG}."
            echo "Please use the -h option for correct formatting information."
            echo ""

            exit
            ;;
        :)
            echo ""
            echo "You've entered an invalid option: -${OPTARG}."
            echo "Please use the -h option for correct formatting information."
            echo ""

            exit
            ;;
    esac
done

main