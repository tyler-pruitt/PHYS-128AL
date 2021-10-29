#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:16:10 2021

@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt

from methods import leastSquaresDist
from methods import distance


lines = []
with open("lifetimes.txt") as lifetimesFile:
    lines = lifetimesFile.readlines()

lineCount = int(len(lines) / 2)

# Reorganize input data
for i in range(len(lines)):
    lines[i] = lines[i][:-1]
    lines[i] = lines[i].split(",")
    lines[i][0] = int(lines[i][0])
    lines[i][2] = float(lines[i][2])

bins, methods, lifetimes = [], [], []

for i in range(len(lines)):
    bins += [lines[i][0]]
    methods += [lines[i][1]]
    lifetimes += [lines[i][2]]

optimalBin = bins[0]
minError = 1000
error = []

# Expected muon decay time is 2.1969811 +/- 0.0000022 usec from https://en.wikipedia.org/wiki/Muon#Muon_decay
expectedLifetime = 2.1969811

method = input("Is the error function least squares ('leastsquares') or distance ('distance')? ")

# For each bin calculate the least squares distance and find minError, optimalBin
for i in range(0, len(lifetimes), 2):
    lifetimeA = lifetimes[i]
    lifetimeB = lifetimes[i+1]
    
    if method == 'leastsquares':
        binError = leastSquaresDist(expectedLifetime, lifetimeA, lifetimeB)
    elif method == 'distance':
        binError = distance(expectedLifetime, lifetimeA, lifetimeB)
    else:
        raise ValueError("your answer must be 'leastsquares' or 'distance'")
    
    error += [binError]
    
    if minError > binError:
        minError = binError
        optimalBin = bins[i]

print("Optimal bin:", optimalBin)
print("Minimum Error:", minError)

plt.figure(1)
x = list(range(bins[0], bins[-1]+1))
plt.plot(x, error, "r.")
plt.xlabel("Bin Number")
plt.ylabel("Error")
plt.title("Optimal Bin Choice (" + method + "): " + str(optimalBin))
plt.show()

