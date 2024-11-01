# Molecular Dynamics Analysis in R

## Overview
This repository contains an R implementation of molecular dynamics trajectory analysis, originally developed in Python and translated to R for educational purposes. The analysis includes calculations of Root Mean Square Deviation (RMSD) and Radial Distribution Function (RDF), with interactive visualisations created using R's modern data science ecosystem.

## Background
The original Python implementation was transformed into an R-based analysis to:
- Demonstrate R's capabilities in scientific computing
- Leverage R's strong statistical analysis features
- Utilise R's excellent visualisation libraries
- Create reproducible documentation using Quarto

## Contents
- `analysis/md_analysis.qmd`: Main analysis document (R implementation)
- `data/`: Directory for data files (when applicable)

## Requirements
- R >= 4.2.0
- Quarto >= 1.3
- Required R packages:
  - tidyverse
  - pracma
  - plotly
  - here
  - knitr
  - broom
  - viridis
  - moments
  - kableExtra

## Usage
1. Install required packages:
```r
install.packages(c(
  "tidyverse", "pracma", "plotly", "here", "knitr",
  "broom", "viridis", "moments", "kableExtra"
))
```

2. Render the analysis:
```r
quarto render analysis/md_analysis.qmd
```

## Features
- Conversion of Python numpy/pandas operations to R tidyverse equivalents
- Enhanced statistical analysis capabilities
- Interactive plotting using plotly
- Reproducible documentation using Quarto

## Note
This is an educational exercise using simulated data for demonstration purposes. The translation from Python to R serves as an example of cross-language implementation of scientific computing concepts.
```
