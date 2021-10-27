#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 13:22:06 2021

@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def CalculateAvgAndStd(sampleData):
    avg = np.average(sampleData)
    std = np.std(sampleData)
    
    return avg, std

def exponentialDecay(t, a, b, c):
    return a * np.exp(-b * t) + c

def errorbar(times, counts):
    
    halfBinSize = (times[1] - times[0]) / 2.0
    
    timeError, countError = [], []
    
    for i in range(len(counts)):
        if counts[i] == 0:
            timeError += [0]
            countError += [0]
        else:
            timeError += [halfBinSize]
            countError += [1 / counts[i]]
    
    return timeError, countError
    

isCurveFit = input("Does this need to be curve fitted (i.e. run curveFit.py) (Yes/No)? ")

yes = ['Yes', 'yes', 'y', 'Y']
no = ['No', 'no', 'n', 'N']

if isCurveFit in yes:

    fileName = input("Enter data file name: ")
    
    data = np.loadtxt(fileName)
    
    bins = int(input("Enter the number of bins: "))
    
    totalCount = len(data)
    
    title = input("Enter title for plot: ")
    title += " (" + str(bins) + " bins, count: " + str(totalCount) + ")"
    
    average, std = CalculateAvgAndStd(data[:,0])
    
    print("Average:", average, "usec")
    print("Std:", std, "usec")
    
    plt.figure(1)
    count, position, _ = plt.hist(data[:,0], bins)
    plt.xlabel("Muon Decay Time (usec)")
    plt.ylabel("Count")
    plt.title(title)
    plt.show()
    
    position = position[:-1]
    
    zeroIndex = []
    for i in range(len(position)):
        if count[i] == 0.:
            zeroIndex += [i]
    
    count, position = np.delete(count, zeroIndex), np.delete(position, zeroIndex)
    
    plt.figure(2)
    #plt.plot(position, count, 'r.')
    xErr1, yErr1 = errorbar(position, count)
    plt.errorbar(position, count, yerr=yErr1, xerr=xErr1, fmt="r.")
    plt.xlabel("Muon Decay Time (usec)")
    plt.ylabel("Count")
    plt.title(title + " Data Points")
    plt.show()
    
    plt.figure(3)
    plt.semilogy(position, count, 'r.')
    plt.xlabel("Muon Decay Time (usec)")
    plt.ylabel("Log of Count")
    plt.title(title + " Data Points")
    plt.show()
    
    
    parameters, covs = curve_fit(exponentialDecay, position, count)
    
    a, b, c = parameters[0], parameters[1], parameters[2]
    
    print("Model: " + str(a) + " * exp(-" + str(b) + " * t) + " + str(c))
    
    print("Time Error bars: +/-", xErr1[0], "usec")
    print("\nCount Error bars: +/-", yErr1)
    
    modelData = []
    
    for item in position:
        modelData += [exponentialDecay(item, a, b, c)]
    
    plt.figure(4)
    #plt.plot(position, count, "r.")
    plt.errorbar(position, count, yerr=yErr1, xerr=xErr1, fmt="r.")
    plt.plot(position, modelData, "b-")
    plt.xlabel("Muon Decay Time (usec)")
    plt.ylabel("Count")
    plt.title("Experiment Versus Model")
    plt.legend(("Model data", "Raw data"))
    plt.show()
    
    lifeTimeA = (totalCount * 2 * xErr1[0]) / a
    print("Lifetime (A coefficient):", lifeTimeA, "usec")
    
    lifeTimeB = 1 / abs(b)
    print("Lifetime (B coefficient):", lifeTimeB, "usec")
    
