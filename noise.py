# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 12:18:28 2019

@author: jp
"""


import matplotlib.pyplot as plt
import numpy as np
import math 

class Stoy:
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
lars =Stoy('navnetErLars',23)
print(lars.name)

Liste=list(3)

for i in rang(10):
    pass


# Time settup
start = 0
stop = 60*60
Ts = 1
numberOfSamples = int(((stop - start)+1)/Ts)

# initiating arrays
t_array = np.linspace(start, stop, numberOfSamples)
u_array = np.random.normal(loc= 0, scale= 0.1, size = len(t_array))
y_array = np.ones(len(t_array))
w_array = np.ones(len(t_array))


###########################################
##              PLOTTING                 ##
fig, ax = plt.subplots(nrows=1,ncols=1, figsize=(12,8))
axes = ax.plot(t_array, u_array, label="Value")
axes = ax.plot(t_array, y_array, label="Filtered VAlue")
axes = ax.plot(t_array, w_array, label="wanted value")

ax.set_title('Model#1')
ax.set_xlabel('Time (s)')
ax.set_ylabel('input/output')
#ax.set_xlim([34, 38])
ax.set_ylim([-2, 2])
ax.legend()
#axes = ax.plot(t_array,u_array,t_array,y_array,t_array,array63p)
