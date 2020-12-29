# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 14:22:19 2020

@author: Mike

Is there a simple way that allows me to provide a weighting function which produces results?
"""

#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import curve_fit
import numpy as np
#from numpy import sqrt, sinh, arctanh, fabs 
#import math

DF=pd.read_csv(r'C:\Users\Mike\Desktop\SNdata\Riess1998_mag_Data.csv')
#Now check to make certain the proper file is being read
DF.info()

x = DF['Z']
y = DF['m_B']
w = DF['Error_m_B']
"""
The following function decribes the FLRW model applied to the mag dataframe with curved spacetime and without dark energy. So the 1-Matter term describes the value for spacetime not dark energy.
"""
def func(x, Hubble, Matter):
    return 5*np.log10(299793/(Hubble*x*np.sqrt(np.fabs(1-Matter))))*np.sinh(2*(np.arctanh(np.sqrt(np.fabs(1-Matter)))-np.arctanh(np.sqrt(np.fabs(1-Matter))/np.sqrt((Matter/x)+np.fabs(1-Matter)))))+25

popt = scipy.optimize.curve_fit(func, x, y,sigma = w)

"""
ValueError: operands could not be broadcast together with shapes (2,) (38,)    


print(popt[0])
print(popt[1])

plt.plot(x, func(x, *popt), 'g--',
         label='fit: Hubble=%5.3f, Matter=%5.3f, space=%5.3f')

plt.xlabel('redshift')
plt.ylabel('mag')
plt.legend()
plt.show()
"""

