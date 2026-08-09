# NATURALIS-INTERNSHIP xml
This folder contains Galaxy tool wrapper XML files created during the 2018
Naturalis internship period. The wrappers define how individual tools are
exposed in Galaxy, including input parameters, outputs, command execution,
and user-facing metadata.

The collection includes wrappers for common processing and utility tasks such
as conversion, quality control, trimming, metadata extraction, read counting,
and taxonomic accumulation. Current files include getFastqToFasta.xml,
getInformation.xml, getMetaData.xml, getPrinseqAnalysis.xml, getReadCount.xml,
getScientificName.xml, runCutAdapt.xml, runFastQC.xml, runPrinseqTrimmer.xml,
runTaxonomicAccumulator.xml, and umi-isolation.xml.

This code reflects student-level, learning-focused development from 2018. As
such, design and implementation choices should be read in that historical
context: the primary goal at the time was practical learning and
experimentation with Galaxy tool wrapping, not production-grade
standardization.

Special note on UMI isolation: the UMI isolation tool was developed further
outside this repository for a period. Development later stopped, and the tool
was brought back into this repository to keep related internship
tooling consolidated in one place for archival and reference purposes.

```text
Copyright (C) 2025 Jasper Boom. All rights reserved.

Proprietary and confidential. Unauthorized use, copying, modification,
distribution, reverse engineering, disclosure, or creation of derivative
works is strictly prohibited without prior written permission from
Jasper Boom.
```