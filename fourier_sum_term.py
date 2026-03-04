# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 

@author: kubap
"""

#Fourier sum term 
import numpy as np
import scipy.integrate as integrate

def function(x):
    func = x**2
    return func

n = int(input("How many terms in Fourier series? "))

A_coefficients = np.array([])
B_coefficients = np.array([])
sum_term = np.array([])

for i in range(n):
    A_n = integrate.quad(lambda x: function(x) * np.cos(i*x), 0, 2*np.pi)[0] / np.pi
    B_n = integrate.quad(lambda x: function(x) * np.sin(i*x), 0, 2*np.pi)[0] / np.pi 
    
    total_term = lambda x: A_n * np.cos(i*x) +  B_n * np.sin(i*x)
    sum_term = np.append(sum_term, total_term)

print(sum_term)