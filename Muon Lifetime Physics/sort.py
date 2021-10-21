#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 13:23:29 2021

@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt

fileName = input("Enter sift file name: ")

name = input("Enter title for data: ")

data = np.loadtxt(fileName)

# Convert times in nanoseconds to microseconds

for i in range(len(data)):
    data[i,0] /= 1000

bins = int(input("Enter the number of bins: "))

totalCount = len(data)
title = name + " (" + str(bins) + " bins, count: " + str(totalCount) + ")"

plt.figure(1)
count, position, _ = plt.hist(data[:,0], bins)
plt.xlabel("Muon Decay Time (usec)")
plt.ylabel("Count")
plt.title(title)
plt.show()

average = np.average(data[:,0])
std = np.std(data[:,0])

print("Average:", average, "usec")
print("Std:", std, "usec")
