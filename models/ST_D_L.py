# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 14:22:19 2020

@author: Mike
"""

import numpy as np
from settings import speed_of_light

"""
This routine analyses D_L_Data for the CURVED UNIVERSE WITHOUT DARK ENERGY.
"""
def ST_D_L(D_L, Hubble, Matter):
    return speed_of_light/(Hubble*D_L*np.sqrt(np.fabs(1-Matter)))*np.sinh(2*(np.arctanh(np.sqrt(np.fabs(1-Matter)))-np.arctanh(np.sqrt(np.fabs(1-Matter))/np.sqrt((Matter/D_L)+np.fabs(1-Matter)))))
