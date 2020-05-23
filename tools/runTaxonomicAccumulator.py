#!/usr/bin/env python3

# Copyright (C) 2018 Jasper Boom

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License version 3 as
# published by the Free Software Foundation.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# Prequisites:
# - Conda environment python >= 3.7
# - conda install -c anaconda pandas
# - conda install -c anaconda xlsxwriter
# - conda install -c anaconda xlrd

# Imports
import argparse
import os
import numpy as np
import pandas as pd


# The getListTaxonDics function.
# This function creates 7 lists containing a number of emptry dictionaries
# equal to the number of files used in the creation of the OTU file or the
# number of BLAST files contained in the input zip file. These lists are then
# returned by the function.
def getListTaxonDics(intFiles):
    lstKingdom = [{} for intNumberOfDics in range(intFiles)]
    lstPhylum = [{} for intNumberOfDics in range(intFiles)]
    lstClass = [{} for intNumberOfDics in range(intFiles)]
    lstOrder = [{} for intNumberOfDics in range(intFiles)]
    lstFamily = [{} for intNumberOfDics in range(intFiles)]
    lstGenus = [{} for intNumberOfDics in range(intFiles)]
    lstSpecies = [{} for intNumberOfDics in range(intFiles)]
    return (
        lstKingdom,
        lstPhylum,
        lstClass,
        lstOrder,
        lstFamily,
        lstGenus,
        lstSpecies,
    )


# The getZipOutput function.
# This function creates a .xlsx file based on the number of files in the input
# zip file. A dictionary is created using the names of these files, this will
# be used to give every column a correct header. It then adds sheets to the
# .xlsx file for every taxon rank based on the dictionary list lstTaxonDics.
def getZipOutput(flOutput, lstFileNames, lstTaxonDics, lstTaxonRanks):
    fosExcelWriter = pd.ExcelWriter(flOutput, engine="xlsxwriter")
    dicIndex = {}
    for intNumber in range(len(lstFileNames)):
        dicIndex[intNumber] = lstFileNames[intNumber]
    for taxonID in range(7):
        dfTemporary = pd.DataFrame(lstTaxonDics[taxonID])
        dfTemporary.rename(index=dicIndex, inplace=True)
        dfTemporary = dfTemporary.T
        dfTemporary = dfTemporary.fillna(0)
        pd.options.display.float_format = "{:,.0f}".format
        dfTemporary.to_excel(fosExcelWriter, sheet_name=lstTaxonRanks[taxonID])
    fosExcelWriter.save()


# The getAccumulationZip function.
# This function creates a list containing all file names extracted from the
# input zip file. It then creates a list with empty dictionaries based on the
# number of files. Every file is opened, the "Taxonomy" column is looped
# through and used to count based on taxon ranks. The getZipOutput function
# is called.
def getAccumulationZip(dirTemporary, flOutput, lstTaxonRanks):
    lstFileNames = []
    for strFile in os.listdir(dirTemporary):
        if strFile.endswith(".tabular"):
            lstFileNames.append(strFile)
        else:
            pass
    lstTaxonDics = getListTaxonDics(len(lstFileNames))
    intFileCounter = 0
    for strFiles in os.listdir(dirTemporary):
        if strFiles.endswith(".tabular"):
            tblReadInput = pd.read_table(dirTemporary + strFiles)
            for strRow in tblReadInput["#Taxonomy"]:
                strTaxonLine = strRow.split("/")
                strTaxonLine = [strName.strip(" ") for strName in strTaxonLine]
                for intTaxonPosition in range(7):
                    try:
                        if (
                            strTaxonLine[intTaxonPosition]
                            in lstTaxonDics[intTaxonPosition][intFileCounter]
                        ):
                            lstTaxonDics[intTaxonPosition][intFileCounter][
                                strTaxonLine[intTaxonPosition]
                            ] += 1
                        else:
                            lstTaxonDics[intTaxonPosition][intFileCounter][
                                strTaxonLine[intTaxonPosition]
                            ] = 1
                    except IndexError:
                        pass
            intFileCounter += 1
    getZipOutput(flOutput, lstFileNames, lstTaxonDics, lstTaxonRanks)


# The getOtuOutputTemporary function.
# This function creates dataframes for the taxonomy ranks it recieves. It also
# renames the empty index for every dataframe. The newly created dataframe is
# returned.
def getOtuOutputTemporary(lstTaxonDic, dicIndex, lstUnknownRow, strFormat):
    dfTemporary = pd.DataFrame(lstTaxonDic)
    if strFormat == "otu_old" or strFormat == "otu_new":
        dfTemporary["No hit"] = lstUnknownRow
    else:
        pass
    dfTemporary.rename(index=dicIndex, inplace=True)
    dfTemporary = dfTemporary.T
    if strFormat == "lca":
        dfTemporary.index = pd.Series(dfTemporary.index).replace(
            np.nan, "No hit"
        )
    else:
        pass
    return dfTemporary


