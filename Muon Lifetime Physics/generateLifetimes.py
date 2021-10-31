#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:25:27 2021

@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from methods import exponentialDecay
from methods import errorbar


start = int(input("Enter min of bin range: "))
end = int(input("Enter max of bin range: "))

bins = list(range(start, end+1))

dataFileName = input("Enter data file name: ")
data = np.loadtxt(dataFileName)

lifetimeFile = open("lifetimes.txt", "w+")


# For each bin calculate the two lifetimes and write them out to lifetimes.txt
for i in range(len(bins)):
    
    binNum = bins[i]
    
    totalCount = len(data)
    
    title = dataFileName + " (" + str(binNum) + " bins, count: " + str(totalCount) + ")"
    
    # Obtain count, position for x, y values for the curve fitting
    plt.figure()
    count, position, _ = plt.hist(data[:,0], binNum)
    plt.xlabel("Muon Decay Time (usec)")
    plt.ylabel("Count")
    plt.title(title)
    #plt.show()
    
    # Make position the same size as count
    position = position[:-1]
    
    # Remove the zero count data points obtained from the histogram
    zeroIndex = []
    for j in range(len(position)):
        if count[j] == 0.:
            zeroIndex += [j]
    
    count, position = np.delete(count, zeroIndex), np.delete(position, zeroIndex)
    
    # Determine the time error and count error
    plt.figure()
    xErr, yErr = errorbar(position, count)
    plt.errorbar(position, count, yerr=yErr, xerr=xErr, fmt="r.")
    plt.xlabel("Muon Decay Time (usec)")
    plt.ylabel("Count")
    plt.title(title)
    #plt.show()
    
    
    parameters, covs = curve_fit(exponentialDecay, position, count, sigma=yErr, bounds=(0, np.inf))
    
    a, b, c = parameters[0], parameters[1], parameters[2]
    
    lifetimeA = (totalCount * 2 * xErr[0]) / a
    lifetimeFile.write(str(binNum) + ",A," + str(lifetimeA) + "\n")
    
    lifetimeB = 1 / abs(b)
    lifetimeFile.write(str(binNum) + ",B," + str(lifetimeB) + "\n")

lifetimeFile.close()

