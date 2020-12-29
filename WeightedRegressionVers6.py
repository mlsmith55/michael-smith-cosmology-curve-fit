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
"""
Z is the redshift astronomers wrongly use as the recession velocity.
m_B is the "distance magnitude" from signals using a blue filter
Error_m_B is the standard deviation about m_B
"""
x = DF['Z']
y = DF['m_B']
w = DF['Error_m_B']
"""
The function below is the exact function decribing the FLRW model with two paramters, Hubble constant and matter density. Note this is a 2-parameter FIT OF FLAT SPACETIME WITH DARK ENERGY
###########
This second portion is the function to be integrated which is mag version of equation E5 of DOI: 10.5772/intechopen.91266. The next definition is the function needed for integration
"""  
def portion2(x, Matter):
    return 1/(x*math.sqrt((Matter/x) + math.fabs(1-Matter)*x**2))
"""
This definition is the integration process, note the integration is from x to 1 and not 1 to x as per the equation E5.
"""                    
def intersum(x):
    return quad(lambda x: portion2, x, 1)
"""
This is a simple calculation of the pre-integral portion of E5
"""
def portion1(x, Hubble):
    return (299792/(x*Hubble))
"""
putting the complete function together as the cmpltresult
"""
def cmpltresult(x, Hubble, Matter):
    return (5*np.log10(portion1)*(intersum)+25)          
"""
I suppose that cmpltresult can be used with curve_fit ?
"""