# The getOtuOutput function.
# This function creates a .xlsx file based on the counting done in the
# getAccumulationOtu function. It formats in such a way that it can handle
# the multiple samples that could have been used. If the format of the OTU
# table is with standard BLAST identifications it also isolates the row which
# contains a count of unidentified OTU's, this row will be used to add that
# count to every sheet. If the format is with a LCA process file, the no hit
# row is automatically added through the dictionaries.
# The first sheet created is the kingdom sheet, when that has been created the
# getOtuOutputTemporary function is called to create dataframes for the
# remaining taxonomy ranks. These dataframes are written to the same file as
# the kingdom dataframe was. The getOtuOutputTemporary handles those remaining
# dataframes.
def getOtuOutput(
    flOutput, lstTaxonDics, lstHeaders, intFiles, lstTaxonRanks, strFormat
):
    dfKingdom = pd.DataFrame(lstTaxonDics[0])
    dicIndex = {}
    for intNumber in range(intFiles):
        dicIndex[intNumber] = lstHeaders[intNumber]
    dfKingdom.rename(index=dicIndex, inplace=True)
    dfKingdom = dfKingdom.T
    if strFormat == "otu_old" or strFormat == "otu_new":
        dfKingdom.rename(index={"nan": "No hit"}, inplace=True)
        try:
            lstUnknownRow = dfKingdom.ix["No hit"].values.tolist()
        except KeyError:
            lstUnknownRow = 0
            dfKingdom.loc["No hit"] = 0
    elif strFormat == "lca":
        dfKingdom.index = pd.Series(dfKingdom.index).replace(np.nan, "No hit")
        lstUnknownRow = 0
    else:
        pass
    fosExcelWriter = pd.ExcelWriter(flOutput, engine="xlsxwriter")
    dfKingdom.to_excel(fosExcelWriter, sheet_name=lstTaxonRanks[0])
    for intTaxonRank in range(1, 7):
        dfTemporary = getOtuOutputTemporary(
            lstTaxonDics[intTaxonRank], dicIndex, lstUnknownRow, strFormat
        )
        dfTemporary.to_excel(
            fosExcelWriter, sheet_name=lstTaxonRanks[intTaxonRank]
        )
    fosExcelWriter.save()


# The getAccumulationOtu function.
# This function opens the input file and creates a list containing all file
# names used to create the OTU table. It then creates a list containing a
# number of empty dictionaries. This number is equal to the number of files
# used in the creation of the OTU table. The function then loops through the
# "Taxonomy" column(s) for every file in the OTU table. Depending on the format
# of the OTU table, either with standard BLAST identifications or a LCA process
# file, the taxonomy is retrieved. It will use the read count in every OTU for
# for every file for every taxon rank to accumulate. The function then calls
# the getOtuOutput function.
def getAccumulationOtu(
    flInput, flOutput, lstTaxonRanks, intColumnLength, strFormat
):
    tblReadInput = pd.read_table(flInput)
    intFiles = 0
    lstHeaders = []
    for strHeader in list(tblReadInput):
        if (
            strHeader[:1] != "#"
            and strHeader[:7] != "Unnamed"
            and strHeader[:16] != "OccurrenceStatus"
        ):
            intFiles += 1
            lstHeaders.append(strHeader)
        else:
            pass
    lstTaxonDics = getListTaxonDics(intFiles)
    for intColumns in range(intFiles):
        intRowCounter = 0
        for intRow in tblReadInput[lstHeaders[intColumns]]:
            if strFormat == "otu_old" or strFormat == "otu_new":
                strTaxonLine = str(
                    tblReadInput.iloc[:, intFiles + intColumnLength][
                        intRowCounter
                    ]
                ).split("/")
                strTaxonLine = [strName.strip(" ") for strName in strTaxonLine]
            elif strFormat == "lca":
                strTaxonLine = []
                for intTaxonColumn in range(4, 11):
                    strTaxonLine.append(
                        tblReadInput.iloc[:, intFiles + intTaxonColumn][
                            intRowCounter
                        ]
                    )
            else:
                pass
            intRowCounter += 1
            for intTaxonPosition in range(7):
                try:
                    if (
                        strTaxonLine[intTaxonPosition]
                        in lstTaxonDics[intTaxonPosition][intColumns]
                    ):
                        lstTaxonDics[intTaxonPosition][intColumns][
                            strTaxonLine[intTaxonPosition]
                        ] += intRow
                    else:
                        lstTaxonDics[intTaxonPosition][intColumns][
                            strTaxonLine[intTaxonPosition]
                        ] = intRow
                except IndexError:
                    pass
    getOtuOutput(
        flOutput, lstTaxonDics, lstHeaders, intFiles, lstTaxonRanks, strFormat
    )


