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
def InterDE_D_L(D_L, Hubble, Matter):
    return _portion1(D_L, Hubble) * _vectorizedIntersum(D_L, Matter)

"""
_portion1 defines the pre-integral
"""
def _portion1(D_L, Hubble):
    return speed_of_light/(Hubble*D_L)

"""
_portion2 is the function to be integrated
"""
def _portion2(D_L,Matter):
    return 1/(D_L*np.sqrt((Matter/D_L)+(1-Matter)*D_L**2))

"""
The _intersum is the integration routine 
"""
def _intersum(D_L, Matter):
    return quad(_portion2, D_L, args=(Matter))[0], 1
_vectorizedIntersum = np.vectorize(_intersum, excluded=["Matter"])
