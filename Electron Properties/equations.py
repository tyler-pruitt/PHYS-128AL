#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:06:20 2021

@author: tylerpruitt
"""

import numpy as np

def chargeOfDrop(fallVelocity, riseVelocity):
    V = 500
    rho = 886
    n = 1.831 * 10**(-5)
    p = 101325
    b = 8.2 * 10**(-3)
    g = 9.80665
    d = 0.00914
    
    q = (4 * np.pi / 3) * (np.sqrt((b / (2*p))**2 + ((9 * n * fallVelocity) / (2 * rho * g)) ) - (b / (2 * p)) )**3 * ((rho * g * d * (fallVelocity + riseVelocity)) / (V * fallVelocity))
    
    e = 1.60217662 * 10**(-19)
    
    return q, q / e

def chargeError(dVf, dVr, Vf, Vr):
    V = 500
    dV = 10
    dn = 0.003 * 10**(-5)
    rho = 886
    n = 1.831 * 10**(-5)
    g = 9.80665
    d = 0.00914
    b = 8.2 * 10**(-3)
    p = 101325
    
    A = (4 * np.pi * g * rho / 3)
    B = (b / (2 * p))**2 + 9 * n * Vf / (2 * rho * g)
    C = b / (2 * p)
    D = d * (Vf + Vr) / (V * Vf)
    F = B**(1/2) - C
    q = A * (F)**3 * D
    dB = B * ((dn/n)**2 + (dVf/Vf)**2)**2
    
    dD = D * (((dVf + dVr) / (Vf + Vr))**2 + (dV / V)**2 +(dVf / Vf)**2)**(1/2)
    
    dq = q * (9 * (dB / (2 * (B - C * B**(1/2))))**2 + (dD / D)**2)**(1/2)
    
    return dq

