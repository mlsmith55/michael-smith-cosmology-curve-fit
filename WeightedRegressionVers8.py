# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 17:28:35 2020

@author: Mike
"""

#import numpy as np
import pandas as pd
import numpy as np
#import math
import matplotlib.pyplot as plt
#import scipy
#import scipy.integrate as integrate
#from scipy.integrate import quad
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
The function below is the exact function decribing the FLRW model with the parameters, Hubble constant and matter density. Note this is a two parameter fit and presumes A CURVED UNIVERSE GEOMETRY WITHOUT DARK ENERGY should give very similar results to Vers5 but without integration.
###########
This portion2 is the subfunction to be subjected to the sinh function
"""  
def portion2(x, Matter):
    return 2*(np.arctanh(np.sqrt(np.fabs(1-Matter)))- np.arctanh(np.sqrt(np.fabs(1-Matter))/np.sqrt(1+Matter*x)))
"""
This portion3 is the sinh function applied to portion 2 above.
"""
def portion3(x, Matter):
    return np.sinh(portion2)
"""
This portion1 of the function is a simple calculation
"""
def portion1(x, Hubble, Matter):
    return ((299792*(1+x))/(Hubble*np.sqrt(np.fabs(1-Matter))))
"""
Putting the complete function together as the cmpltresult. Note this routine only uses the numpy module.
"""
cmpltresult=5*(np.log10((portion1)*(portion3)))+25
"""
TypeError: unsupported operand type(s) for *: 'function' and 'function' BUT AGAIN I DON'T KNOW WHY?' Supposedly something wrong with cmpltresult calculation?
"""