# Intensity Spectra of Nebulae
# Rofhiwa Matumba
# 3931762

from DataAnalysis import g_arr, h_arr, i_arr # Importing arrays from Amani's code
import matplotlib.pyplot as plt # Import matplotlib library for plotting
import numpy as np # Import numpy library for array arithmetic

files = [g_arr, h_arr, i_arr] # Create a list of filenames
names = ["Hydrogen Alpha", "Oxygen III", "Silicon II"]

def plot_spectrum(file): # Create a function to plot the spectrum
    pixels = []
    for row in file:
        pixels.append(np.mean(row)) # Flatten the data into a single array by getting averages of each image row

    # Plot the resultant spectrum
    plt.plot(range(len(pixels)), pixels)
    plt.xlabel("Pixel Number")
    plt.ylabel("Light Intensity")

for file in files:
    plot_spectrum(file)

plt.title(f"Intensity Spectrum of Nebulae") # Title of the plot
plt.legend(names) # Legend of the plot
plt.figure()

# Individual spectra for each nebula

for i, file in enumerate(files):
    plot_spectrum(file)
    plt.title(names[i]) # Title of the plot
    plt.figure() # Show plot in its own window

plt.show() # Display all the spectra on the screen at once
