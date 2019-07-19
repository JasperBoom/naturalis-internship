#!/usr/bin/env bash
# Copyright ©2007 Free Software Foundation, Inc.

# Author: Jasper Boom

# The getZipOutput function.
# This function loops through all files extracted from the input file. It
# isolates the unique name of every file into strFileName. All lines are
# counted per file and divided by intDivide. This calculation is then added to
# the output file. A total of all reads is also calculated and added.
getZipOutput() {
    echo "The getReadCount.sh script is done counting the reads!"\
         >> ${fosOutput}
    echo " " >> ${fosOutput}
    for strFile in ${strDirectory}_temp/*${strExtension};
    do
        strFileName="$(basename ${strFile})"
        intFileLines="$(cat ${strFile} | wc -l)"
        intReadCount="$(awk "BEGIN {print ${intFileLines}/${intDivide}}")"
        intTotalCount=$(($intTotalCount + ${intReadCount}))
        echo "${strFileName}: ${intReadCount} reads" >> ${fosOutput}
    done
    echo "Total: ${intTotalCount} reads" >> ${fosOutput}
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
# format. And sets the integer used for calculating the read count. This integer
# depends on what extension the input file(s) are. When working with a single
# file, the calculations are done immediately. When working with a zip file,
# the function getZipFile is called. After calculations are done the temporary 
# storage directory is deleted.
getFormatFlow() {
    if [ "${disType}" = "fasta" ]
    then
        intDivide=2
        strExtension=".fasta"
    elif [ "${disType}" = "fastq" ]
    then
        intDivide=4
        strExtension=".fastq"
    fi
    if [ "${disFormat}" = "single" ]
    then
        strFileName="$(basename ${fisInput})"
        intFileLines="$(cat ${fisInput} | wc -l)"
        intReadCount="$(awk "BEGIN {print ${intFileLines}/${intDivide}}")"
        echo "The getReadCount.sh script is done counting the reads!"\
             >> ${fosOutput}
        echo " " >> ${fosOutput}
        echo "${strFileName}: ${intReadCount} reads" >> ${fosOutput}
    elif [ "${disFormat}" = "zip" ]
    then
        getZipFile
        rm -rf ${strDirectory}_temp
    fi
}

# The main function.
main() {
    getFormatFlow
}

# The getopts function.
while getopts ":i:o:f:e:vh" opt; do
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
        e)
            disType=${OPTARG}
            ;;
        v)
            echo ""
            echo "getReadCount.sh [0.1.0]"
            echo ""

            exit
            ;;
        h)
            echo ""
            echo "Usage: getReadCount.sh [-h] [-v] [-i INPUT] [-o OUTPUT]"
            echo "                       [-f FORMAT] [-e EXTENSION]"
            echo ""
            echo "Optional arguments:"
            echo " -h                    Show this help page and exit"
            echo " -v                    Show the software's version number"
            echo "                       and exit"
            echo " -i                    The location of the input file(s)"
            echo " -o                    The location of the output file(s)"
            echo " -f                    The format of the input" 
            echo "                       file(s) [single/zip]"
            echo " -e                    The extension of the input"
            echo "                       files(s) [fastq/fasta]"
            echo ""
            echo "The ReadCount tool will count the number of reads in a file" 
            echo "or multiple [zip] files and output these numbers to a text"
            echo "file."
            echo ""
            echo "Files in fastA format should always have a .fasta extension."
            echo "Files in fastQ format should always have a .fastq extension."
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
# Files in fastA format should always have a .fasta extension.
# Files in fastQ format should always have a .fastq extension.
