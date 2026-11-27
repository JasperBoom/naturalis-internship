# Naturalis Internship TODO
## Current
- Request the three BioContainers images below. Until their respective
  images exist, Galaxy cannot run PRINSEQ Analysis, UMI isolation, Metadata,
  Scientific Name or Taxonomic Accumulator.

## BioContainers Images
Every tool runs in a public container. Five tools depend on these three
package combinations, which still need to be built:
- [prinseq-analysis.xml](tools/prinseq-analysis.xml): the `prinseq` image
  lacks the Perl modules Cairo and JSON, which the graph script needs.
- [umi-isolation.xml](tools/umi-isolation.xml): the `vsearch` image has no
  Python to run the script.
- [metadata.xml](tools/metadata.xml),
  [scientific-name.xml](tools/scientific-name.xml) and
  [taxonomic-accumulator.xml](tools/taxonomic-accumulator.xml): one shared
  image with Python, pandas, XlsxWriter and curl, replacing the broad ~2 GB
  image. The versions match those used in the previous image. NumPy is
  installed as a pandas dependency, and Python provides ZIP creation.
  Measure the final image size after it is built.

BioContainers builds these combined, or "mulled", images from a list of
package combinations. The image name is a hash of the packages, so the
names in the XML files are already correct and only need to be built.

To request the images, open a pull request that adds these three lines to
[combinations/hash.tsv](https://github.com/BioContainers/multi-package-containers/blob/master/combinations/hash.tsv),
or use the [helper service](https://biocontainers.pro/#/multipackage):
```text
prinseq=0.20.4,perl-cairo=1.109,perl-json=4.11
python=3.14,vsearch=2.32.0
python=3.12.2,pandas=2.2.0,xlsxwriter=3.1.9,curl=8.5.0
```

Once an image appears on [quay.io](https://quay.io/organization/biocontainers),
remove the "Not built yet" comment from each XML file that uses it and test
the affected tools in Galaxy.

--------------------

Copyright 2025-2026 Jasper Boom. All rights reserved. See LICENSE.md.