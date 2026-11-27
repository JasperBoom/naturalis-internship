#!/usr/bin/env python3
# Copyright 2025-2026 Jasper Boom. All rights reserved. See LICENSE.md.

"""
Retrieve the accepted taxonomic names for the species names in an input
file, using either the Global Names API or the TNRS API.

Prerequisites:
- Python with pandas.
- curl.
- scientific-name.xml names a container that provides them.
"""

# Imports
import argparse
import re
import pandas as pd
import subprocess as sp


def getScientificName(
    lstSpecies, lstOtuNames, strProcess, strFormat, strOutputPath
):
    """
    This function loops through the names list. If the name is either "nan"
    or "unknown species", an empty entry is added to the lstScientificNames
    list. Otherwise, every species name is transformed into a correct format
    in order to support either the Global Names API or the TNRS API. The API
    is called and the accepted name is isolated. This name is then added to
    lstScientificNames. When all names have been processed, a new tabular
    file is created with a column containing the original input names, the
    accepted name and, when using an OTU file, the OTU names.
    """
    lstScientificNames = []
    for strRow in lstSpecies:
        if strRow == "nan" or strRow == "unknown species":
            lstScientificNames.append("")
        else:
            try:
                lstRow = strRow.split()
                strSpeciesCommand = "%20".join(lstRow)
                if strProcess == "global":
                    strCommand = (
                        "http://resolver.globalnames.org/"
                        + "name_resolvers.json?names="
                        + strSpeciesCommand
                        + "&best_match_only"
                    )
                    strSearch = "canonical_form"
                    strTitle = "Accepted taxonomic name (Global Names)"
                elif strProcess == "tnrs":
                    strCommand = (
                        "http://tnrs.iplantc.org/tnrsm-svc/"
                        + "matchNames?retrieve=best&names="
                        + strSpeciesCommand
                    )
                    strSearch = "nameScientific"
                    strTitle = "Accepted taxonomic name (TNRS)"
                rafTrnsApi = sp.Popen(
                    ["curl", "-X", "GET", strCommand],
                    stdout=sp.PIPE,
                    stderr=sp.PIPE,
                    text=True,
                )
                strOut, strError = rafTrnsApi.communicate()
                intScientificNameStart = re.search(strSearch, strOut).end()
                intScinetificNameEnd = re.search(
                    '"', strOut[intScientificNameStart + 3 :]
                ).start()
                strName = strOut[intScientificNameStart + 3 :][
                    :intScinetificNameEnd
                ]
                lstScientificNames.append(strName.strip(" "))
            except AttributeError:
                lstScientificNames.append("")
    if strFormat == "otu_old" or strFormat == "otu_new":
        dfScientificNames = pd.DataFrame(
            {"#OTU ID": lstOtuNames, "Input name": lstSpecies}
        )
    else:
        dfScientificNames = pd.DataFrame({"Input name": lstSpecies})
    dfScientificNames[strTitle] = lstScientificNames
    strOutputPath = strOutputPath + "flNewOutput.tabular"
    dfScientificNames.to_csv(
        strOutputPath, sep="\t", encoding="utf-8", index=False
    )


def getNameColumn(flInput, flOutput, strProcess, strFormat):
    """
    This function isolates a list of names used for the name resolution
    process. When processing an OTU file with standard BLAST
    identifications, the names are isolated based on the taxonomy column at
    the end of an OTU file. Species names are extracted from the taxonomy
    column. When processing an OTU file with an LCA process file, the names
    are extracted from the lowest common ancestor column. When processing a
    BLAST file, the names are isolated from the taxonomy column and
    extracted per row. The species column is then sent to the
    getScientificName function.
    """
    tblReadInput = pd.read_table(flInput)
    lstOtuNames = tblReadInput.iloc[:, 0]
    if strFormat == "otu_old":
        intColumnLength = 11
    elif strFormat == "otu_new":
        intColumnLength = 10
    else:
        pass
    if strFormat == "otu_old" or strFormat == "otu_new":
        lstSpecies = []
        intFiles = 0
        for strHeader in list(tblReadInput):
            if (
                strHeader[:1] != "#"
                and strHeader[:7] != "Unnamed"
                and strHeader[:16] != "OccurrenceStatus"
            ):
                intFiles += 1
        tblTaxonomyColumn = tblReadInput.iloc[:, intFiles + intColumnLength]
        for strRow in tblTaxonomyColumn:
            strTaxonLine = str(strRow).split("/")
            strTaxonLine = [strName.strip(" ") for strName in strTaxonLine]
            lstSpecies.append(strTaxonLine[-1])
    elif strFormat == "lca":
        intFiles = 0
        for strHeader in list(tblReadInput):
            if (
                strHeader[:1] != "#"
                and strHeader[:7] != "Unnamed"
                and strHeader[:16] != "OccurrenceStatus"
            ):
                intFiles += 1
        lstSpecies = tblReadInput.iloc[:, intFiles + 3]
    elif strFormat == "blast":
        lstSpecies = []
        for strRow in tblReadInput["Taxonomy"]:
            strTaxonLine = str(strRow).split("/")
            strTaxonLine = [strName.strip(" ") for strName in strTaxonLine]
            lstSpecies.append(strTaxonLine[-1])
    else:
        pass
    getScientificName(lstSpecies, lstOtuNames, strProcess, strFormat, flOutput)


def parseArgvs():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Use a Python script to\
                                                  utilise either the Global\
                                                  Names API or the TNRS API to\
                                                  collect accepted taxonomic\
                                                  names.")
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
        "-s",
        action="store",
        dest="disProcess",
        help="The name resolution service [global/tnrs]",
    )
    parser.add_argument(
        "-f",
        action="store",
        dest="disFormat",
        help="The format of the input file(s) [otu_old/otu_new/lca/blast]",
    )
    argvs = parser.parse_args()
    return argvs


def main():
    """
    Run the script with the parsed command-line arguments.
    """
    argvs = parseArgvs()
    getNameColumn(
        argvs.fisInput, argvs.fosOutput, argvs.disProcess, argvs.disFormat
    )


if __name__ == "__main__":
    main()
