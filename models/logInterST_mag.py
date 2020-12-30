# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 17:28:35 2020

@author: Mike
"""

#import numpy as np
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy
#import scipy.integrate as integrate
from scipy.integrate import quad
"""
Importing SNe Ia data from a csv file, below. The info command is run to double check that the correct file has been called.
"""
DF=pd.read_csv(r'C:/Users/Mike/Desktop/MartinS/SNdata/Riess1998_mag_Data.csv')
#Now check to make certain the proper file is being read
DF.info()

x = DF['Z']
y = DF['m_B']
w = DF['Error_m_B']
"""
The function below is the exact function decribing the FLRW model with the parameters, Hubble constant and matter density. Note this presumes A CURVED UNIVERSE GEOMETRY WITHOUT DARK ENERGY
###########
This portion2 is the function to be integrated
"""  
def portion2(x, Matter):
    return 1/(math.sqrt(((1+x)**2)*(1+Matter*x)))
                     
def intersum(x):
    return quad(lambda x: portion2, 0, x)
"""
This portion3 is the sinh(sqrt(1-Matter)function of the intersum above). Use of math.sinh seems OK with Python 3.
"""
def portion3(x, Matter):
    return math.sinh(math.sqrt(math.fabs(1-Matter))*intersum)
"""
This first portion of the function is a simple calculation
"""
def portion1(x, Hubble, Matter):
    return ((299792*(1+x))/(Hubble*math.sqrt(math.fabs(1-Matter))))
"""
Putting the complete function together as the cmpltresult. Note this is the only use of the numpy module, supposedly math.log10 works as well.
"""
cmpltresult=5*(np.log10((portion1)*(portion3)))+25
"""
TypeError: unsupported operand type(s) for *: 'function' and 'function' BUT I DON'T KNOW WHY?' Supposedly something wrong with cmpltresult calculation?
"""