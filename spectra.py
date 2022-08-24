# Intensity Spectra of Nebulae
# Rofhiwa Matumba
# 3931762

from DataAnalysis import arrs, Levels # Importing arrays from Amani's code
from DataAnalysis import XYm_Lists # Importing filtered data from Amani's code
import matplotlib.pyplot as plt # Import matplotlib library for plotting
import numpy as np # Import numpy library for array arithmetic

files = arrs # Create a list of filenames (unfiltered data)
files_filtered = XYm_Lists # Create a list of filtered data
names = ["Hydrogen Alpha", "Oxygen III", "Silicon II"] # Names of nebulae

def plot_spectrum(file): # Create a function to plot the spectrum
    pixels = np.mean(file, axis=1) # Get average of all pixels relative to x-axis

    # Plot the resultant spectrum
    plt.plot(range(len(pixels)), pixels)
    plt.xlabel("Pixel Number (relative to x-axis)")
    plt.ylabel("Light Intensity relative to x-axis (Arbitrary Unit)")

for file in files:
    plot_spectrum(file)

plt.title(f"Intensity Spectrum of Nebulae") # Title of the plot for all nebulae
plt.legend(names) # Legend of the plot
plt.figure() # Show plot in its own window

# Individual spectra for each nebula

for i, file in enumerate(files):
    plot_spectrum(file)
    plt.title(f"{names[i]} Intensity Spectrum") # Title of the plot for each nebula spectrum
    plt.figure() # Show plot in its own window


for i, data in enumerate(files_filtered):
    arr = np.zeros([400,400]) # Create a 400x400 matrix of zeros
    for coord in data: # Loops through each of the filtered data, plots accordingly
        arr[coord[1], coord[0]] = Levels - coord[2] # Adds filtered data to the matrix, including specified intensity levels
        # (Max = Levels - 0, where 0 -> Max intensity)
    plt.title(f"Filtered data for {names[i]}")
    plt.xlabel("Image X-axis")
    plt.axis("off")
    plt.ylabel("Image Y-axis")
    plt.imshow(arr, cmap=plt.cm.magma)
    plt.figure() # Show plot in its own window

    plot_spectrum(arr.transpose())
    plt.title(f"Filtered spectrum data for {names[i]}")
    plt.figure()

plt.show() # Show all the plots at once
