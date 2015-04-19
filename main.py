# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:40:01 2015

@author: samthomas
"""

import ReadCSV as csv
import Langmuir as lm
import Data as d
import numpy as np
import matplotlib.pyplot as plt

#get the data
data = d.getData()
langmuir = lm.data(data[0], data[1])

#langmuir.populateCurrentArray(data[0], d.isMultiple())
#langmuir.populateVoltageArray(data[1], d.isMultiple())
#langmuir.getLinearVoltage()

langmuir.plotData()
langmuir.plotLogFit()
langmuir.plotLimits()

plt.ylabel("I (mA)")
plt.xlabel("V (volts)")
plt.title("Langmuir Probe Data")

plt.grid()
plt.show()

