# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:55:27 2015

@author: samthomas
"""

import numpy as np

def lineFit(xVal, yVal):
    coef = getCoef(xVal, yVal, 1) #coefficients
    return getArrayFromCoef(coef, xVal, yVal, 1)
    
def polyFit(xVal, yVal, power):
    coef = getCoef(xVal, yVal, power)
    return getArrayFromCoef(coef, xVal, yVal, power)
    
def logFit(x, y):
    #array = []
    logVal = np.log(np.abs(y))
    fit = lineFit(x, logVal)
    array = np.e**np.array(fit)
    return array
    
def getCoef(x, y, power):
    return np.polyfit(x, y, power)
    
def getArrayFromCoef(coefficients, xVal, yVal, power):
    coef = coefficients
    lineVal = []
    for x in xVal:
        p = power #counter for power
        c = 0 #counter for coef
        val = 0
        while p > -1:
            val += (coef[c] * toPower(x,p))
            p -= 1
            c += 1
        lineVal.append(val)
    return lineVal
    
def toPower(val, deg):
    if (deg == 0):
        return 1
    v = val
    for i in range(deg-1):
        v *= val
    return v