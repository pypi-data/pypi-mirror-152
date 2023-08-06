# PRIME: Command Line Metrics Tool

> A complete installer for PRIME (Transitioning from CLIME)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6477789.svg)](https://doi.org/10.5281/zenodo.6477789)
[![Release Project](https://github.com/SoftwareSystemsLaboratory/clime/actions/workflows/release.yml/badge.svg)](https://github.com/SoftwareSystemsLaboratory/clime/actions/workflows/release.yml)

## Table of Contents

- [PRIME: Command Line Metrics Tool](#prime-command-line-metrics-tool)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
    - [Licensing](#licensing)
  - [Developer Tooling](#developer-tooling)
    - [Operating System](#operating-system)
    - [Shell Software](#shell-software)
  - [Bundled Projects](#bundled-projects)

## About

The Software Systems Laboratory (SSL) PRIME (PRocess Internal Metrics) project is a collection of `python` tools that can be used on any Git repository to generate longitudinal graphs of classical process metrics.

You can install the entirety of the PRIME project from Pypi with `pip install --upgrade pip clime-metrics`.

### Licensing

These tools can be modified by outside teams or individuals for usage of their own personal projects.

This project is licensed under the BSD-3-Clause. See the [LICENSE](LICENSE) for more information.

## Developer Tooling

To maximize the utility of this project and the greater SSL PRIME project, the following dependencies are **required**:

### Operating System

All tools developed for the greater SSL PRIME project **target** Mac OS and Linux. PRIME is not supported or recommended to run on Windows *but can be modified to do so at your own risk*.

### Shell Software

The following software **is required** to run the tools:

- `cloc`
- `git`
- `python 3.9.6` or newer
- `sloccount`

The following software **is optional** to run the tools:

- `jq`
- `parallel`
- `Parallel::ForkManager` Perl package

## Bundled Projects

This projects bundles the following `python` projects into one `pip` installable:

- [PRIME Badges](https://github.com/SoftwareSystemsLaboratory/prime-badges)
- [PRIME Bus Factor](https://github.com/SoftwareSystemsLaboratory/prime-bus-factor)
- [PRIME Commits](https://github.com/SoftwareSystemsLaboratory/prime-commits)
- [PRIME GitHub Repository Searcher](https://github.com/SoftwareSystemsLaboratory/prime-github-repository-searcher)
- [PRIME Issue Density](https://github.com/SoftwareSystemsLaboratory/prime-issue-density)
- [PRIME Issue Spoilage](https://github.com/SoftwareSystemsLaboratory/prime-issue-spoilage)
- [PRIME Issues](https://github.com/SoftwareSystemsLaboratory/prime-issues)
- [PIME JSON Converter](https://github.com/SoftwareSystemsLaboratory/prime-json-converter)
- [PRIME Productivity](https://github.com/SoftwareSystemsLaboratory/prime-productivity)
