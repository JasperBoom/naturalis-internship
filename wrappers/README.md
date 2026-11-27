# Naturalis Internship wrappers
This folder contains shell wrapper scripts used by the Galaxy tools from the
Naturalis internship project. These wrappers are responsible for invoking
command-line tools, passing input and output paths, and preparing execution
flow expected by the corresponding Galaxy XML definitions.

The scripts in this directory include getFastqToFasta.sh, getInformation.sh,
getMetaData.sh, getPrinseqAnalysis.sh, getReadCount.sh, getScientificName.sh,
runCutAdapt.sh, runFastQC.sh, runPrinseqTrimmer.sh, and
runTaxonomicAccumulator.sh.

This code originates from 2018 internship work and should be viewed as
student-level, heavily learning-driven development. The focus at the time was
practical exploration of Galaxy integration and scripting workflows, rather
than production-level engineering standards.

Special note on UMI isolation: the UMI isolation tool was developed further
outside this repository for a period. Development later stopped, and the tool
was brought back into this repository to keep all related internship tooling
consolidated in one place for reference and archival continuity. That is why
there is no UMI isolation wrapper script in this folder: it was superseded by
the Python script in the tools folder and the XML wrapper in the xml folder.

--------------------

Copyright 2025-2026 Jasper Boom. All rights reserved. See LICENSE.md.