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
    
    # Think about excluding the farthest three points in the dataset because
    # they are not near the line in the linear semilogy plot.
    
    # Filter the data is needed
    isFilter = input("Should this data be filtered (Yes/No): ")
    
    yes = ['Yes', 'yes', 'y', 'Y']
    no = ['No', 'no', 'n', 'N']
    
    if isFilter in yes:
        filterFileName = input("Enter new file name for filtered data: ")
        
        maxThreshold = float(input("Enter max threshold (in usec) for data: "))
        minThreshold = float(input("Enter min threshold (in usec) for data: "))
        
        sortedData = []
    
        for i in range(len(data[:,0])):
            if (data[i,0] <= maxThreshold) and (data[i,0] >= minThreshold):
                sortedData += [data[i]]
        
        sortedData = np.array(sortedData)
        
        filterFile = open(filterFileName, "w+")
        
        # Write the filtered data to the file
        for i in range(len(sortedData)):
            message = str(sortedData[i,0]) + " " + str(sortedData[i,1]) + "\n"
            filterFile.write(message)
        
        filterFile.close()
        
        filterAvg, filterStd = CalculateAvgAndStd(sortedData[:,0])
    
        print("Filtered Average:", filterAvg, "usec")
        print("Filtered Std:", filterStd, "usec")
        
        # Plot the filtered data in a histogram
        filterFigureTitle = input("Enter title for figure of filtered data: ")
        filterFigureTitle += " (" + str(bins) + " bins, count: " + str(totalCount) + ")"
        
        plt.figure(4)
        filterCount, filterPosition, _ = plt.hist(sortedData[:,0], bins)
        plt.xlabel("Muon Decay Time (usec)")
        plt.ylabel("Count")
        plt.title(filterFigureTitle)
        plt.show()
        
        filterPosition = filterPosition[:-1]
    
        plt.figure(5)
        plt.plot(filterPosition, filterCount, 'r.')
        plt.xlabel("Muon Decay Time (usec)")
        plt.ylabel("Count")
        plt.title(filterFigureTitle + " Data Points")
        
        plt.figure(6)
        plt.semilogy(filterPosition, filterCount, 'r.')
        plt.xlabel("Muon Decay Time (usec)")
        plt.ylabel("Log of Count")
        plt.title(filterFigureTitle + " Data Points")
    
