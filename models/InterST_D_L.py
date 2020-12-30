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
DF=pd.read_csv(r'C:/Users/Mike/Desktop/MartinS/SNdata/Riess1998_DL_Data.csv')
#Now check to make certain the proper file is being read
DF.info()

x = DF['ExpFact']
y = DF['D_L']
w = DF['Err_D_L']
"""
The function below is the exact function decribing the FLRW model with two parameters, Hubble constant and matter density. Note this is a 2-parameter FIT OF CURVED SPACETIME WITHOUT DARK ENERGY
###########
This second portion is the function to be integrated
"""  
def portion2(x, Matter):
    return 1/(x*math.sqrt((Matter/x) + math.fabs(1-Matter)))
                     
def intersum(x):
    return quad(lambda x: portion2, x, 1)
"""
This first portion is a simple calculation
"""
def portion1(x, Hubble, Matter):
    return ((299792/(x*Hubble *math.sqrt(math.fabs(1-Matter))))
"""
putting the complete function together as the cmpltresult
"""
def cmpltresult(x, Hubble, Matter):
    return ((portion1)*math.sinh(math.sqrt(math.fabs(1-Matter))*(intersum)))          
"""
TypeError: unsupported operand type(s) for *: 'function' and 'function'
"""