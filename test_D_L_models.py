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

from settings import curve_fit_parameter_settings
from models.ST_D_L import ST_D_L
from models.InterST_D_L import InterST_D_L
from models.InterDE_D_L import InterDE_D_L

DF = pd.read_csv('data/Riess1998_DL_Data.csv')
#Now check to make certain the proper file is being read
DF.info()

x = DF['ExpFact']
d = DF['D_L']
ed = DF['Err_D_L']

# Enforce non-zero error to avoid NaN in least squares resulting as product of inf and 0
ed.mask(ed == 0, 1e-9, inplace=True)

for model in [InterDE_D_L, ST_D_L, InterST_D_L]:
    popt, pcov = optimize.curve_fit(model, x, d, sigma=ed, **curve_fit_parameter_settings)
    fitLabel = 'fit: Hubble=%5.3f, Matter=%5.3f' % (popt[0], popt[1])

    plt.figure()
    plt.errorbar(x, d, ed, fmt='.', label='data', capsize=5)
    xf = np.linspace(x.min(), x.max(), num=50)
    plt.plot(xf, model(xf, *popt), 'g--',
            label=fitLabel)

    plt.title('Model: %s. Hubble=%5.3f, Matter=%5.3f' % (model.__name__, popt[0], popt[1]))
    plt.xlabel('Expansion factor')
    plt.ylabel('D_L')
    plt.legend()
    plt.show()

# %%
