#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 13:45:20 2021

@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt

from methods import CalculateAvgAndStd


# Filter the data if needed
isFilter = input("Does this data need to be filtered (i.e. run filter.py) (Yes/No)? ")

yes = ['Yes', 'yes', 'y', 'Y']
no = ['No', 'no', 'n', 'N']

if isFilter in yes:
    # Load data from data file
    dataFile = input("Enter data file name: ")
    data = np.loadtxt(dataFile)
    
    filterFileName = input("Enter new file name for filtered data: ")
    
    maxThreshold = float(input("Enter max threshold (in usec) for data: "))
    minThreshold = float(input("Enter min threshold (in usec) for data: "))
    
    # Input the number of bins from user
    bins = int(input("Enter the number of bins: "))
    
    totalCount = len(data)
    
    sortedData = []
    
    removedData = []

    for i in range(len(data[:,0])):
        if (data[i,0] <= maxThreshold) and (data[i,0] >= minThreshold):
            sortedData += [data[i]]
        else:
            removedData += [data[i]]
    
    sortedData = np.array(sortedData)
    removedData = np.array(removedData)
    
    newCount = totalCount - len(removedData)
    
    print("Filtering out", len(removedData), "data points at time (in usec):")
    
    for i in range(len(removedData)):
        if i == 0:
            message = "[" + str(removedData[i,0]) + ", "
            print(message, end='')
        elif i == len(removedData) - 1:
            message = str(removedData[i,0]) + "]"
            print(message)
        else:
            message = str(removedData[i,0]) + ", "
            print(message, end='')
    
    
    filterFile = open(filterFileName, "w+")
    
    # Write the filtered data to the file
    for i in range(len(sortedData)):
        message = str(sortedData[i,0]) + " " + str(sortedData[i,1]) + "\n"
        filterFile.write(message)
    
    filterFile.close()
    
    average, std = CalculateAvgAndStd(sortedData[:,0])

    print("Filtered Average:", average, "usec")
    print("Filtered Std:", std, "usec")
    
    # Plot the filtered data in a histogram
    figureTitle = input("Enter title for figure of filtered data: ")
    figureTitle += " (" + str(bins) + " bins, count: " + str(newCount) + ")"
    
    plt.figure(1)
    count, position, _ = plt.hist(sortedData[:,0], bins)
    plt.xlabel("Muon Decay Time (usec)")
    plt.ylabel("Count")
    plt.title(figureTitle)
    plt.show()
    
    position = position[:-1]
    
    zeroIndex = []
    for i in range(len(position)):
        if count[i] == 0.:
            zeroIndex += [i]
    
    count, position = np.delete(count, zeroIndex), np.delete(position, zeroIndex)

    plt.figure(2)
    plt.plot(position, count, 'r.')
    plt.xlabel("Muon Decay Time (usec)")
    plt.ylabel("Count")
    plt.title(figureTitle)
    plt.show()
    
    plt.figure(3)
    plt.semilogy(position, count, 'r.')
    plt.xlabel("Muon Decay Time (usec)")
    plt.ylabel("Log of Count")
    plt.title(figureTitle)
    plt.show()

