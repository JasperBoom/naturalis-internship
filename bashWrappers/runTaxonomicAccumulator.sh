#!/usr/bin/env bash
# Author: Jasper Boom

# Prequisites:
# - Conda environment python >= 3.7
# - conda install -c anaconda pandas
# - conda install -c anaconda xlsxwriter
# - conda install -c anaconda xlrd

# The getZipOutput function.
# This function copies the input file to the temporary storage directory. The
# input file is searched for, based on its .dat extension. This search
# will output the name of the input file which is used to unzip it into the
# temporary zip directory. The runTaxonomicAccumulator.py script is called,
# the output is send to the expected location and the temporary storage
# directory is deleted.
getZipOutput() {
    cp ${fisInput} ${strDirectory}_temp
    strZipName=$(find ${strDirectory}_temp -name "*.dat" -printf "%f\n")
    unzip -q ${strDirectory}_temp/${strZipName} -d ${strDirectory}_temp
    runTaxonomicAccumulator.py -o ${strDirectory}_temp/temporary.xlsx\
                               -t ${strDirectory}_temp/ -f ${disFormat}
    cat ${strDirectory}_temp/temporary.xlsx > ${fosOutput}
    rm -rf ${strDirectory}_temp
}

# The getFormatFlow function.
# This function creates a temporary storage directory in the output directory.
# It then initiates the correct function chain depending on the file format.
# Afther the accumulation processes are done, the output is send to the
# expected location and the temporary storage directory is deleted.
getFormatFlow() {
    strDirectory=${fosOutput::-4}
    mkdir -p "${strDirectory}_temp"
    if [ "${disFormat}" = "blast" ] || [ "${disFormat}" = "otu_old" ] ||\
       [ "${disFormat}" = "otu_new" ] || [ "${disFormat}" = "lca" ]
    then
        runTaxonomicAccumulator.py -i ${fisInput}\
                                   -o ${strDirectory}_temp/temporary.xlsx\
                                   -f ${disFormat}
        cat ${strDirectory}_temp/temporary.xlsx > ${fosOutput}
        rm -rf ${strDirectory}_temp
    elif [ "${disFormat}" = "zip" ]
    then
        getZipOutput
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
            echo "runTaxonomicAccumulator.sh [0.1.0]"
            echo ""

            exit
            ;;
        h)
            echo ""
            echo "Usage: runTaxonomicAccumulator.sh [-h] [-v] [-i INPUT]"
            echo "                                  [-o OUTPUT] [-f FORMAT]"
            echo ""
            echo "Optional arguments:"
            echo " -h                    Show this help page and exit"
            echo " -v                    Show the software's version number"
            echo "                       and exit"
            echo " -i                    The location of the input file(s)"
            echo " -o                    The location of the output file(s)"
            echo " -f                    The format of the input file(s)"
            echo "                       [otu_old/otu_new/blast/zip/lca]"
            echo ""
            echo "The TaxonomicAccumulator tool will count all occurrences of"
            echo "the identifications for every taxonomic level, for every"
            echo "file used as input."
            echo ""
            echo "The tool will handle either a BLAST file, OTU file with old"
            echo "BLAST output, OTU file with new BLAST output, a zip file"
            echo "containing multiple BLAST files or a OTU file with LCA"
            echo "processing added to it."
            echo ""
            echo "Sample names can not start with a '#'."
            echo "All columns in a OTU table should have a header starting"
            echo "with '#'."
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
# Sample names can not start with a "#".
# All columns in a OTU table should have a header starting with "#".
