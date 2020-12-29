# -*- coding: utf-8 -*-
#%%
"""
Created on Mon Dec 28 17:28:35 2020

@author: Mike
"""

import pandas as pd
import numpy as np
import scipy.optimize as optimize
import math
import matplotlib.pyplot as plt
from scipy.integrate import quad

"""
Importing SNe Ia data from a csv file, below. The info command is run to double check that the correct file has been called.
"""
DF = pd.read_csv('data/Riess1998_mag_Data.csv')
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
def intersum(x, Matter):
    return quad(portion2, x, 1, args=(Matter))[0]
vectorizedIntersum = np.vectorize(intersum, excluded=["Matter"])

"""
This is a simple calculation of the pre-integral portion of E5
"""
def portion1(x, Hubble):
    return (299792/(x*Hubble))

"""
putting the complete function together as the func
"""
def func(x, Hubble, Matter):
    return (5*np.log10(portion1(x, Hubble))*(vectorizedIntersum(x, Matter))+25)

"""
I suppose that func can be used with curve_fit ?
"""

popt, pcov = optimize.curve_fit(func, x, y, sigma=w, p0=[70, 0.5], bounds=([60,0.01],[80,0.99]))
fitLabel = 'fit: Hubble=%5.3f, Matter=%5.3f' % (popt[0], popt[1])

plt.figure()
plt.errorbar(x, y, w, fmt='.', label='data', capsize=5)
xf = np.linspace(x.min(), x.max(), num=50)
plt.plot(xf, func(xf, *popt), 'g--',
         label=fitLabel)

plt.xlabel('redshift')
plt.ylabel('mag')
plt.legend()
plt.show()

# %%
