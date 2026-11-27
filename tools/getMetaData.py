#!/usr/bin/env python3
# Copyright 2025-2026 Jasper Boom. All rights reserved. See LICENSE.md.

"""
Collect metadata for the species names in an input file: the occurrence
status from the Naturalis API, or pictures from the Naturalis, BOLD and ALA
APIs.

Prerequisites:
- Conda environment with Python >= 3.7.
- conda install -c anaconda pandas
"""

# Imports
import os
import argparse
import re
import math
import itertools
import pandas as pd
import subprocess as sp


def getDownload(strUrl):
    """
    This function downloads an image based on the getPictureUrl function
    output. The name of such an image consists of
    [OTU_ID]-[species_name]-[database].
    """
    rafDownload = sp.Popen(
        ["wget", "-O", strUrl[1], strUrl[0]], stdout=sp.PIPE, stderr=sp.PIPE
    )
    strOut, strError = rafDownload.communicate()


def getPictureUrl(
    strCommand, strStart, strOutputPath, strOtu, lstSpecies, strDatabase
):
    """
    This function calls a database API [Naturalis/BOLD/ALA] and searches
    through the output for a specific string. This string differs depending
    on which database is being searched. After finding this string, the
    image link is isolated. In the case of the BOLD database, a small edit
    needs to be applied in order to create a correct HTTP format. This HTTP
    link, along with a species name linked by _, is returned as output.
    """
    rafApi = sp.Popen(
        ["curl", "-X", "GET", strCommand], stdout=sp.PIPE, stderr=sp.PIPE
    )
    strOut, strError = rafApi.communicate()
    try:
        intUrlStart = re.search(strStart, strOut).end()
        intUrlEnd = re.search('"', strOut[intUrlStart + 3 :]).start()
        strDownload = strOut[intUrlStart + 3 :][:intUrlEnd]
        strSpeciesName = "_".join(lstSpecies)
        strPictureFile = (
            strOutputPath
            + strOtu
            + "-"
            + strSpeciesName
            + "-"
            + strDatabase
            + ".jpg"
        )
        if strDatabase == "BOLD":
            strDownload = strDownload.replace("\\", "")
        else:
            pass
        return strDownload, strPictureFile
    except AttributeError:
        pass


def getBoldApi(strSpeciesCommand, strOutputPath, strOtu, lstSpecies):
    """
    This function creates an API string with the provided name. This API
    string is based on the BOLD API backbone. The created API string is
    included in the call of the getPictureUrl function.
    """
    strBoldCommand = (
        "http://www.boldsystems.org/index.php/API_Public/"
        + "specimen?taxon="
        + strSpeciesCommand
        + "&format=json"
    )
    strBoldUrl = getPictureUrl(
        strBoldCommand, "image_file", strOutputPath, strOtu, lstSpecies, "BOLD"
    )
    return strBoldUrl


def getAlaApi(strSpeciesCommand, strOutputPath, strOtu, lstSpecies):
    """
    This function creates an API string with the provided name. This API
    string is based on the ALA API backbone. The created API string is
    included in the call of the getPictureUrl function.
    """
    strAlaCommand = (
        "http://bie.ala.org.au/ws/search.json?q="
        + strSpeciesCommand
        + "&facets=imageAvailable"
    )
    strAlaUrl = getPictureUrl(
        strAlaCommand, "imageUrl", strOutputPath, strOtu, lstSpecies, "ALA"
    )
    return strAlaUrl


