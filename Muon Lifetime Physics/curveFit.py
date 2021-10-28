#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 13:22:06 2021

@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from methods import CalculateAvgAndStd
from methods import exponentialDecay
from methods import errorbar
from methods import leastSquaresDist
from methods import distance


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
    plt.title(title)
    plt.show()
    
    plt.figure(3)
    plt.semilogy(position, count, 'r.')
    plt.xlabel("Muon Decay Time (usec)")
    plt.ylabel("Log of Count")
    plt.title(title)
    plt.show()
    
    
    parameters, covs = curve_fit(exponentialDecay, position, count, bounds=(0, np.inf))
    
    a, b, c = parameters[0], parameters[1], parameters[2]
    
    parameterStd = np.sqrt(np.diag(covs))
    
    print("Model: A * exp(-B * t) + C")
    print("A:", a, "std:", parameterStd[0])
    print("B:", b, "std:", parameterStd[1])
    print("C:", c, "std:", parameterStd[2])
    
    print("\nTime Error bars: +/-", xErr1[0], "usec")
    print("\nCount Error bars: +/-", yErr1, "\n")
    
    modelData = []
    
    for item in position:
        modelData += [exponentialDecay(item, a, b, c)]
    
    plt.figure(4)
    plt.errorbar(position, count, yerr=yErr1, xerr=xErr1, fmt="r.")
    plt.plot(position, modelData, "b-")
    plt.xlabel("Muon Decay Time (usec)")
    plt.ylabel("Count")
    plt.title("Experiment Versus Model")
    plt.legend(("Model data", "Raw data"))
    plt.show()
    
    lifetimeA = (totalCount * 2 * xErr1[0]) / a
    print("Lifetime (A coefficient):", lifetimeA, "usec")
    
    lifetimeB = 1 / abs(b)
    print("Lifetime (B coefficient):", lifetimeB, "usec")
    
    # Expected muon decay time is 2.1969811 +/- 0.0000022 usec from https://en.wikipedia.org/wiki/Muon#Muon_decay
    expectedLifetime = 2.1969811
    
    leastSquaresError = leastSquaresDist(expectedLifetime, lifetimeA, lifetimeB)
    print("Least squares error:", leastSquaresError)
    
    distanceError = distance(expectedLifetime, lifetimeA, lifetimeB)
    print("Distance error:", distanceError)
    
