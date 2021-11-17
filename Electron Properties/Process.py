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

class Drop(object):
    def __init__(self, id, eCharge, cCharge, riseTimes, fallTimes, statedAvgRiseVelocity, statedAvgFallVelocity, riseVelocities, fallVelocities, riseTrials, fallTrials):
        self.id = int(id)
        
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
        
        e = 1.60217662 * 10**(-19)
        
        self.dq = chargeError(self.dvFall, self.dvRise, self.averageFallSpeed, self.averageRiseSpeed)
        self.dqInE = self.dq / e
        
    def __repr__(self):
        rep = 'Drop(ID: ' + str(self.id) + ', Charge: ' + str(self.chargeInE) + ' e)'
        return rep


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
            drops += [Drop(lastDropNumber, electronCharge, coulombCharge, riseTime, fallTime, avgRiseVelocity, avgFallVelocity, riseVelocity, fallVelocity, len(riseTime), len(fallTime))]
        
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

print('Drops:')
print(drops, end='\n\n')

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

sortedDrops = []

minimumCount = int(input("Enter minimum number of rise trials and of fall trials: "))

for i in range(len(drops)):
    if drops[i].riseTimeCount >= minimumCount and drops[i].fallTimeCount >= minimumCount:
        if minimumCount != 0:
            if drops[i].chargeInE <= 4:
                sortedDrops += [drops[i]]
        else:
            sortedDrops += [drops[i]]

print('Sorted Drops:')
print(sortedDrops, end='\n\n')

a, b, c, d = [], [], [], []
for i in range(len(sortedDrops)):
    if sortedDrops[i].chargeInE <= 1.9:
        a += [sortedDrops[i].chargeInC]
        b += [sortedDrops[i].chargeInE]
        c += [sortedDrops[i].dq]
        d += [sortedDrops[i].dqInE]

averageChargeInC, averageChargeInE, averagedqInC, averagedqInE = np.average(a), np.average(b), np.average(c), np.average(d)

print('Average charge of electron:', averageChargeInC, 'C,', averageChargeInE, 'e')
print('Average dq of electron:', averagedqInC, 'C,', averagedqInE, 'e')

xAxis, yAxis, yError = [], [], []

for i in range(len(sortedDrops)):
    xAxis += [sortedDrops[i].id]
    yAxis += [sortedDrops[i].chargeInE]
    yError += [sortedDrops[i].dqInE]

plt.figure(1)
plt.plot(xAxis, yAxis, "r.")
plt.xlabel("Drop Number")
plt.ylabel("Charge (in e)")
#plt.title("Quantization of Charge")
plt.show()

plt.figure(2)
plt.errorbar(xAxis, yAxis, yerr=yError, fmt="r.")
plt.xlabel("Drop Number")
plt.ylabel("Charge (in e)")
#plt.title("Quantization of Charge")
plt.show()

maxCharge = 0

for i in range(len(sortedDrops)):
    if sortedDrops[i].chargeInE >= maxCharge:
        maxCharge = sortedDrops[i].chargeInE

numberOfLines = int(maxCharge) + 1

lines = []
for i in range(1, numberOfLines+1):
    lines += [len(xAxis) * [i]]

plt.figure(3)
plt.errorbar(xAxis, yAxis, yerr=yError, fmt="r.")

for i in range(len(lines)):
    plt.plot(xAxis, lines[i], "b-")

plt.xlabel("Drop Number")
plt.ylabel("Charge (in e)")
#plt.title("Quantization of Charge")
plt.show()

charge, error = [], []

for i in range(len(sortedDrops)):
    charge += [sortedDrops[i].chargeInE]
    error += [sortedDrops[i].dqInE]

# Sort 'charge' and 'error' for ascending charge
# Use selection sort
for i in range(len(charge)):
    minIndex = i
    
    for j in range(i+1, len(charge)):
        if charge[minIndex] > charge[j]:
            minIndex = j
    
    charge[i], charge[minIndex] = charge[minIndex], charge[i]
    error[i], error[minIndex] = error[minIndex], error[i]


plt.figure(4)
plt.plot(charge, error, "r.")
plt.xlabel("Charge (in e)")
plt.ylabel("Error in Charge (in e)")
#plt.title("Trend in Error and Charge")
plt.show()

