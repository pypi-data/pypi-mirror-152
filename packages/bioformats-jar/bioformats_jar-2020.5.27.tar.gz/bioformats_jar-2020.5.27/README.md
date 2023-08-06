# bioformats_jar

[![License](https://img.shields.io/pypi/l/bioformats_jar.svg?color=green)](https://github.com/tlambert03/bioformats_jar/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/bioformats_jar.svg?color=green)](https://pypi.org/project/bioformats_jar)
[![Python Version](https://img.shields.io/pypi/pyversions/bioformats_jar.svg?color=green)](https://python.org)
[![CI](https://github.com/tlambert03/bioformats_jar/actions/workflows/ci.yml/badge.svg)](https://github.com/tlambert03/bioformats_jar/actions/workflows/ci.yml)

## deprecated

This package is deprecated.  You should use [scyjava](https://github.com/scijava/scyjava) to download and import jars.  The functionality in this
package can be accomplished using scyjava as follows:

```python
import jpype
import scyjava

scyjava.config.endpoints.append('ome:formats-gpl:6.7.0')
scyjava.start_jvm()
loci = jpype.JPackage("loci")
loci.common.DebugTools.setRootLevel("ERROR")
```

This package remains only for packages that already depend on it.

## usage

```python
from bioformats_jar import get_loci, set_loci_log_level

# start the JVM and get the loci module
loci = get_loci()

# optionally:
set_loci_log_level("DEBUG")  # by default "ERROR"
```

The following environment variables can also be used:

- `BIOFORMATS_VERSION` - version of bioformats to use.  by default "LATEST"
- `BIOFORMATS_LOG_LEVEL` - logging level for loci tools. by default "ERROR"
- `BIOFORMATS_LICENSE` - license version of bioformats to use.  must be either
  `"gpl"` or `"bsd"`.  By default `"gpl"`

*see also:*

- [Bioformats Docs](https://docs.openmicroscopy.org/bio-formats/latest)
- [Javadocs](https://downloads.openmicroscopy.org/bio-formats/latest/api/) with the loci API

## install

```sh
pip install bioformats-jar
```

```sh
conda install -c conda-forge bioformats-jar
```
