
# Molecular Dynamics Analysis in R

## Overview
This branch contains an R-based analysis of molecular dynamics trajectories using Quarto for reproducible documentation.

This an extension/alternative to previous python MD analysis 

## Contents
- `analysis/md_analysis.qmd`: Main analysis document
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
