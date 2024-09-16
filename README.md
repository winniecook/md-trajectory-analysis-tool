# md-trajectory-analysis-tool
This Python script analyzes molecular dynamics (MD) trajectories, calculates Root Mean Square Deviation (RMSD) and Radial Distribution Function (RDF), and generates informative plots.


## Features

- Reads MD trajectory data from CSV files
- Calculates and plots RMSD
- Calculates and plots RDF
- Identifies peaks in the RDF
- Computes average structure

## Requirements

- Python 3.6+
- NumPy
- Pandas
- Matplotlib
- SciPy

For a complete list of dependencies, see `requirements.txt`.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/md-trajectory-analysis-tool.git
   cd md-trajectory-analysis-tool
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Prepare your MD trajectory data in a CSV file named `md_trajectory.csv` with the following format:
   ```
   time,x,y,z
   0,1.000,2.000,3.000
   1,1.023,2.015,3.042
   ...
   ```

2. Place the `md_trajectory.csv` file in the same directory as the script.

3. Run the script:
   ```
   python md-analysis-script-v6.py
   ```

4. The script will generate the following output:
   - RMSD plot (saved as `rmsd_plot.png`)
   - RDF plot (saved as `rdf_plot.png`)
   - Average structure (saved as `average_structure.csv`)
   - Console output with RDF peak positions
