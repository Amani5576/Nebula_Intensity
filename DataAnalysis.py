# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 16:06:49 2022

@author: Amani
"""

from FitsExtraction import hdu0, hdu1, hdu2  #importing HDU Data Sets from FIT file
import numpy as np
import matplotlib.pyplot as plt
from statistics import median, multimode, stdev

"""
Converting PrimaryHDU's into numpy arrays by firstly extracting them from 
FitsEctract.py package
"""
g_arr , h_arr, i_arr= np.array(hdu0[1].data), np.array(hdu1[1].data) , np.array(hdu2[1].data) #[0] means the Primary whilst [1] would have been ImageHDU


#Making sure to close each Fits file after accessing. 
#Must come after converting the "readonly" data to numpy array first
hdu0.close() 
hdu1.close()
hdu2.close()

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
        

minToMax_arr = []   #Matrix needed to store 1D data for checking Max and Min 
                    #photons in particular array

print("_____HA Stats________")
print("")
for i in g_arr: #Looping over each individual sub-araay list
    for j in i: #Looping through each element in specific sub-array list
        minToMax_arr.append(j) #Adding each element into 1D array 
minToMax_arr.sort() #Sorts the array in ascending order
max_g, min_g = minToMax_arr[-1], minToMax_arr[0]
print("Maximum photons in a pixel = ", max_g) #Max pixel value
print("Minimum photons in a pixel = ", min_g) #Min Pixel value
print("Median = ", median(minToMax_arr)) #Getting median value
print("Mode(s) = ", multimode(minToMax_arr)) #Getting modal value. Using multimode in case of two modes or more
mean = sum(minToMax_arr)/len(minToMax_arr) #Getting Mean value of data
print("StDev = ", stdev(minToMax_arr, xbar = mean)) #Standard Deviation
minToMax_arr.clear() #Clearing array of all content for OIII and SII data storing
print("")

print("_____OIII Stats________")
print("")
for i in h_arr:
    for j in i:
        minToMax_arr.append(j)
minToMax_arr.sort()
max_h, min_h = minToMax_arr[-1], minToMax_arr[0]
print("Maximum photons in a pixel = ", max_h)
print("Minimum photons in a pixel = ", min_h)
print("Median = ", median(minToMax_arr))
print("Mode(s) = ", multimode(minToMax_arr))
mean = sum(minToMax_arr)/len(minToMax_arr)
print("StDev = ", stdev(minToMax_arr, xbar = mean))
minToMax_arr.clear()
print("")

print("_____SI Stats________")
print("")
for i in i_arr:
    for j in i:
        minToMax_arr.append(j)
minToMax_arr.sort()
max_i, min_i = minToMax_arr[-1], minToMax_arr[0]
print("Maximum photons in a pixel = ", max_i)
print("Minimum photons in a pixel = ", min_i)
print("Median = ", median(minToMax_arr))
print("Mode(s) = ", multimode(minToMax_arr))
mean = sum(minToMax_arr)/len(minToMax_arr)
print("StDev = ", stdev(minToMax_arr, xbar = mean))
print("")

###############################################################################
"""
Below is the part where I Look at levels of high to relatively low intensity
The levels of intensity will be rated by the maximum and minimum values that
were previously collected.

All other lower levels of intensity are counted as negligible if user chooses 
a number of levels.

