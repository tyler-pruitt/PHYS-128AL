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


lines = []

with open("bins.txt") as binsDataFile:
    lines = binsDataFile.readlines()

lineCount = int(len(lines) / 3)

binsDataFile.close()


# Reorganize input data

for i in range(len(lines)):
    lines[i] = lines[i][:-1]
    lines[i] = lines[i].split(",")
    lines[i][1] = int(lines[i][1])


lifetimeFile = open("lifetimes.txt", "w+")


# For each line in bins.txt
for line in lines:
    fileName = line[0]
    
    data = np.loadtxt(fileName)
    
    bins = line[1]
    
    totalCount = len(data)
    
    title = line[2]
    title += " (" + str(bins) + " bins, count: " + str(totalCount) + ")"
    
    plt.figure()
    count, position, _ = plt.hist(data[:,0], bins)
    plt.xlabel("Muon Decay Time (usec)")
    plt.ylabel("Count")
    plt.title(title)
    #plt.show()
    
    position = position[:-1]
    
    zeroIndex = []
    for j in range(len(position)):
        if count[j] == 0.:
            zeroIndex += [j]
    
    count, position = np.delete(count, zeroIndex), np.delete(position, zeroIndex)
    
    plt.figure()
    xErr1, yErr1 = errorbar(position, count)
    plt.errorbar(position, count, yerr=yErr1, xerr=xErr1, fmt="r.")
    plt.xlabel("Muon Decay Time (usec)")
    plt.ylabel("Count")
    plt.title(title)
    #plt.show()
    
    
    parameters, covs = curve_fit(exponentialDecay, position, count)
    
    a, b, c = parameters[0], parameters[1], parameters[2]
    
    lifetimeA = (totalCount * 2 * xErr1[0]) / a
    lifetimeFile.write(str(bins) + ",A," + str(lifetimeA) + "\n")
    
    lifetimeB = 1 / abs(b)
    lifetimeFile.write(str(bins) + ",B," + str(lifetimeB) + "\n")

lifetimeFile.close()

