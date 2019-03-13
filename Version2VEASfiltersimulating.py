# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 14:40:46 2019

@author: jp
"""

import matplotlib.pyplot as plt
import numpy as np
import math 


# Time settup
start = 0
stop = 5*60*60
Ts = 1
numberOfSamples = int(((stop - start)+1)/Ts)

# initiating arrays
t_array = np.linspace(start, stop, numberOfSamples)
u_array = np.ones(len(t_array))
y_array = np.ones(len(t_array))
w_array = np.ones(len(t_array))


# Setting up parrameters
Tf = 100 # Filter tidskonstant maks på AI820 er "65535 ms" / "65,535 s"

antallSvingninger = 3
Hz = antallSvingninger/(stop-start)
stoy = 0
stoy = stoy/(stop-start)

# CONSTRUCTING MODEL INPUT
for k in range(len(t_array)):
    if t_array[k] < 7500 :
        u_array[k] = 1
        if t_array[k] < 2500 :
            u_array[k] = 0
        elif t_array[k] < 5000 :
            u_array[k] = 1
    else:
        Hz1 = math.sin((2*math.pi*Hz)*(t_array[k]+1.5))
        Hz2 = math.sin((2*math.pi*stoy)*t_array[k])
        # TOTAL FREQUENCY
        u_array[k] = Hz1 + Hz2*0.2 
        w_array[k] = Hz1

# SIMULATING MODEL
Y_k_1 = 0
for k in range(len(t_array)):
        #u_array[k] = 1
    
    a = (Ts/(Tf+Ts))
    y_array[k] = (1-a) * Y_k_1 + a * u_array[k]
    Y_k_1 = y_array[k]
    
    


#array63p = np.ones(len(t_array))*(1-(u_array[0]-u_array[-1])*0.632)

fig, ax = plt.subplots(nrows=1,ncols=1, figsize=(12,8))
axes = ax.plot(t_array, u_array, label="Value")
axes = ax.plot(t_array, y_array, label="Filtered VAlue")
#axes = ax.plot(t_array, w_array, label="wanted value")

ax.set_title('Model#1')
ax.set_xlabel('Time (s)')
ax.set_ylabel('input/output')
#ax.set_xlim([2400, 3000])
ax.set_ylim([-2, 2])
ax.legend()
#axes = ax.plot(t_array,u_array,t_array,y_array,t_array,array63p)

fig.savefig('stepresponse')