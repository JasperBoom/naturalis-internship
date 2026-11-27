# Naturalis Internship CHANGELOG
## [Unreleased]
### Development build
#### Added
- A licence file.
- A README file.
- A TODO list.
- A CHANGELOG file.
- A Makefile with useful targets.
- An env file for the Makefile variables.
- A logo for the repository. Found in `img/`.
- A table of contents in the root README linking to all Markdown files.
- A documentation overview in `docs/README.md`.
- A UMI isolation section in `docs/DESCRIPTION.md`, so every tool is
  described.
- A standard licence notice in `.env-dev`.
- Blackbook's `Makefile.common`, providing shared help, Docker listing,
  Black formatting, and Python cache-cleanup targets.
- A public BioContainers image in every Galaxy tool XML file, so nothing has
  to be installed on the Galaxy server. `docs/INSTALL.md` explains how to
  add the tools to Galaxy.
- Galaxy list collections as input for FastQC, PRINSEQ Analysis, Read Count,
  and Taxonomic Accumulator, replacing zip files. Galaxy runs the other tools
  once for every file in a collection.
- A tool overview table in `tools/README.md`.
- Steps in `TODO.md` for requesting the three BioContainers images that do not
  exist yet.

#### Changed
- umi-isolation.xml and umi-isolation.py had a large overhaul to improve the
  code quality and maintainability.
  - Updated naming and formatting.
  - Applied Black formatting to the Python script.
  - Deleted the old Bash wrapper; Galaxy can run the Python script directly.
  - Reworked the Python script to fit the new Python version.
- Major rework of the repository structure and files.
- Updated the documentation and README files to reflect the new repository
  structure and files, clarify development intentions, and provide more
  information about the tools.
- Replaced the main licence with Blackbook's reusable version: updated the
  years to 2025-2026, made ownership more specific, excluded third-party
  materials, and changed the contact address to `contact@boom.frl`.
- Replaced full licence blocks with one-line notices referring to
  `LICENSE.md`. Markdown files show the notice below a separator line.
- Changed the creator email address in `umi-isolation.xml` to
  `contact@boom.frl`.
- Kept the documentation, scripts, and XML files within 79 characters.
  URLs and the UMI format example keep their original lines.
- Converted the comment-block function headers in the Python scripts to
  docstrings, and moved the prerequisites into the module docstrings.
- Gave the Markdown headings a consistent title case.
- Proofread the documentation, script comments, help text, and Galaxy tool
  text for British English.
- Clarified the UMI input and output descriptions in the documentation and
  Galaxy help: the script produces tabular and BLAST-ready fasta files,
  while the Galaxy tool creates the zip archive after clustering.
- Removed trailing whitespace.
- Fixed the help and version text of `getMetaData.sh`, which showed the name
  `runMetaData.sh`.
- Simplified the main Makefile to load `.env` and import `Makefile.common`,
  removing duplicated helpers and the old `version` target.
- Moved the environment values to `.env-dev`, with `.env` as a relative
  symlink, and removed `VERSION`.
- Replaced the Naturalis logo with an original cartoon logo in
  `img/naturalis-internship.png`, matching the Blackbook, GO-VIRAL, and
  Minecraft Server logos.
- Merged `xml/` into `tools/`, so every Galaxy tool XML file sits next to its
  script, and removed `xml/README.md`.
- Renamed the tool files, scripts, and tool ids to lower case, with hyphens
  between words and without the get and run prefixes. The R script is now
  `phyloseq-analysis.r`, including a lower-case extension. Galaxy workflows
  that use the old tool ids must be updated:
  - `getFastqToFasta` is now `fastq-to-fasta`.
  - `getInformation` is now `phyloseq-analysis`.
  - `getMetaData` is now `metadata`.
  - `getPrinseqAnalysis` is now `prinseq-analysis`.
  - `getReadCount` is now `read-count`.
  - `getScientificName` is now `scientific-name`.
  - `runCutAdapt` is now `cutadapt`.
  - `runFastQC` is now `fastqc`.
  - `runPrinseq` (`runPrinseqTrimmer.xml`) is now `prinseq-trimmer`.
  - `runTaxonomicAccumulator` is now `taxonomic-accumulator`.
