# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 17:28:35 2020

@author: Mike
"""

import numpy as np
import math
from scipy.integrate import quad
from settings import speed_of_light

"""
The function below is the exact function decribing the FLRW model with the parameters, Hubble constant and matter density. Note this presumes A CURVED UNIVERSE GEOMETRY WITHOUT DARK ENERGY
"""
def model(x, Hubble, Matter):
    return 5*(np.log10((_portion1(x, Hubble, Matter))*(_portion3(x, Matter))))+25

"""
This _portion2 is the function to be integrated
"""  
def _portion2(x, Matter):
    return 1/(np.sqrt(((1+x)**2)*(1+Matter*x)))

def _intersum(x, Matter):
    return quad(_portion2, 0, x, args=(Matter))[0]
_vectorizedIntersum = np.vectorize(_intersum, excluded=["Matter"])


"""
This _portion3 is the sinh(sqrt(1-Matter)function of the _intersum above).
"""
def _portion3(x, Matter):
    return np.sinh(np.sqrt(np.fabs(1-Matter))*_vectorizedIntersum(x, Matter))

"""
This first portion of the function is a simple calculation
"""
def _portion1(x, Hubble, Matter):
    return speed_of_light*(1+x)/(Hubble*np.sqrt(np.fabs(1-Matter)))
