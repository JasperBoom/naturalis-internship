#!/usr/bin/env bash
# Copyright ©2007 Free Software Foundation, Inc.

# Author: Jasper Boom

# The getZipOutput function.
# This function loops through all fastQ files extracted from the input file.
# It isolates the unqiue name of every fastQ file into strFastqFileName.
# Every fastQ file is converted into a fastA file using sed. The unique name
# is used to add the new fastA file to a new zip file. If this zip file already
# exists, the fastA file is added to it, if it does not yet exist, the function
# creates a new zip file and then adds the fastA file.
getZipOutput() {
    for strFile in ${strDirectory}_temp/*.fastq;
    do
        strUniqueFileName=$(printf "%s\n" "${strFile##*/}")
        strFastqFileName=${strUniqueFileName::-6}
        cat ${strFile} | sed -n "1~4s/^@/>/p;2~4p" \
            > ${strDirectory}_temp/${strFastqFileName}.fasta
        if [ -e flZip.zip ]
        then
            zip -jqru ${strDirectory}_temp/flZip.zip \
                ${strDirectory}_temp/${strFastqFileName}.fasta
        else
            zip -jqr ${strDirectory}_temp/flZip.zip \
                ${strDirectory}_temp/${strFastqFileName}.fasta
        fi
    done
}

# The getZipFile function.
# This function creates a temporary storage directory in the output directory.
# The input file is copied to the temporary storage directory. The input file
# is searched for, based on its .dat extension. This search will output the
# name of the input file which is used to unzip it into the temporary storage
# directory. After unzipping, the getZipOutput function is called.
getZipFile() {
    strDirectory=${fosOutput::-4}
    mkdir -p "${strDirectory}_temp"
    cp ${fisInput} ${strDirectory}_temp
    strZipName=$(find ${strDirectory}_temp -name "*.dat" -printf "%f\n")
    unzip -q ${strDirectory}_temp/${strZipName} -d ${strDirectory}_temp
    getZipOutput
}

# The getFormatFlow function.
# This function initiates the correct function chain depending on the file
# format. When transforming a single fastQ file to fastA, the conversion is
# done instantly using sed. When transforming a zip file, the function
# getZipFile is called. After conversions are done, output is send to the 
# expected location and the temporary storage directory is deleted.
getFormatFlow() {
    if [ "${disFormat}" = "fastq" ]
    then
        cat ${fisInput} | sed -n "1~4s/^@/>/p;2~4p" > ${fosOutput}
    elif [ "${disFormat}" = "zip" ]
    then
        getZipFile
        cat ${strDirectory}_temp/flZip.zip > ${fosOutput}
        rm -rf ${strDirectory}_temp
    fi
}

# The main function.
main() {
    getFormatFlow
}

# The getopts function.
while getopts ":i:o:f:vh" opt; do
    case ${opt} in
        i)
            fisInput=${OPTARG}
            ;;
        o)
            fosOutput=${OPTARG}
            ;;
        f)
            disFormat=${OPTARG}
            ;;
        v)
            echo ""
            echo "getFastqToFasta.sh [0.1.0]"
            echo ""

            exit
            ;;
        h)
            echo ""
            echo "Usage: getFastqToFasta.sh [-h] [-v] [-i INPUT] [-o OUTPUT]"
            echo "                          [-f FORMAT]"
            echo ""
            echo "Optional arguments:"
            echo " -h                    Show this help page and exit"
            echo " -v                    Show the software's version number"
            echo "                       and exit"
            echo " -i                    The location of the input file(s)"
            echo " -o                    The location of the output file(s)"
            echo " -f                    The format of the input" 
            echo "                       file(s) [fastq/zip]"
            echo ""
            echo "The FastqToFasta tool will convert one or multiple [zip]"
            echo "fastQ files to fastA files using sed."
            echo ""
            echo "Files in fastQ format should always have a .fastq extension."
            echo ""
            echo "Source(s):"
            echo " - Stackoverflow user Owen."
            echo "   https://stackoverflow.com/questions/1542306/converting-fastq-to-fasta-with-sed-awk"
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

# Additional information:
# =======================
#
# Files in fastQ format should always have a .fastq extension.
