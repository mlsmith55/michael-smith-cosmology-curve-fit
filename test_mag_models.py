# -*- coding: utf-8 -*-
#%%
"""
Created on Mon Dec 28 17:28:35 2020

@author: Mike
"""

import pandas as pd
import numpy as np
import scipy.optimize as optimize
import matplotlib.pyplot as plt
from models.logDE_mag import logDE_mag
from models.logST_mag import logST_mag
from models.logInterST_mag import logInterST_mag
from settings import curve_fit_parameter_settings

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
Z = DF['Z']
m_B = DF['m_B']
error_m_B = DF['Error_m_B']

for model in [logDE_mag, logST_mag, logInterST_mag]:
    popt, pcov = optimize.curve_fit(
        model,
        Z,
        m_B,
        sigma=error_m_B,
        **curve_fit_parameter_settings
    )

    plt.figure()
    plt.errorbar(Z, m_B, error_m_B, fmt='.', label='data', capsize=5)
    Zf = np.linspace(Z.min(), Z.max(), num=50)
    plt.plot(Zf, model(Zf, *popt), 'g--',
            label='fit: Hubble=%5.3f, Matter=%5.3f' % (popt[0], popt[1]))

    plt.title('Model: %s' % (model.__name__))
    plt.xlabel('redshift')
    plt.ylabel('mag')
    plt.legend()
    plt.show()

# %%
