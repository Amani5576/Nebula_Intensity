# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 16:06:49 2022

@author: Amani
"""
from astropy.io import fits

g = "HA.fit"
h = "OIII.fit"
i = "SII.fit"

#Dictionary for usage in getting the numpy data and its type
numpyDatTyp = { 8: "numpy.uint8 (note it is UNsigned integer)",
               16: "numpy.int16",
               32: "numpy.int32",
               64: "numpy.int64",
              -32: "numpy.float32",
              -64: "numpy.float64"
              }

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
print("_______Impotant Header information from all PrimaryHDU's_______")
print("")


head0 = fits.getheader(g) # Could have used (h) or (i) but all info are equivalent

print(head0)
"""
print(head0) is astropy's version of head0.keys() to get key names.
In addition this feature also shows the assigned data to each key.
"""
print("Name of Object: ", fits.getval(g,"OBJECT"))
print("Number of data Axes: ", fits.getval(g,"NAXIS1"), "pixels")
print("Resolution: ", fits.getval(g,"RESOLUTN")," ", fits.getval(g,"RESOUNIT"))
print("Color Spacing: ", fits.getval(g,"COLORSPC"))
print("Approximate right ascension in hours: (", fits.getval(g,"OBJCTRA"), ")")
print("Approximate declination: (", fits.getval(g,"OBJCTDEC"), ") degrees")

BITPIXData = fits.getval(g,"BITPIX")
if BITPIXData in numpyDatTyp:
    print("number of bits per data pixel: ", BITPIXData, " meaning of type ", numpyDatTyp[BITPIXData])

print("")

#Displaying the default data Matrix from PrimaryHDU's of HA, OIII and SII
print("__________________HA ImageHDU Data_________________________")
print("")
print(hdu0[1].data) 
print("")
print("__________________OIII ImageHDU Data_________________________")
print("")
print(hdu1[1].data)
print("")
print("__________________SII ImageHDU Data_________________________")
print("")
print(hdu2[1].data)
print("")

