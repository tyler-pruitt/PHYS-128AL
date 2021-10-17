#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:29:29 2021

@author: tylerpruitt
"""


def massOfElectron(Egamma, Emax):
    energy = (2 * Egamma**2)/Emax - 2*Egamma
    
    mec2 = 511
    
    percentError = (energy - mec2) * 100 / mec2
    
    print("Energy:", energy, "keV")
    print("Percent error:", percentError, "%")
    
    return energy
