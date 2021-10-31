#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 22:26:57 2021

@author: tylerpruitt
"""

import numpy as np

def CalculateAvgAndStd(sampleData):
    avg = np.average(sampleData)
    std = np.std(sampleData)
    
    return avg, std

def exponentialDecay(t, a, b, c):
    return a * np.exp(-b * t) + c

def errorbar(times, counts):
    
    halfBinSize = (times[1] - times[0]) / 2.0
    
    timeError, countError = [], []
    
    for i in range(len(counts)):
        if counts[i] == 0:
            timeError += [0]
            countError += [0]
        else:
            timeError += [halfBinSize]
            countError += [1 / np.sqrt(counts[i])]
    
    return timeError, countError

def leastSquaresDist(expectedLifetime, lifetimeA, lifetimeB):
    return np.sqrt(abs(lifetimeA - expectedLifetime)**2 + abs(lifetimeB - expectedLifetime)**2)

def distance(expectedLifetime, lifetimeA, lifetimeB):
    return abs(lifetimeA - expectedLifetime) + abs(lifetimeB - expectedLifetime)

