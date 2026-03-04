# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9

@author: kubap
"""
#An and Bn coefficients sum

import numpy as np
import scipy.integrate as integrate

def function(x):
    x = x**2
    return x

n = int(input("How many terms in Fourier series? "))

A_coefficients = np.array([])
B_coefficients = np.array([])

for i in range(n):
    A_n = integrate.quad(lambda x: function(x) * np.cos((i+1)*x), 0, 2*np.pi)[0] / np.pi
    B_n = integrate.quad(lambda x: function(x) * np.sin((i+1)*x), 0, 2*np.pi)[0] / np.pi 
    
    A_coefficients = np.append(A_coefficients, A_n)
    B_coefficients = np.append(B_coefficients, B_n)
    
A_total = np.sum(A_coefficients)
B_total = np.sum(B_coefficients)

#print(A_total, B_total)

print("A_coefficients", A_coefficients)
print("B_coefficients", B_coefficients)

print(A_total)
print(B_total)