- Rewrote every Galaxy tool XML file in the structure and style of the
  infra-docker-galaxy tools: comment blocks, sections, help text with
  defaults and flags, EDAM topics and operations, citations, and output
  labels named after the input. The display names are now the plain tool
  names, such as "Metadata" and "PRINSEQ Analysis".
- Galaxy now calls CutAdapt, FastQC, PRINSEQ, and GNU Awk directly from the
  XML files. Deleted the Bash wrappers in `wrappers/`.
- Replaced the ~2 GB shared Python container with a pending mulled image
  containing only Python, pandas, XlsxWriter, curl and their dependencies,
  shared by Metadata, Scientific Name and Taxonomic Accumulator.
- The CutAdapt, FastQC, and PRINSEQ tool versions now match the software they
  run: 5.2, 0.12.1, and 0.20.4.
- Removed CutAdapt's `--format` option, which current CutAdapt versions no
  longer accept.
- Fixed the PRINSEQ Trimmer length filters. The old wrapper passed
  `-min_length` and `-max_length`, which PRINSEQ does not know; the tool now
  uses `-min_len` and `-max_len`.
- PRINSEQ Trimmer now gives an empty output file when no reads pass the
  filters.
- Read Count now counts fasta reads by their headers, so wrapped fasta files
  are counted correctly, and no longer writes a "done counting" line.
- Made Read Count's command separators explicit, with immediate failure if
  an input cannot be counted instead of continuing to the collection total.
- Made Taxonomic Accumulator's sanitised collection names unique, including
  names that already end in a numeric suffix.
- FASTQ to FASTA now uses GNU Awk instead of sed.
- Phyloseq Analysis now writes PDF files instead of PostScript, because
  Galaxy has no PostScript datatype.
- Updated the Python scripts for Python 3 and current pandas: `zip` instead of
  `itertools.izip`, text mode for subprocess output, `.iloc` and `.loc`
  instead of the removed `.ix`, and `close()` instead of the removed
  `ExcelWriter.save()`.
- `metadata.py` downloads pictures with curl instead of wget, and follows the
  redirects of the Naturalis API from HTTP to HTTPS.
- `umi-isolation.py` uses the `csv` module instead of pandas. Galaxy zips the
  per-UMI files with Python's `zipfile` module instead of `zip`.
- Fixed FASTQ mode in `umi-isolation.py`: the per-UMI files are fasta files
  but kept the FASTQ "@" headers, which VSEARCH rejects.
- Fixed two bugs in the old `umi-isolation.xml` command. Cheetah read
  `${WORK_DIR}` as its own variable, and without `&&` between the lines, the
  folder assignments became part of the Python command once Galaxy joined
  the lines.
- Replaced the obsolete EDAM topic "Primers" in `umi-isolation.xml` with
  "Probes and primers", and added the EDAM operations "Sequence clustering"
  and "Read binning".
- Updated the documentation to the new tool names, collections, and
  containers.
- Aligned the UMI form labels and help with the other Galaxy tools, including
  defaults and command-line flags, without changing parameters or commands.
- Updated the Python dependency notes and folder-input descriptions, and
  clarified which OTU column headers should start with "#".
- Removed the XML regression-test definitions and instructions after their
  input files were removed.

#### Notes
- The external tools that the Galaxy tools call, such as PRINSEQ, FastQC,
  CutAdapt, and Phyloseq, are third-party software and are not covered by
  `LICENSE.md`.
- The tools were tested in their containers outside Galaxy, not in a running
  Galaxy instance.
- The Global Names, TNRS, and BOLD APIs that the scripts call no longer
  answer at their old addresses. The scripts are kept as they were, so these
  services give no results.

--------------------

Copyright 2025-2026 Jasper Boom. All rights reserved. See LICENSE.md.