# -*- coding: utf-8 -*-
#%%
"""
Created on Mon Dec 21 14:22:19 2020

@author: Mike

Is there a simple way that allows me to provide a weighting function which produces results?
"""

import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np
from models.ST_D_L import model

DF = pd.read_csv('data/Riess1998_DL_Data.csv')
#Now check to make certain the proper file is being read
DF.info()

x = DF['ExpFact']
d = DF['D_L']
ed = DF['Err_D_L']

# Enforce non-zero error to avoid NaN in least squares resulting as product of inf and 0
ed.mask(ed == 0, 1e-9, inplace=True)

popt, pcov = optimize.curve_fit(model, x, d, sigma=ed, p0=[70, 0.5], bounds=([60,0.01],[80,0.99]))
fitLabel = 'fit: Hubble=%5.3f, Matter=%5.3f' % (popt[0], popt[1])

plt.figure()
plt.errorbar(x, d, ed, fmt='.', label='data', capsize=5)
xf = np.linspace(x.min(), x.max(), num=50)
plt.plot(xf, model(xf, *popt), 'g--',
         label=fitLabel)

plt.xlabel('redshift')
plt.ylabel('mag')
plt.legend()
plt.show()

# %%
