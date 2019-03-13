# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 08:32:38 2019

@author: jp
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,1001)


y1 = x**3+2*x**2+4*x
y2 = 3*x**2+4*x+4
y3 = np.linspace(-10,10,101)

fig, ax = plt.subplots(1,1,figsize=[16,8])

ax.plot(x,y1,'b')
ax.plot(x,y2,'g')
ax.plot(x,y3,'r')
ax.set_ylim([-100,100])
ax.grid(True)