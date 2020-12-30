# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 17:28:35 2020

@author: Mike
"""

import numpy as np
"""
Importing SNe Ia data from a csv file, below. The info command is run to double check that the correct file has been called.
"""
# DF=pd.read_csv(r'C:/Users/Mike/Desktop/MartinS/SNdata/Riess1998_mag_Data.csv')

"""
The function below is the exact function decribing the FLRW model with the parameters, Hubble constant and matter density. Note this is a two parameter fit and presumes A CURVED UNIVERSE GEOMETRY WITHOUT DARK ENERGY should give very similar results to Vers5 but without integration.
###########
This _portion2 is the subfunction to be subjected to the sinh function
"""  
def _portion2(x, Matter):
    return 2*(np.arctanh(np.sqrt(np.fabs(1-Matter)))- np.arctanh(np.sqrt(np.fabs(1-Matter))/np.sqrt(1+Matter*x)))
"""
This _portion3 is the sinh function applied to portion 2 above.
"""
def _portion3(x, Matter):
    return np.sinh(_portion2(x, Matter))
"""
This _portion1 of the function is a simple calculation
"""
def _portion1(x, Hubble, Matter):
    return ((299792*(1+x))/(Hubble*np.sqrt(np.fabs(1-Matter))))
"""
Putting the complete function together as the cmpltresult. Note this routine only uses the numpy module.
"""
def model(m_B, Hubble, Matter):
    return 5*(np.log10((_portion1(m_B, Hubble, Matter))*(_portion3(m_B, Matter))))+25
"""
TypeError: unsupported operand type(s) for *: 'function' and 'function' BUT AGAIN I DON'T KNOW WHY?' Supposedly something wrong with cmpltresult calculation?
"""