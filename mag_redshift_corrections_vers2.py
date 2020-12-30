# -*- coding: utf-8 -*-
#%%
"""
Created on Sat Dec 12 15:31:02 2020

@author: Mike
"""

# importing pandas and numpy libraries 
import pandas as pd
#import numpy as np 
"""   
Importing the redshift Z data, the mag, typically labeled m_B and the error, Error_m_B, associated with each mag value. m_B to be calculated becoming the expansion factor, the proper D_L distance and associated error, Err_D_L. This read command declares the first row a proper string which cannot be used for calculations.
"""
df=pd.read_csv('data/Riess1998_mag_Data.csv', header=0)
"""
Print information to check if the correct file has been imported. The first row, being strings, should not be numbered nor used as data, but the first row of numerical data should be numbered as zero. The table characteristics shall be printed first.
"""
df.info()  
"""
Applying lambda function to calculate the expansion factor
by using df.assign()on values of the redshift, Z, column.
"""   
df = df.assign( Expansion_factor = lambda x: (1/(1+x['Z'])))
""" 
Applying lambda function to calculate the real distance D_L using the values from the m_B column.
""" 
df = df.assign(D_L = lambda x: 10**((x['m_B']-25)/5))
"""
Calculating the associated error is slightly more complicated. We first apply the lambda function to calculate the Distance_Error, here in a geometric manner. First calculate the lower and the upper mag value errors as applied to the m_B values.
"""
df=df.assign(Lower_m_B = lambda x: x['m_B']-x['Error_m_B'])
df=df.assign(Upper_m_B = lambda x: x['m_B']+x['Error_m_B'])
"""
Next calculate the lower and upper distances, as D_L, after the error values have been applied.
"""
df = df.assign(LowVal = lambda x: 10**((x['Lower_m_B']-25)/5))
df = df.assign(UpVal = lambda x: 10**((x['Upper_m_B']-25)/5))
"""
Then calculate the differences of the upper and lower errors associated with each value of D_L
"""
df=df.assign(Up_SD = lambda x: (x['UpVal']-x['D_L']))
df=df.assign(Low_SD = lambda x: (x['D_L']-x['LowVal']))
"""
Then calculate the the geometric standard deviations for each distance estimate, D_L, as Err_DL
"""
df = df.assign(nearly = lambda x: x['Up_SD']*x['Low_SD'])
#df.nearly=df.nearly.round()
df['Err_D_L']=df['nearly']**(1/2)
""" The values of D_L and Err_D_L should be rounded to not give the impression that these values are really accurate."""
decimals = pd.Series([1, 1], index=['D_L', 'Err_D_L'])
df.round(decimals)
"""
Finally we need to add the values of the expansion factor, 1, the D_L of 0, and the error of 0 associated with the position of the earth. These vaules must be used in any fit of SNe, gamma-ray burst or HII type data and cannot be excluded for any reason.
"""
to_append = ['earth', 0,0,0,1,0,0,0,0,0,0,0,0,0]
df_length = len(df)
df.loc[df_length] = to_append
"""
Now to display the data frame of the original and calculated data. 
"""
df.info()
print(df) 
print('Remember the row count begins at 0 with Python. Also, the values of columns m_B and m_B may not be used as data for the log fits, since we have assigned the two values as 0, here, just as place holders - so any regression analysis will be quite difficult, perhaps impossible.')
"""
Now the completed file is saved in csv format
"""
df.to_csv('data/test.csv')
"""
The above name is only an example.
"""
# %%
