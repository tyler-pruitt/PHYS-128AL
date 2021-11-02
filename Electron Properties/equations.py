#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:06:20 2021

@author: tylerpruitt
"""

import numpy as np

def chargeOfDrop(fallVelocity, riseVelocity, a=0):
    V = 500
    rho = 886
    n = 1.8285 * 10**(-5)
    p = 101325
    b = 8.2 * 10**(-3)
    g = 9.80665
    d = 0.00914
    
    if a == 0:
        q = (4 * np.pi / 3) * (np.sqrt((b / (2*p))**2 + ((9 * n * fallVelocity) / (2 * rho * g)) ) - (b / (2 * p)) )**3 * ((rho * g * d * (fallVelocity + riseVelocity)) / (V * fallVelocity))
    else:
        q = (4 * np.pi / 3) * a**3 * ((rho * g * d * (fallVelocity + riseVelocity)) / (V * fallVelocity))
    
    return q

def radiusOfDrop(fallVelocity):
    rho = 886
    n = 1.8285 * 10**(-5)
    p = 101325
    b = 8.2 * 10**(-3)
    g = 9.80665
    
    a = np.sqrt((b / (2*p))**2 + ((9 * n * fallVelocity) / (2 * rho * g)) ) - (b / (2 * p))
    
    return a

def chargeError(dVf, dVr, Vf, Vr, dV, dn, dd):
    V = 500
    rho = 886
    n = 1.8285 * 10**(-5)
    g = 9.80665
    d = 0.00914
    
    factor = (4 * np.pi * g * rho / 3)
    
    dq = 1 * np.sqrt( ((dVf + dVr) / (Vf + Vr))**2 + (dd / d)**2 + (dV / V)**2 + (745 / 16) * (dVf / Vf)**2 + (729 / 16) * (dn / n)**2 )
    
    return dq

response = input("To end enter 'end', else press enter: ")

while response != "end":
    Vrise = float(input("Enter Vrise: "))
    Vfall = float(input("Enter Vfall: "))
    
    q = chargeOfDrop(Vfall, Vrise)
    e = 1.60217662 * 10**(-19)
    
    print("Charge:", q, "C")
    print("Charge:", q/e, "e")
    
    response = input("To end enter 'end', else press enter: ")