By increasing the scaling factor, the data is categorized in more levels.
By inputting the number of levels (starting from the highest level; Level 1), 
the data recorded will be categorized upto that level.
"""
###############################################################################
#Creating user-input based Scale-Levels for relative intensity

print("_______________________________________________________________________________________________")
scF = int(input("""
                           
    What Integer Scaling Factor would you like to make 
    in order to create Scale-Levels for relative intensity?                
    E.g. You've chosen Scaling factor to be 6 (6 levels of varying intensity):
         If max = 80 and min = 20 then range is (80 - 20) = 60
         By dividing the range by the Scale we get -> (60)/(6)= 10.
         Hence, from Level 1 (highest intensity) to Level 2
         (Second highest intensity) is a difference of 10.
         
         So what will it be?
         
                """))

Levels = int(input("""
                           
    Levels have been successfully constructed. 
    
    Input the number of level intensities you desire (from highest intesity as the first level)
    e.g. Level 1 -> highest intensity level (Thus, type in the number 1)
         Level 2 -> 2nd highest intensity up until highest intenisty (Thus, type in the number 2)
         Level 3 -> 3rd highest intensity up until highest intenisty (Thus, type in the number 3)
         Level 4 -> 4th highest.... etc.             
                
                """))

print("_______________________________________________________________________________________________")
print("")
print("Note data given as: ( <x-coord> , <y-coord> , <Intensity level> )")
print("")
print("<Intensity level> with a value 0 means its region of highest intensity)")
print("")

gScale, hScale, iScale = (max_g - min_g)/scF, (max_h - min_h)/scF, (max_i - min_h)/scF

XYm_gList = [] #set array holding x and y coordinates for g_arr
XYm_hList = [] #set array holding x and y coordinates for h_arr
XYm_iList = []#set array holding x and y coordinates for i_arr

i_idxNum = 0 #row number
for i in g_arr: #Looping through array of 
    y = i_idxNum #row number or y coordinate of element
    j_idxNum = 0 #column number
    for j in i: #for every element in the list "i"
        mltp = 0 #creating multiplier variable
        x = j_idxNum #column number or x coordinate of element
        while mltp <= scF and mltp<=Levels+1: #If the multiplier vairable smaller than or equal to the scaling factor
                                              #Also making sure to dump the rest of the other data inside an extra lower level
            if j >= max_g - mltp*gScale: 
                """Checking condition if data is in specific intensity level 
                in terms of the pixel's photon number First level is from maximum (inclusive)
                to lover region of that first level (aslo inclusive)"""
                if mltp == Levels+1 or (x,y,mltp-1) in XYm_gList: #If data lands in extra level or there already exists a coordinate
                    break #Get out of while loop rather than recording it
                else:
                    temp_tup = (x,y,mltp) #Trapping tuple of coords and their corresponding multiplier
                    #tuples t in (<x>,<y>, t) where t = 0 are just the pixel coordinates that have maximum number of photons.
                    XYm_gList.append(temp_tup) #Tuple will be having cooridnate elements x, y as well as the reverse multiplier prescribed to that coordinate.
            mltp += 1  #Increasing multiplier to find the next relative intensity
        j_idxNum += 1 #Incrementing the x-cooordinate
    i_idxNum += 1 #Incrementing the y-coordinate

#Same done for h_arr
i_idxNum = 0 #start y coordinate counter from 0 again
for i in h_arr:
    y = i_idxNum
    j_idxNum = 0 #start x coordinate counter from 0 again
    for j in i:
        mltp = 0 
        x = j_idxNum 
        while mltp <= scF and mltp<=Levels+1:
            if j >= max_h - mltp*hScale : 
                if mltp == Levels+1 or (x,y,mltp-1) in XYm_hList:
                    break
                else:
                    temp_tup = (x,y,mltp)
                    XYm_hList.append(temp_tup)
            mltp += 1
        j_idxNum += 1
    i_idxNum += 1

XYm_iList.append(temp_tup)
#Same done for i_arr
i_idxNum = 0 #The "i" here is regards to the i in the for loop. NOT the matrix "i_arr".
for i in i_arr:
    y = i_idxNum
    j_idxNum = 0
    for j in i:
        mltp = 0
        x = j_idxNum 
        while mltp <= scF and mltp<=Levels+1:
            if j >= max_i - mltp*iScale : 
                if mltp == Levels+1 or (x,y,mltp-1) in XYm_iList:
                    break
                else:
                    temp_tup = (x,y,mltp)
                    XYm_iList.append(temp_tup)
            mltp += 1
        j_idxNum += 1
    i_idxNum += 1

#Sorting all tuple elements in the List array
XYm_gList.sort(), XYm_hList.sort(), XYm_iList.sort() #Sorting all lists



if Levels > 1:
    print("Hydrogen Alpha Level 1 -> %d data:" % Levels)
    print("")
    print(XYm_gList)
    print("")
    print("Oxygen III Level 1 -> %d data:" % Levels)
    print("")
    print(XYm_hList)
    print("")
    print("Silicon II Level 1 -> %d data:" % Levels)
    print("")
    print(XYm_iList)
else:
    print("Hydrogen Alpha Level 1 data:")
    print("")
    print(XYm_gList)
    print("")
    print("Oxygen III Level 1 data:")
    print("")
    print(XYm_hList)
    print("")
    print("Silicon II Level 1 data:")
    print("")
    print(XYm_iList)