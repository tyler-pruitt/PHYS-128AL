#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:04:46 2021

@author: tylerpruitt
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from equations import chargeOfDrop
from equations import chargeError

class drop(object):
    def __init__(self, number, eCharge, cCharge, riseTimes, fallTimes, statedAvgRiseVelocity, statedAvgFallVelocity, riseVelocities, fallVelocities, riseTrials, fallTrials):
        self.num = int(number)
        
        self.chargeInE = eCharge
        self.chargeInC = cCharge
        
        self.riseTime = riseTimes
        self.fallTime = fallTimes
        
        self.averageRiseTime = np.average(riseTimes)
        self.averageFallTime = np.average(fallTimes)
        
        self.calcAvgRiseSpeed = statedAvgRiseVelocity
        self.calcAvgFallSpeed = statedAvgFallVelocity
        
        self.riseSpeed = riseVelocities
        self.fallSpeed = fallVelocities
        
        self.averageRiseSpeed = np.average(riseVelocities)
        self.averageFallSpeed = np.average(fallVelocities)
        
        self.riseTimeCount = riseTrials
        self.fallTimeCount = fallTrials
        
        self.riseTimeStd = np.std(riseTimes)
        self.fallTimeStd = np.std(fallTimes)
        
        self.dtRise = np.sqrt( (self.riseTimeStd / np.sqrt(self.riseTimeCount))**2 + (0.10 * self.averageRiseTime)**2 )
        self.dtFall = np.sqrt( (self.fallTimeStd / np.sqrt(self.riseTimeCount))**2 + (0.10 * self.averageFallTime)**2 )
        
        self.dvRise = self.averageRiseSpeed * (self.dtRise / self.averageRiseTime)
        self.dvFall = self.averageFallSpeed * (self.dtFall / self.averageFallTime)
        
        self.dq = chargeError(self.dvFall, self.dvRise, self.averageFallSpeed, self.averageRiseSpeed)


csv = pd.read_csv('Electron Properties Data - Sheet1.csv')

data = np.array(csv)

# Filter out the nan in the data
data = np.nan_to_num(data)

drops = []
lastDropNumber = 0

for i in range(len(data)):
    dropNumber = data[i,0]
    
    # New drop
    if dropNumber != lastDropNumber or i == len(data) - 1:
        
        if lastDropNumber != 0:
            drops += [drop(lastDropNumber, electronCharge, coulombCharge, riseTime, fallTime, avgRiseVelocity, avgFallVelocity, riseVelocity, fallVelocity, len(riseTime), len(fallTime))]
        
        lastDropNumber = dropNumber
        
        riseTime = []
        fallTime = []
        riseVelocity = []
        fallVelocity = []
        
        avgRiseVelocity = data[i,5]
        avgFallVelocity = data[i,6]
        
        coulombCharge = data[i,7]
        electronCharge = data[i,8]
    
    # Same drop
    if data[i,1] != 0:
        riseTime += [data[i,1]]
    if data[i,2] != 0:
        fallTime += [data[i,2]]
    
    if data[i,3] != 0:
        riseVelocity += [data[i,3]]
    if data[i,4] != 0:
        fallVelocity += [data[i,4]]

count = 1
for eachDrop in drops:
    if (eachDrop.calcAvgRiseSpeed >= 1.02 * eachDrop.averageRiseSpeed) or (eachDrop.calcAvgRiseSpeed <= 0.98 * eachDrop.averageRiseSpeed):
        print("Drop:", count)
        print(eachDrop.calcAvgRiseSpeed, eachDrop.averageRiseSpeed)
        print("\n")
    if (eachDrop.calcAvgFallSpeed >= 1.02 * eachDrop.averageFallSpeed) or (eachDrop.calcAvgFallSpeed <= 0.98 * eachDrop.averageFallSpeed):
        print("Drop:", count)
        print(eachDrop.calcAvgFallSpeed, eachDrop.averageFallSpeed)
        print("\n")
    count += 1

newDrops = []

minimumCount = int(input("Enter minimum number of rise trials and of fall trials: "))

for i in range(len(drops)):
    if drops[i].riseTimeCount >= minimumCount and drops[i].fallTimeCount >= minimumCount:
        newDrops += [drops[i]]

xAxis, yAxis, yError = [], [], []
e = 1.60217662 * 10**(-19)

for i in range(len(newDrops)):
    xAxis += [newDrops[i].num]
    yAxis += [newDrops[i].chargeInE]
    yError += [newDrops[i].dq / e]

plt.figure(1)
plt.plot(xAxis, yAxis, "r.")
plt.xlabel("Drop Number")
plt.ylabel("Charge (in e)")
plt.title("Quantization of Charge")
plt.show()

plt.figure(2)
plt.errorbar(xAxis, yAxis, yerr=yError, fmt="r.")
plt.xlabel("Drop Number")
plt.ylabel("Charge (in e)")
plt.title("Quantization of Charge")
plt.show()

lines = []
for i in range(1, 7):
    lines += [len(xAxis) * [i]]

plt.figure(3)
plt.errorbar(xAxis, yAxis, yerr=yError, fmt="r.")

for i in range(6):
    plt.plot(xAxis, lines[i], "b-")

plt.xlabel("Drop Number")
plt.ylabel("Charge (in e)")
plt.title("Quantization of Charge")
plt.show()


