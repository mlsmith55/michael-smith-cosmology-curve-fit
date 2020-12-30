import math
import numpy as np
from scipy.integrate import quad

"""
The function below is the exact function decribing the FLRW model with two paramters, Hubble constant and matter density. Note this is a 2-parameter FIT OF FLAT SPACETIME WITH DARK ENERGY
###########
This second portion is the function to be integrated which is mag version of equation E5 of DOI: 10.5772/intechopen.91266. The next definition is the function needed for integration
"""
def portion2(Z, Matter):
    return 1/(math.sqrt((1+Z)**2)*(1+Matter*Z) - 2*(2+Z)*math.fabs(1-Matter))

"""
This definition is the integration process, note the integration is from 0 to Z and not 1 to Z as per the equation E5.
"""
def intersum(Z, Matter):
    return quad(portion2, 0, Z, args=(Matter))[0]
vectorizedIntersum = np.vectorize(intersum, excluded=["Matter"])

"""
This is a simple calculation of the pre-integral portion of E5
"""
def portion1(Z, Hubble):
    return 299792*(1+Z)/Hubble

def model(Z, Hubble, Matter):
    return (5*np.log10(portion1(Z, Hubble))*(vectorizedIntersum(Z, Matter))+25)
