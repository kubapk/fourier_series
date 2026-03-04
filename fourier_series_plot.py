# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 
(Based on a project from Oliver Smedt)

@author: Kuba Kane
"""

#Fourier series 
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

def func(x):
    x = x % (2*np.pi)
    x = x**2
    return x


def series_terms(function, n):
    A_coefficients = np.array([])
    B_coefficients = np.array([])
    
    for i in range(n):
        A_n = integrate.quad(lambda x: function(x) * np.cos((i+1)*x), 0, 2*np.pi)[0] / np.pi
        B_n = integrate.quad(lambda x: function(x) * np.sin((i+1)*x), 0, 2*np.pi)[0] / np.pi 

        A_coefficients = np.append(A_coefficients, A_n)
        B_coefficients = np.append(B_coefficients, B_n)
    

    a_0 = integrate.quad(function,0,2*np.pi)[0]/(2*np.pi)
    
    return a_0, A_coefficients, B_coefficients


def fourier_series_plot(function, n):
    x = np.linspace(0,4*np.pi,1000) #0 to 4pi in steps of 1000
    y = function(x)
    
    a_0, a_coefs, b_coefs = series_terms(function, n)
    print("a_0 =: ", a_0)
    print("a_coefs (sin coeffs) = : ", a_coefs)
    print("b_coefs (cos coeffs) = : ", b_coefs)

    plt.plot(x, y, label = "function") #plot of original func
    
    series = np.full(1000, a_0) #create array where all terms take the value
    #of a_0 (1000 since there are 1000 x steps)
    
    for i in range(n):
        print("\n x:", x)
        series += a_coefs[i]*np.cos((i+1)*x) + b_coefs[i]*np.sin((i+1)*x)
        print("\n series: ",series)
        
        
    plt.plot(x, series, label = "series n={}".format(n))
    plt.legend()


def main():
    n = int(input("How many terms in Fourier series? "))
    fourier_series_plot(func, n)
    return 

main()
