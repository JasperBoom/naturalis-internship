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
- Changed the creator email address in `xml/umi-isolation.xml` to
  `contact@boom.frl`.
- Kept the documentation, scripts, and XML wrappers within 79 characters.
  URLs and the UMI format example keep their original lines.
- Converted the comment-block function headers in the Python scripts to
  docstrings, and moved the prerequisites into the module docstrings.
- Gave the Markdown headings a consistent title case.
- Proofread the documentation, script comments, help text, and Galaxy tool
  text for British English. The tool display names now read "Harvest
  Metadata", "PRINSEQ Sequence Analyser", and "FastQC Sequence Analyser";
  the tool ids are unchanged.
- Clarified the UMI input and output descriptions in the documentation and
  Galaxy help: the script produces tabular and BLAST-ready fasta files,
  while the Galaxy XML wrapper creates the zip archive after clustering.
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

#### Notes
- The external tools that the scripts and wrappers call, such as PRINSEQ,
  FastQC, CutAdapt, and Phyloseq, are third-party software and are not
  covered by `LICENSE.md`.

--------------------

Copyright 2025-2026 Jasper Boom. All rights reserved. See LICENSE.md.