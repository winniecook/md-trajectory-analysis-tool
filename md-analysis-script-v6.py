import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import io

def read_trajectory(filename="md_trajectory.csv"):
    try:
        # Read the file content
        with open(filename, 'r') as f:
            content = f.read().strip()

        # Remove triple backticks if present
        if content.startswith("```") and content.endswith("```"):
            content = content[3:-3].strip()

        # Use StringIO to create a file-like object from the string
        csv_data = io.StringIO(content)

        # Read the CSV data
        df = pd.read_csv(csv_data)
        
        print("Successfully read data from", filename)
        print("\nDataFrame info:")
        print(df.info())
        print("\nFirst few rows:")
        print(df.head())
        
        # Set 'time' as index
        df.set_index('time', inplace=True)
        
        return df
    except Exception as e:
        print(f"Error in read_trajectory: {str(e)}")
        raise

def calculate_rmsd(traj):
    ref_structure = traj.iloc[0, :]  # Use first frame as reference
    rmsd = np.sqrt(((traj - ref_structure) ** 2).sum(axis=1) / traj.shape[1])
    return rmsd

def calculate_rdf(traj, bins=100, max_distance=10):
    distances = np.sqrt(((traj - traj.mean()) ** 2).sum(axis=1))
    hist, bin_edges = np.histogram(distances, bins=bins, range=(0, max_distance))
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    rdf = hist / (4 * np.pi * bin_centers**2)
    return bin_centers, rdf

def plot_rmsd(time, rmsd):
    plt.figure(figsize=(10, 6))
    plt.plot(time, rmsd)
    plt.xlabel("Time")
    plt.ylabel("RMSD")
    plt.title("Root Mean Square Deviation")
    plt.savefig("rmsd_plot.png")
    plt.close()
    print("RMSD plot saved as rmsd_plot.png")

def plot_rdf(r, rdf):
    plt.figure(figsize=(10, 6))
    plt.plot(r, rdf)
    plt.xlabel("r")
    plt.ylabel("g(r)")
    plt.title("Radial Distribution Function")
    plt.savefig("rdf_plot.png")
    plt.close()
    print("RDF plot saved as rdf_plot.png")

def main():
    try:
        traj = read_trajectory()
        
        rmsd = calculate_rmsd(traj)
        plot_rmsd(traj.index, rmsd)
        
        r, rdf = calculate_rdf(traj)
        plot_rdf(r, rdf)
        
        # Find peaks in RDF
        peaks, _ = find_peaks(rdf, height=0.1)
        print("RDF peak positions:")
        print(r[peaks])
        
        # Calculate average structure
        avg_structure = traj.mean()
        avg_structure.to_csv("average_structure.csv")
        print("Average structure saved as average_structure.csv")
        
        print("Analysis completed successfully. Check the current directory for output files.")
        
    except Exception as e:
        print(f"An error occurred in main: {str(e)}")
        print("Please check your input file structure and ensure it contains the necessary data.")

if __name__ == "__main__":
    main()
