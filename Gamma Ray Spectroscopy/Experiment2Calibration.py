#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 16:38:59 2021

@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

line = np.linspace(0,700,1000)
m = 2.213
b = -1*48.9
y=m*line + b
channel = [330,57,180,152,225,57,150,177,42,60,549,616,402,41,321,522,320,520]
exp_energy = [661.6,81,356,276.4,383.9,81,276.4,356.0,122.1,136.5,1173.2,1332.5,834.8,88,661.6,1115.5,661.6,1115.5]

plt.figure(1)
plt.plot(line, y)
plt.scatter(channel, exp_energy)
plt.title("Experiement 2: 22Na 2-Point Fit")
plt.show()

def quadratic(x, a, b, c):
    return a*(x**2) + b*x + c

parameters, covs = curve_fit(quadratic, channel, exp_energy)

quadratic_energy = []

for i in range(len(channel)):
    quadratic_energy += [quadratic(channel[i], parameters[0], parameters[1], parameters[2])]

plt.figure(2)
plt.plot(line, y)
plt.scatter(channel, exp_energy)
plt.plot(channel, quadratic_energy)
plt.title("Experiement 2: 22Na 3-Point Fit")
plt.legend(("2-Point Fit", "3-Point Fit"))
plt.show()
