import numpy as np

def model(D_L, Hubble, Matter):
    x = D_L
    return (299792/(Hubble*x*np.sqrt(np.fabs(1-Matter)))*np.sinh(2*(np.arctanh(np.sqrt(np.fabs(1-Matter)))-np.arctanh(np.sqrt(np.fabs(1-Matter))/np.sqrt((Matter/x)+np.fabs(1-Matter))))))
