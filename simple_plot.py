# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9

@author: kubap
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,4*np.pi,100) #from 0 to 10 in steps of 100
y = (x % (2*np.pi))**2


fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(x, y)

axes.set_title(r'Plot of $y=x^2$')
axes.set_xlabel('x')
axes.set_ylabel(r'$y=x^2$')

axes.grid(which='major', color='#DDDDDD', linewidth=0.8)
axes.grid(which='minor', color='#EEEEEE', linestyle=':', linewidth=0.5)
axes.minorticks_on()
plt.savefig("even_process_Cm.png", dpi=600)
plt.show()
plt.close()
