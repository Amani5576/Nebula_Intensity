# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 04:09:06 2022

@author: Amani
"""

import DataAnalysis.py as DA
import matplotlib.pyplot as plt

def show(filename):
    
    if filename.endswith(".fit") == True:
        if filename.startswith("OIII") or filename.startswith("SII") or filename.startswith("HA"):
            if filename == "HA.fit": #Checking whether input data is same as output
                plt.axis("off") #No axis on the image
                plt.title("Hydrogen Alpha") #Title of the image
                plt.imshow(DA.g_arr) #pyplot DAature tospit out the array in an image
                
            elif filename == "OIII.fit":
                plt.axis("off")
                plt.title("Oxygen III")
                plt.imshow(DA.h_arr)
                
            elif filename == "OIII.fit":
                plt.axis("off")
                plt.title("Silicon II")
                plt.imshow(DA.i_arr)
        else: 
            print("You typed the name of file wrongly: HA, OIII and SII are the only existing ones")
    else:
        print("You have not inserted the name properly: <name.fit>")
        
    