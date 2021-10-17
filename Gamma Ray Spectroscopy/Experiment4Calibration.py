#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 16:55:17 2021

@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

line = np.linspace(0,500,1000)
m = 2.194
b = -1*48.461
y=m*line + b
channel = [324,231,98,322,322,96,402,307,96,401,308,103,174,94,55,174,94,55]
exp_energy = [661.6,477.3,184.3,661.6,477.3,184.3,834.8,639.2,195.6,834.8,639.2,195.6,356,207.3,148.7,356,207.3,148.7]

plt.figure(1)
plt.plot(line, y)
plt.scatter(channel, exp_energy)
plt.xlabel("Channel Number")
plt.ylabel("Energy (keV)")
plt.title("Experiement 4")
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
plt.xlabel("Channel Number")
plt.ylabel("Energy (keV)")
plt.title("Experiement 4")
plt.legend(("2-Point Fit", "3-Point Fit"))
plt.show()
