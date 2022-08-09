# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 04:09:06 2022

@author: Amani
"""

from DataAnalysis import g_arr, h_arr, i_arr #Importing arrays

import matplotlib.pyplot as plt

colors = plt.cm.Greys #Making Background black and data white.

def show(filename):
    
    if filename.endswith(".fit") == True:
        if filename.startswith("OIII") or filename.startswith("SII") or filename.startswith("HA"):
            if filename == "HA.fit": #Checking whether input data is same as output
                N1 = plt.Normalize(g_arr.min(), g_arr.max())
                #Creation of a normalizer based on min value to max value
                """Normalizing colour band makes sure
                entire range of black to white is 
                used for particular data set""" 
                g_arr_norm = colors(N1(g_arr)) #Normalizing the matrix values
                '''new matrix will have assigned colours for each pixel
                   based on pixel value. The higher the value the brighter the grey 
                   (towards white) and the lower the value the darker the grey (towards black)
                '''
                
                plt.axis("off") #No axis on the image
                plt.title("Hydrogen Alpha") #Title of the image
                plt.imshow(g_arr_norm) #pyplot DAature tospit out the array in an image
                
            elif filename == "OIII.fit":
                N2 = plt.Normalize(h_arr.min(), h_arr.max())
                h_arr_norm = colors(N2(h_arr))
                plt.axis("off")
                plt.title("Oxygen III")
                plt.imshow(h_arr_norm)
                
            elif filename == "SII.fit":
                N3 = plt.Normalize(i_arr.min(), i_arr.max())
                i_arr_norm = colors(N3(i_arr))
                plt.axis("off")
                plt.title("Silicon II")
                plt.imshow(i_arr_norm)
        else: 
            print("You typed the name of file wrongly: HA, OIII and SII are the only existing ones")
    else:
        print("You have not inserted the name properly: <name.fit>")