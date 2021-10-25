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
    
    plt.figure(2)
    plt.plot(position, count, 'r.')
    plt.xlabel("Muon Decay Time (usec)")
    plt.ylabel("Count")
    
    plt.figure(3)
    plt.semilogy(position, count, 'r.')
    plt.xlabel("Muon Decay Time (usec)")
    plt.ylabel("Log of Count")
    
    
    parameters, covs = curve_fit(exponentialDecay, position, count)
    
    a, b, c = parameters[0], parameters[1], parameters[2]
    
    print("Model: " + str(a) + " * exp(-" + str(b) + " * t) + " + str(c))
    
    modelData = []
    
    for item in position:
        modelData += [exponentialDecay(item, a, b, c)]
    
    plt.figure(4)
    plt.plot(position, count, "r.")
    plt.plot(position, modelData, "b-")
    plt.xlabel("Muon Decay Time (usec)")
    plt.ylabel("Count")
    plt.legend(("Raw data", "Model data"))
    plt.show()
    
