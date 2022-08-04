# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 16:06:49 2022

@author: Amani
"""

from pathlib import Path as P
from astropy.io import fits
import numpy as np

HomeDir = P.home()#Gettting the home directory
CurrDir = P.cwd() #Path to current working directory
CurrDirr = P.cwd().parent #Parent folder path
CurrDir0 = P.cwd().parents[0] #Parent folder path
CurrDir1 = P.cwd().parents[1] #Parent folder path
CurrDir2 = P.cwd().parents[2] #Parent folder path