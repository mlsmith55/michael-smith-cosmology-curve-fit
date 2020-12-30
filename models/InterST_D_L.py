# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 17:28:35 2020

@author: Mike
"""

import numpy as np
from scipy.integrate import quad
from settings import speed_of_light

"""
The function below is the exact function decribing the FLRW model with two parameters, Hubble constant and matter density. Note this is a 2-parameter FIT OF CURVED SPACETIME WITHOUT DARK ENERGY
"""
def model(x, Hubble, Matter):
    return (_portion1(x, Hubble, Matter))*np.sinh(np.sqrt(np.fabs(1-Matter))*(_vectorizedIntersum(x, Matter)))

"""
This second portion is the function to be integrated
"""
def _portion2(x, Matter):
    return 1/(x*np.sqrt((Matter/x) + np.fabs(1-Matter)))

def _intersum(x, Matter):
    return quad(_portion2, x, 1, args=(Matter))[0]
_vectorizedIntersum = np.vectorize(_intersum, excluded=["Matter"])

"""
This first portion is a simple calculation
"""
def _portion1(x, Hubble, Matter):
    return speed_of_light / (x * Hubble * np.sqrt(np.fabs(1 - Matter)))
