#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:12:34 2021

@author: tylerpruitt
"""

# Create .txt file for list of bins to iterate through
start = int(input("Enter min of bin range: "))
end = int(input("Enter max of bin range: "))

bins = list(range(start, end+1))

dataFileName = input("Enter data file name: ")

figureTitle = input("Enter figure title: ")

binsFile = open("bins.txt", "w+")

for i in range(len(bins)):
    binsFile.write(dataFileName + "," + str(bins[i]) + "," + figureTitle + "\n")

binsFile.close()