def getPicture(tblReadInput, strOutputPath, tblSpecies):
    """
    This function loops through the names column and OTU column. Every name
    is transformed into a correct format in order to support the database
    APIs. The first database called in this function is the Naturalis
    database. If that call does not provide an image, the BOLD database is
    called. If the call does provide a file, but it is an empty one, the
    BOLD database is also called. The same rules apply to the BOLD calls,
    which means the ALA database is called next. No result after the ALA
    call means no image.
    """
    tblOtu = tblReadInput.iloc[:, 0]
    for strOtu, strSpecies in itertools.izip(tblOtu, tblSpecies):
        try:
            lstSpecies = strSpecies.split()
            strSpeciesCommand = "%20".join(lstSpecies).lower()
            # Naturalis database.
            strNaturalisCommand = (
                "http://api.biodiversitydata.nl/v2/multi"
                + "media/query?identifications.scientific"
                + "Name.scientificNameGroup="
                + strSpeciesCommand
                + "&_fields=service"
                + "AccessPoints"
            )
            strNaturalisUrl = getPictureUrl(
                strNaturalisCommand,
                "accessUri",
                strOutputPath,
                strOtu,
                lstSpecies,
                "NATURALIS",
            )
            if strNaturalisUrl:
                getDownload(strNaturalisUrl)
                if os.stat(strNaturalisUrl[1]).st_size == 0:
                    rafRemove = sp.call(["rm", strNaturalisUrl[1]])
                    # BOLD database.
                    strBoldUrl = getBoldApi(
                        strSpeciesCommand, strOutputPath, strOtu, lstSpecies
                    )
                    if strBoldUrl:
                        getDownload(strBoldUrl)
                        if os.stat(strBoldUrl[1]).st_size == 0:
                            rafRemove = sp.call(["rm", strBoldUrl[1]])
                            # ALA database.
                            strAlaUrl = getAlaApi(
                                strSpeciesCommand,
                                strOutputPath,
                                strOtu,
                                lstSpecies,
                            )
                            if strAlaUrl:
                                getDownload(strAlaUrl)
                                if os.stat(strAlaUrl[1]).st_size == 0:
                                    rafRemove = sp.call(["rm", strAlaUrl[1]])
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    else:
                        # ALA database.
                        strAlaUrl = getAlaApi(
                            strSpeciesCommand,
                            strOutputPath,
                            strOtu,
                            lstSpecies,
                        )
                        if strAlaUrl:
                            getDownload(strAlaUrl)
                            if os.stat(strAlaUrl[1]).st_size == 0:
                                rafRemove = sp.call(["rm", strAlaUrl[1]])
                            else:
                                pass
                        else:
                            pass
                else:
                    pass
            else:
                # BOLD database.
                strBoldUrl = getBoldApi(
                    strSpeciesCommand, strOutputPath, strOtu, lstSpecies
                )
                if strBoldUrl:
                    getDownload(strBoldUrl)
                    if os.stat(strBoldUrl[1]).st_size == 0:
                        rafRemove = sp.call(["rm", strBoldUrl[1]])
                        # ALA database.
                        strAlaUrl = getAlaApi(
                            strSpeciesCommand,
                            strOutputPath,
                            strOtu,
                            lstSpecies,
                        )
                        if strAlaUrl:
                            getDownload(strAlaUrl)
                            if os.stat(strAlaUrl[1]).st_size == 0:
                                rafRemove = sp.call(["rm", strAlaUrl[1]])
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    # ALA database.
                    strAlaUrl = getAlaApi(
                        strSpeciesCommand, strOutputPath, strOtu, lstSpecies
                    )
                    if strAlaUrl:
                        getDownload(strAlaUrl)
                        if os.stat(strAlaUrl[1]).st_size == 0:
                            rafRemove = sp.call(["rm", strAlaUrl[1]])
                        else:
                            pass
                    else:
                        pass
        except AttributeError:
            pass


