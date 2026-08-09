# NATURALIS-INTERNSHIP tools
This folder contains the core executable scripts used by the Naturalis
internship Galaxy tooling. These are the underlying processing utilities that
are called by wrappers and Galaxy XML definitions to perform data extraction,
metadata handling, taxonomy-related processing, and UMI-related analysis logic.

Current tool scripts in this directory include getInformation.R,
getMetaData.py, getScientificName.py, runTaxonomicAccumulator.py, and
umi-isolation.py.

This codebase reflects 2018 internship work and should be interpreted as
student-quality, strongly learning-oriented implementation. The main objective
during development was to gain practical experience with scripting and Galaxy
tool integration workflows rather than to deliver production-level software
architecture.

Special note on UMI isolation: the UMI isolation tool was developed further
outside this repository after the internship period. Development later stopped,
and the tool was brought back into this repository so all related internship
tooling remains available in one place for reference and continuity.

```text
Copyright (C) 2025 Jasper Boom. All rights reserved.

Proprietary and confidential. Unauthorized use, copying, modification,
distribution, reverse engineering, disclosure, or creation of derivative
works is strictly prohibited without prior written permission from
Jasper Boom.
```