# The getBlastOutput function.
# This function creates a .xlsx file based on the counting done in the
# getAccumulationBlast function. Every taxonomy rank gets its own sheet in
# the .xlsx file and gets the corresponding dictionary from lstTaxonDics as
# input.
def getBlastOutput(flOutput, lstTaxonDics, lstTaxonRanks):
    fosExcelWriter = pd.ExcelWriter(flOutput, engine="xlsxwriter")
    for intTaxonPosition in range(7):
        dfTemporary = pd.DataFrame.from_dict(
            lstTaxonDics[intTaxonPosition], orient="index"
        )
        dfTemporary.columns = ["Number of identifications"]
        dfTemporary.to_excel(
            fosExcelWriter, sheet_name=lstTaxonRanks[intTaxonPosition]
        )
    fosExcelWriter.save()


# The getAccumulationBlast function.
# This function opens the input file and creates a list containing 7 empty
# dictionaries. The number 7 equals the number of taxon ranks. It then loops
# through the "Taxonomy" column. Every row in this column is divided into a
# list based on the slash(/) character. Each name in this list is then added to
# their corresponding dictionary or, if it is already present in that
# dictionary, added to the count of that name. The function then calls the
# getBlastOutput function.
def getAccumulationBlast(flInput, flOutput, lstTaxonRanks):
    tblReadInput = pd.read_table(flInput)
    lstTaxonDics = [{} for intTaxonCount in range(7)]
    for strRow in tblReadInput["#Taxonomy"]:
        strTaxonLine = strRow.split("/")
        strTaxonLine = [strName.strip(" ") for strName in strTaxonLine]
        for intTaxonPosition in range(7):
            try:
                if (
                    strTaxonLine[intTaxonPosition]
                    in lstTaxonDics[intTaxonPosition]
                ):
                    lstTaxonDics[intTaxonPosition][
                        strTaxonLine[intTaxonPosition]
                    ] += 1
                else:
                    lstTaxonDics[intTaxonPosition][
                        strTaxonLine[intTaxonPosition]
                    ] = 1
            except IndexError:
                pass
    getBlastOutput(flOutput, lstTaxonDics, lstTaxonRanks)


# The argvs function.
def parseArgvs():
    parser = argparse.ArgumentParser(
        description="Use a python script to accumulate all identifications\
                     based on taxonomy."
    )
    parser.add_argument("-v", action="version", version="%(prog)s [0.1.0]")
    parser.add_argument(
        "-i",
        action="store",
        dest="fisInput",
        help="The location of the input file(s)",
    )
    parser.add_argument(
        "-o",
        action="store",
        dest="fosOutput",
        help="The location of the output file(s)",
    )
    parser.add_argument(
        "-t",
        action="store",
        dest="fosOutputTemp",
        help="The location of the temporary output directory",
    )
    parser.add_argument(
        "-f",
        action="store",
        dest="disFormat",
        help="The format of the input file(s)\
                              [otu_old/otu_new/blast/zip/lca]",
    )
    argvs = parser.parse_args()
    return argvs


# The main function.
def main():
    argvs = parseArgvs()
    lstTaxonRanks = [
        "Kingdom",
        "Phylum",
        "Class",
        "Order",
        "Family",
        "Genus",
        "Species",
    ]
    if argvs.disFormat == "blast":
        getAccumulationBlast(argvs.fisInput, argvs.fosOutput, lstTaxonRanks)
    elif argvs.disFormat == "otu_old":
        intColumnLength = 11
        getAccumulationOtu(
            argvs.fisInput,
            argvs.fosOutput,
            lstTaxonRanks,
            intColumnLength,
            argvs.disFormat,
        )
    elif argvs.disFormat == "otu_new":
        intColumnLength = 10
        getAccumulationOtu(
            argvs.fisInput,
            argvs.fosOutput,
            lstTaxonRanks,
            intColumnLength,
            argvs.disFormat,
        )
    elif argvs.disFormat == "zip":
        getAccumulationZip(argvs.fosOutputTemp, argvs.fosOutput, lstTaxonRanks)
    elif argvs.disFormat == "lca":
        getAccumulationOtu(
            argvs.fisInput, argvs.fosOutput, lstTaxonRanks, 0, argvs.disFormat
        )
    else:
        pass


if __name__ == "__main__":
    main()

# Additional information:
# =======================
#
# Sample names can not start with a "#".
# All columns in a OTU table should have a header starting with "#".
