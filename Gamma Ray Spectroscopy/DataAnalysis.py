#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:01:08 2021

@author: tylerpruitt
"""

# Load the necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

labels = ("Channel", "Energy", "Counts")
UnknownData = pd.read_csv("UnknownData.csv", names=labels, sep=",", skiprows=tuple(range(26)))

Cs137Data = pd.read_csv("Cs-137Data.csv", names=labels, sep=",", skiprows=tuple(range(24)))

unknownDataArray = np.array(UnknownData)
Cs137DataArray = np.array(Cs137Data)

for i in range(1,1025):
    for j in range(3):
        unknownDataArray[i,j] = float(unknownDataArray[i,j])
        Cs137DataArray[i,j] = float(Cs137DataArray[i,j])

plt.figure(1)
plt.semilogy(unknownDataArray[1:,1], unknownDataArray[1:,2])
plt.title("Unknown Sample (20 mins)")
plt.savefig("Unknown.png")
plt.show()

plt.figure(2)
plt.semilogy(Cs137DataArray[1:,1], Cs137DataArray[1:,2])
plt.title("Cs-137 Sample (20 mins)")
plt.savefig("Cs137.png")
plt.show()

unknownRemainingCount = unknownDataArray[1:,2] - Cs137DataArray[1:,2]

plt.figure(3)
plt.semilogy(unknownDataArray[1:,1], unknownRemainingCount)
plt.title("Unknown Sample Without Cs-137")
plt.savefig("Unknown without Cs137.png")
plt.show()

dividedByTwo = unknownDataArray[1:,2] - (Cs137DataArray[1:,2] / 2.0)

plt.figure(4)
plt.semilogy(unknownDataArray[1:,1], dividedByTwo)
plt.title("Unknown Sample Without Half of Cs-137")
plt.savefig("Unknown without half of Cs137.png")
plt.show()

