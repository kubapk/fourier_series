# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9

@author: kubap
"""

#Plotting a_0
import numpy as np
import scipy.integrate as integrate

def function(x):
    x = x**2
    return x

    
a_0 = integrate.quad(function,-np.pi,np.pi)[0]/(np.pi)

print(a_0)