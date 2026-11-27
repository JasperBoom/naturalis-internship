#!/usr/bin/env python3
# Copyright 2025-2026 Jasper Boom. All rights reserved. See LICENSE.md.

"""
Count the identifications for every taxonomic rank in a BLAST file, an OTU
file or a zip file with BLAST files, and write the totals to a .xlsx file.

Prerequisites:
- Conda environment with Python >= 3.7.
- conda install -c anaconda pandas
- conda install -c anaconda xlsxwriter
- conda install -c anaconda xlrd
"""

# Imports
import argparse
import os
import numpy as np
import pandas as pd


def getListTaxonDics(intFiles):
    """
    This function creates 7 lists containing a number of empty dictionaries
    equal to the number of files used in the creation of the OTU file or the
    number of BLAST files contained in the input zip file. These lists are
    then returned by the function.
    """
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


def getZipOutput(flOutput, lstFileNames, lstTaxonDics, lstTaxonRanks):
    """
    This function creates a .xlsx file based on the number of files in the
    input zip file. A dictionary is created using the names of these files;
    this will be used to give every column a correct header. It then adds
    sheets to the .xlsx file for every taxon rank based on the dictionary
    list lstTaxonDics.
    """
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


def getAccumulationZip(dirTemporary, flOutput, lstTaxonRanks):
    """
    This function creates a list containing all file names extracted from
    the input zip file. It then creates a list with empty dictionaries based
    on the number of files. Every file is opened, and the "Taxonomy" column
    is looped through and used to count based on taxon ranks. The
    getZipOutput function is called.
    """
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


def getOtuOutputTemporary(lstTaxonDic, dicIndex, lstUnknownRow, strFormat):
    """
    This function creates dataframes for the taxonomy ranks it receives. It
    also renames the empty index for every dataframe. The newly created
    dataframe is returned.
    """
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


def getOtuOutput(
    flOutput, lstTaxonDics, lstHeaders, intFiles, lstTaxonRanks, strFormat
):
    """
    This function creates a .xlsx file based on the counting done in the
    getAccumulationOtu function. It formats the file in such a way that it
    can handle the multiple samples that could have been used. If the OTU
    table uses standard BLAST identifications, it also isolates the row
    which contains a count of unidentified OTUs; this row will be used to
    add that count to every sheet. If the format is with an LCA process
    file, the no hit row is automatically added through the dictionaries.

    The first sheet created is the kingdom sheet. When that has been
    created, the getOtuOutputTemporary function is called to create
    dataframes for the remaining taxonomy ranks. These dataframes are
    written to the same file as the kingdom dataframe. The
    getOtuOutputTemporary function handles those remaining dataframes.
    """
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


def getAccumulationOtu(
    flInput, flOutput, lstTaxonRanks, intColumnLength, strFormat
):
    """
    This function opens the input file and creates a list containing all
    file names used to create the OTU table. It then creates a list
    containing a number of empty dictionaries. This number is equal to the
    number of files used in the creation of the OTU table. The function then
    loops through the "Taxonomy" column(s) for every file in the OTU table.
    Depending on the format of the OTU table, either with standard BLAST
    identifications or an LCA process file, the taxonomy is retrieved. It
    uses the read count in every OTU, for every file and every taxon rank,
    to accumulate. The function then calls the getOtuOutput function.
    """
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


def getBlastOutput(flOutput, lstTaxonDics, lstTaxonRanks):
    """
    This function creates a .xlsx file based on the counting done in the
    getAccumulationBlast function. Every taxonomy rank gets its own sheet in
    the .xlsx file and gets the corresponding dictionary from lstTaxonDics
    as input.
    """
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


def getAccumulationBlast(flInput, flOutput, lstTaxonRanks):
    """
    This function opens the input file and creates a list containing 7 empty
    dictionaries. The number 7 equals the number of taxon ranks. It then
    loops through the "Taxonomy" column. Every row in this column is divided
    into a list based on the slash (/) character. Each name in this list is
    then added to its corresponding dictionary or, if it is already present
    in that dictionary, added to the count of that name. The function then
    calls the getBlastOutput function.
    """
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


def parseArgvs():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Use a Python script to accumulate all identifications\
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


def main():
    """
    Run the script with the parsed command-line arguments.
    """
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
