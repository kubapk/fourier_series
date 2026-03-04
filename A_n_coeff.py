# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9

@author: kubap
"""

#A_n coefficient
import numpy as np
import scipy.integrate as integrate

def function(x):
    x = x**2
    return x

n = int(input("How many terms in Fourier series? "))
A_n = integrate.quad(lambda x: function(x) * np.cos(n*x), 0, 2*np.pi)[0] / np.pi
B_n = integrate.quad(lambda x: function(x) * np.sin(n*x), 0, 2*np.pi)[0] / np.pi

print(A_n, B_n)