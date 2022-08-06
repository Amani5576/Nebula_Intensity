# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 16:06:49 2022

@author: Amani
"""

import FitsExtract.py as FE
import numpy as np
import matplotlib.pyplot as plt


"""
Converting PrimaryHDU's into numpy arrays by firstly extracting them from 
FitsEctract.py package
"""
g_arr , h_arr, i_arr= np.array(FE.hdu0[1].data), np.array(FE.hdu1[1].data) , np.array(FE.hdu2[1].data) #[0] means the Primary whilst [1] would have been ImageHDU


#Making sure to close each Fits file after accessing. 
#Must come after converting the "readonly" data to numpy array first
FE.hdu0.close() 
FE.hdu1.close()
FE.hdu2.close()

print("__________________HA array/matrix________________________")
print("")
print(g_arr) 
print("")
print("__________________OIII array/matrix_________________________")
print("")
print(h_arr)
print("")
print("__________________SII array/matrix_________________________")
print("")
print(i_arr)
print("")
print("Please note that 2D arrays are already matrices")
print("")

"""

Below represents an easy method for the user to use the show() function on the
 console to get an output of an image that enables them to see the list 
 arrays/matrices of HA, OIII and SII. Each numbered value in the matrices is a
 quanitity of the number of photons captured by the Telescope. Each element is 
 a pixel containing a specified 
number of photons.

"""
def show(filename):
    
    if filename == "HA.fit": #Checking whether input data is same as output
        plt.axis("off") #No axis on the image
        plt.title("Hydrogen Alpha") #Title of the image
        plt.imshow(g_arr) #pyplot feature tospit out the array in an image
        
    elif filename == "OIII.fit":
        plt.axis("off")
        plt.title("Oxygen III")
        plt.imshow(h_arr)
        
    elif filename == "OIII.fit":
        plt.axis("off")
        plt.title("Silicon II")
        plt.imshow(i_arr)
        

minMax_arr = []   #Matrix needed to store 1D data for checking Max and Min 
                    #photons in particular array

for i in g_arr: #Looping over each individual sub-araay list
    for j in i: #Looping through each element in specific sub-array list
        minMax_arr.append(j) #Adding each element into 1D array 
minMax_arr.sort() #Sorts the array in ascending order
max_g, min_g = minMax_arr[-1], minMax_arr[0]
print("Max Val of HA pixel data = ", max_g) #Max pixel value
print("Min Val of HA pixel data = ", min_g) #Min Pixel value
minMax_arr.clear() #Clearing array of all content for OIII and SII data storing

        
for i in h_arr:
    for j in i:
        minMax_arr.append(j)
minMax_arr.sort()
max_h, min_h = minMax_arr[-1], minMax_arr[0]
print("Max Val of OIII pixel data = ", max_h)
print("Min Val of OIII pixel data = ", min_h)
minMax_arr.clear()

for i in i_arr:
    for j in i:
        minMax_arr.append(j)
minMax_arr.sort()
max_i, min_i = minMax_arr[-1], minMax_arr[0]
print("Max Val of SII pixel data = ", max_i)
print("Min Val of SII pixel data = ", min_i)

"""
Below is the part where I Look at levels of high to relatively low intensity
The levels of intensity will be rated by the maximum and minimum values that
were previously collected.

All other lower levels of intensity are counted as negligible.
"""
#Creating Scale-Levels for relative intensity

scF = 7 #Scaling 

gScale, hScale, iScale = (max_g - min_g)/scF, (max_h - min_h)/scF, (max_i - min_h)/scF

for i in g_arr:
    mltp = 0
    for j in i:
        mltp += 1 #Multiplier (Higher the value, the lower the range)
        if j >= max_g - mltp*gScale: #If pixel is of highest intensity      
            j = 0