def getOccurrenceStatus(tblReadInput, strOutputPath, tblSpecies):
    """
    This function loops through the names column generated by the
    getNameColumn function. Every name is transformed into a correct format
    in order to support the Naturalis bioportal API. The Naturalis bioportal
    API is called. The word "occurrenceStatusVerbatim" is searched for in the
    output of the API. The value after the word occurrenceStatusVerbatim is
    isolated and this value is added to the list lstStatus. If no value can
    be found, an empty string is added to the list lstStatus. After every
    species name is processed, the list lstStatus is added to the input file
    as a new column and written to a new file.
    """
    dicOccurrence = {
        "0": "Reported",
        "0a": "Reported correctly, to be refined",
        "1": "Indigenous (undetermined)",
        "1a": "Indigenous: native species",
        "1b": "Indigenous: incidental/periodical species",
        "2": "Introduced (undetermined)",
        "2a": "Introduced: at least 100 years independent survival",
        "2b": "Introduced: 10-100 years independent survival",
        "2c": "Introduced: less than 10 years independent survival",
        "2d": "Introduced: incidental import",
        "3a": "Data deficient",
        "3b": "Incorrectly reported",
        "3c": "To be expected",
        "3d": "Incorrectly used name (auct.)",
        "4": "Miscellaneous",
    }
    lstStatus = []
    for strRow in tblSpecies:
        try:
            lstSpecies = strRow.split()
            strSpeciesCommand = "%20".join(lstSpecies).lower()
            strCommand = (
                "http://api.biodiversitydata.nl/v2/taxon/query?"
                + "acceptedName.scientificNameGroup="
                + strSpeciesCommand
                + "&_fields=occurrenceStatusVerbatim"
            )
            rafNaturalisApi = sp.Popen(
                ["curl", "-X", "GET", strCommand],
                stdout=sp.PIPE,
                stderr=sp.PIPE,
            )
            strOut, strError = rafNaturalisApi.communicate()
            intOccurrenceStart = re.search(
                "occurrenceStatusVerbatim", strOut
            ).end()
            strOccurrence = strOut[
                intOccurrenceStart + 3 : intOccurrenceStart + 5
            ]
            strOccurrenceTotal = (
                strOccurrence.strip(" ")
                + " "
                + dicOccurrence[str(strOccurrence)]
            )
            lstStatus.append(strOccurrenceTotal)
        except AttributeError:
            lstStatus.append("")
    tblReadInput["OccurrenceStatus"] = lstStatus
    strOutputPath = strOutputPath + "flNewOutput.tabular"
    tblReadInput.to_csv(strOutputPath, sep="\t", encoding="utf-8", index=False)


def getNameColumn(flInput, flOutput, strProcess, strFormat):
    """
    This function isolates a list of names used for the metadata processes.
    When processing an OTU file with standard BLAST identifications, the
    names are isolated based on the taxonomy column at the end of an OTU
    file. Species names are extracted from the taxonomy column. When
    processing an OTU file with an LCA process file, the names are extracted
    from the lowest common ancestor column. When processing an accepted
    taxonomic name file, the names are extracted from the third column, but
    if a row is empty, the name in the second column is used. When
    processing a BLAST file, the names are isolated from the taxonomy column
    and extracted per row. Depending on what type of metadata the user
    wants, the species column is sent to the correct functions.
    """
    tblReadInput = pd.read_table(flInput)
    if strFormat == "otu_old":
        intColumnLength = 11
    elif strFormat == "otu_new":
        intColumnLength = 10
    else:
        pass
    if strFormat == "accepted":
        intCounter = 0
        lstSpecies = []
        for strRow in tblReadInput.iloc[:, 2]:
            try:
                if math.isnan(strRow) is True:
                    lstSpecies.append(tblReadInput.iloc[:, 1][intCounter])
            except TypeError:
                lstSpecies.append(strRow)
            intCounter += 1
    elif strFormat == "otu_old" or strFormat == "otu_new":
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
    if strProcess == "occurrences":
        getOccurrenceStatus(tblReadInput, flOutput, lstSpecies)
    elif strProcess == "pictures":
        getPicture(tblReadInput, flOutput, lstSpecies)
    else:
        pass


def parseArgvs():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Use a Python script to\
                                                  utilise the Naturalis, BOLD\
                                                  and ALA APIs to collect\
                                                  metadata.")
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
        "-p",
        action="store",
        dest="disProcess",
        help="The metadata process type [occurrences/pictures]",
    )
    parser.add_argument(
        "-f",
        action="store",
        dest="disFormat",
        help="The format of the input file(s)\
              [otu_old/otu_new/lca/accepted/blast]",
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
