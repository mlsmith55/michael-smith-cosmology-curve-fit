# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 14:22:19 2020

@author: Mike
"""

import numpy as np
from scipy.integrate import quad
from settings import speed_of_light

"""
The function below is the exact function decribing the FLRW model with the parameters, Hubble constant and matter density. Note this is a two parameter fit and presumes A FLAT UNIVERSE GEOMETRY WITH DARK ENERGY.
"""
def InterDE_D_L(x, Hubble, Matter):
    return _portion1(x, Hubble) * _vectorizedIntersum(x, Matter)

"""
_portion1 defines the pre-integral
"""
def _portion1(x, Hubble):
    return speed_of_light/(Hubble*x)
"""
_portion2 is the function to be integrated
"""
def _portion2(x,Matter):
    return 1/(x*np.sqrt((Matter/x)+(1-Matter)*x**2))

"""
The _intersum is the integration routine 
"""
def _intersum(x, Matter):
    return quad(_portion2, x, 1, args=(Matter))[0]
_vectorizedIntersum = np.vectorize(_intersum, excluded=["Matter"])
