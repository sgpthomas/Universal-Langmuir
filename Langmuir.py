# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 17:57:46 2015

@author: samthomas
"""

#imports
import numpy as np
import matplotlib.pyplot as plt
import Fit as fit

class data():
    def __init__(self, currentArr, voltageArr):
        self.originalCurrent = self.getCurrentArray(currentArr)
        self.originalVoltage = self.getVoltageArray(voltageArr)
        self.linearVoltage = self.getLinearVoltage()
        self.lowerLogLimit, self.upperLogLimit = self.getLogLimits()
        
        self.logFit = self.getLogFit()
        #self.populateVariables(currentArr, voltageArr)
        
    def populateVariables(self, currentArr, voltageArr):
        self.originalCurrent = self.populateCurrentArray(currentArr)
        self.originalVoltage = self.populateVoltageArray(voltageArr)
        self.linearVoltage = self.setLinearVoltage()        
    
    def getCurrentArray(self, array):
        a = self._populateArray(array)
        return -a
        
    def getVoltageArray(self, array):
        return self._populateArray(array)
        
    def getLinearVoltage(self):
        if (self.originalVoltage == None):
            print("hi")
        return fit.lineFit(np.arange(len(self.originalVoltage)), self.originalVoltage)
        
    def getLogFit(self):
        ll = self.lowerLogLimit
        ul = self.upperLogLimit
        return fit.logFit(self.linearVoltage[ll:ul], self.originalCurrent[ll:ul])
        
    def getLogLimits(self):
        return (1500, 2600)
        
    def plotData(self, linear=True):
        if (linear):
            plt.plot(self.linearVoltage, self.originalCurrent, color='y')
            plt.plot(self.linearVoltage, fit.polyFit(self.linearVoltage, self.originalCurrent, 6), 'g--', linewidth=0.5)
            print("Linearized Voltage")
        else:
            plt.plot(self.originalVoltage, self.originalCurrent)
            print("Non-linearized Voltage")
        #plt.show()
        
    def plotLogFit(self):
        ll, ul = self.lowerLogLimit, self.upperLogLimit
        plt.plot(self.linearVoltage[ll:ul], self.logFit, linewidth=2)
        
    def plotLogExtension(self):
        coef = fit.getCoef([1,2],[self.logFit[-1], self.logFit[-2]], 1)
        #make line with the coef
        
        
    def plotLimits(self):
        ll, ul = self.lowerLogLimit, self.upperLogLimit
        x1 = self.linearVoltage[ll]
        x2 = self.linearVoltage[ul]
        plt.plot(np.linspace(x1, x1, 2), [-0.01, 0.06], 'k--', linewidth=0.6)
        plt.plot(np.linspace(x2, x2, 2), [-0.01, 0.06], 'k--', linewidth=0.6)
        
        
    def _populateArray(self, array):
        sumArr = None
        if (not isinstance(array[0], float)):
            sumArr = np.zeros(len(array[0]))
            count = 0
            for a in array:
                count += 1
                sumArr += a
            sumArr /= count
        else:
            sumArr = np.zeros(len(array))
            sumArr += array
            
        return sumArr
        

            

if __name__ == "__main__":
    print("This has been run independently")