# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 14:22:19 2020

@author: Mike
"""

import numpy as np

"""
This routine analyses D_L_Data for the CURVED UNIVERSE WITHOUT DARK ENERGY.
"""
def model(D_L, Hubble, Matter):
    return (299793/(Hubble*D_L*np.sqrt(np.fabs(1-Matter)))*np.sinh(2*(np.arctanh(np.sqrt(np.fabs(1-Matter)))-np.arctanh(np.sqrt(np.fabs(1-Matter))/np.sqrt((Matter/D_L)+np.fabs(1-Matter))))))
