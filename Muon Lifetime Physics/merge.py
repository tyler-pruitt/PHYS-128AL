#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:31:13 2021

@author: tylerpruitt
"""

import numpy as np

isMerge = input("Does this need to be merged with another file (i.e. run merge.py) (Yes/No)? ")

yes = ['Yes', 'yes', 'y', 'Y']
no = ['No', 'no', 'n', 'N']

if isMerge in yes:

    fileName1 = input("Enter first data file name: ")
    fileName2 = input("Enter second data file name: ")
    
    name = input("Enter file name for merged data: ")
    
    data1, data2 = np.loadtxt(fileName1), np.loadtxt(fileName2)
    
    mergedData = []
    
    for i in range(len(data1)):
        mergedData += [data1[i]]
    
    for j in range(len(data2)):
        mergedData += [data2[j]]
    
    mergedData = np.array(mergedData)
    
    # Create a file to write the merged data to
    mergedFile = open(name, "w+")
    
    # Write the merged data to the file
    for i in range(len(mergedData)):
        message = str(mergedData[i,0]) + " " + str(mergedData[i,1]) + "\n"
        mergedFile.write(message)
    
    mergedFile.close()
