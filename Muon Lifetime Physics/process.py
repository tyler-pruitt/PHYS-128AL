#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 13:23:29 2021

@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt

def CalculateAvgAndStd(sampleData):
    avg = np.average(sampleData)
    std = np.std(sampleData)
    
    return avg, std

isProcess = input("Does this need to be processed (i.e. run process.py) (Yes/No)? ")

yes = ['Yes', 'yes', 'y', 'Y']
no = ['No', 'no', 'n', 'N']

if isProcess in yes:

    # Load data from sift file
    siftFile = input("Enter sift file name: ")
    
    processedFileName = input("Enter new file name for processed data: ")
    
    data = np.loadtxt(siftFile)
    
    # Convert times in nanoseconds to microseconds
    for i in range(len(data)):
        data[i,0] /= 1000
    
    # Input the number of bins from user
    bins = int(input("Enter the number of bins: "))
    
    totalCount = len(data)
    
    # Calculate average and standard deviation for the processed data
    average, std = CalculateAvgAndStd(data[:,0])
    
    print("Average:", average, "usec")
    print("Std:", std, "usec")
    
    # Plot the processed data in a histogram
    figureTitle = input("Enter title for figure of processed data: ")
    figureTitle += " (" + str(bins) + " bins, count: " + str(totalCount) + ")"
    
    plt.figure(1)
    count, position, _ = plt.hist(data[:,0], bins)
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
    plt.title(figureTitle + " Data Points")
    
    plt.figure(3)
    plt.semilogy(position, count, 'r.')
    plt.xlabel("Muon Decay Time (usec)")
    plt.ylabel("Log of Count")
    plt.title(figureTitle + " Data Points")
    
    # Create a file to write the processed data to
    processedFile = open(processedFileName, "w+")
    
    # Write the merged data to the file
    for i in range(len(data)):
        message = str(data[i,0]) + " " + str(data[i,1]) + "\n"
        processedFile.write(message)
    
    processedFile.close()

