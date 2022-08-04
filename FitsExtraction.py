# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 16:06:49 2022

@author: Amani
"""
from astropy.io import fits
import numpy as np



g = "HA.fit"
h = "OIII.fit"
i = "SII.fit"

print("_________________HDULists________________________")
#Below returns a HDUList of the Fit data files.
hdu0 = fits.open(g, mode='readonly',                #String value, fits file name (including extension)
                     memmap=None,                   #No memory mapping required
                     save_backup=False,             #No need to ensure that a backup of the original file is saved before any changes occur
                     cache=True,                    #files are already locally stored
                     lazy_load_hdus=None)           #file isnt too large
        
hdu1 = fits.open(h, mode='readonly', memmap=None, 
                     save_backup=False, cache=True, lazy_load_hdus=None)
hdu2 = fits.open(i, mode='readonly', memmap=None, 
                     save_backup=False, cache=True, lazy_load_hdus=None)

print(hdu0.info(),hdu1.info(),hdu2.info())

print("")
print("_______Impotant Header information from all PrimaryHDU_______")
print("")

head0 = fits.getheader(g) # Could have used (h) or (i) but all info are equivalent

"""
print(head0) is astropy's version of head0.keys() to get key names.
In addition this feature also shows the assigned data to each key.
"""
print("Name of Object: ", fits.getval(g,"OBJECT"))
print("Number of data Axes: ", fits.getval(g,"NAXIS1"))
print("Resolution: ", fits.getval(g,"RESOLUTN")," ", fits.getval(g,"RESOUNIT"))
print("Color Spacing: ", fits.getval(g,"COLORSPC"))
print("Number of Data Axe: ", fits.getval(g,"NAXIS1"))
print("Approximate right ascension in hours: (", fits.getval(g,"OBJCTRA"), ")")
print("Approximate declination: (", fits.getval(g,"OBJCTDEC"), ") degrees")
print("number of bits per data pixel: ", fits.getval(g,"BITPIX"))

print("")

#Displaying the default data Matrix from PrimaryHDU's of HA, OIII and SII
print("__________________HA PrimaryHDU Data_________________________")
print("")
print(hdu0[0].data) 
print("")
print("__________________OIII PrimaryHDU Data_________________________")
print("")
print(hdu1[0].data)
print("")
print("__________________SII PrimaryHDU Data_________________________")
print("")
print(hdu2[0].data)
print("")

#Converting PrimaryHDU's into numpy arrays
g_arr = np.array(hdu0[0].data) #[0] means the Primary whilst [1] would have been ImageHDU
h_arr = np.array(hdu0[0].data)
i_arr = np.array(hdu0[0].data)

#Making sure to close each Fits file after accessing. 
#Must come after converting the "readonly" data to numpy array first
hdu0.close() 
hdu1.close()
hdu2.close()

print("__________________HA array________________________")
print("")
print(g_arr) 
print("")
print("__________________OIII array_________________________")
print("")
print(h_arr)
print("")
print("__________________SII array_________________________")
print("")
print(i_arr)
print("")



