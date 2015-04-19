# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:41:55 2015

@author: samthomas
"""

import numpy as np
import ReadCSV as csv

#this is the file that defines the data
#have this file define a 'getData' function that returns the data array 
#as a tuple: Current first and voltage second.

dataDir = "data/"
currentCh = "C1"
voltageCh = "C3"
baseFileName = "_LP_heatpulse_000"
fileExt = ".txt"
times = 24
csvIndex = 4
zoom = (2200, 7000)
        
def chooseFileName(index, channel):
    if index < 10:
        return dataDir + channel + baseFileName + "0" + str(index) + fileExt
    else:
        return dataDir + channel + baseFileName + str(index) + fileExt
    
    
def getData():
    currArray = []
    voltArray = []
    
    for t in range(times):
        i = csv.read_csv(chooseFileName(t, currentCh), output=True)
        i = i[4]
        i = i[zoom[0]:zoom[1]]
        v = csv.read_csv(chooseFileName(t, voltageCh), output=True)
        v = v[4]
        v = v[zoom[0]:zoom[1]]
        currArray.append(i)
        voltArray.append(v)
        
    return (currArray, voltArray)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    