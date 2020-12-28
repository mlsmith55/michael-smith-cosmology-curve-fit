# -*- coding: utf-8 -*-
#%%
"""
Created on Mon Dec 21 14:22:19 2020

@author: Mike

Is there a simple way that allows me to provide a weighting function which produces results?
"""

#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np
#from np import sqrt, sinh, arctanh, fabs 

DF=pd.read_csv('Riess1998_DL_Data.csv')
#Now check to make certain the proper file is being read
DF.info()

x = DF['ExpFact']
y = DF['D_L']
w = DF['Err_D_L']

# Enforce non-zero error to avoid NaN in least squares resulting as product of inf and 0
w.mask(w == 0, 1e-9)

def func(x, Hubble, Matter):
    return (299793/(Hubble*x*np.sqrt(np.fabs(1-Matter)))*np.sinh(2*(np.arctanh(np.sqrt(np.fabs(1-Matter)))-np.arctanh(np.sqrt(np.fabs(1-Matter))/np.sqrt((Matter/x)+np.fabs(1-Matter))))))

popt, pcov = optimize.curve_fit(func, x, y, sigma=w, p0=[70, 0.5], bounds=([60,0.01],[80,0.99]))
fitLabel = 'fit: Hubble=%5.3f, Matter=%5.3f' % (popt[0], popt[1])

plt.figure()
plt.plot(x, y, '+', label='data')
xf = np.linspace(x.min(), x.max(), num=50)
plt.plot(xf, func(xf, *popt), 'g--',
         label=fitLabel)

plt.xlabel('redshift')
plt.ylabel('mag')
plt.legend()
plt.show()

# %%
