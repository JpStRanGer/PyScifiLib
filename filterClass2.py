# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 12:40:56 2019

@author: jp
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import time
#start = 0
#stop = 6
#Ts = 0.01  
#NumbSamp = ((stop-start)/Ts)+1
toc = time.time()

class stoy():
    def __init__(self, start = 0, stop = 3, Ts = 0.01):
        #initiating Variables
        self.start = start
        self.stop = stop
        self.Ts = Ts 
        self.hz = ((np.random.random()*2)-1)
        self.amp = np.random.random()
        self.offset = ((np.random.random()*2)-1)
        self.NumbSamp = ((self.stop-self.start)/self.Ts)+1
        #initiating arrays
        self.timeArray = np.linspace(self.start, self.stop, self.NumbSamp)
        self.output = np.zeros(len(self.timeArray))
        
        for k in range(len(self.timeArray)):
            self.output[k] = self.amp*np.sin(2*np.pi*self.timeArray[k]*self.hz+self.offset) + self.offset
        
    def __init__(self, start = 0, stop = 3, Ts = 0.01, hz = 0, amp = 1, offset = 0):
        #initiating Variables
        self.start = start
        self.stop = stop
        self.Ts = Ts 
        self.hz = hz
        self.amp = amp
        self.offset = offset
        self.NumbSamp = ((self.stop-self.start)/self.Ts)+1
        #initiating arrays
        self.timeArray = np.linspace(self.start, self.stop, self.NumbSamp)
        self.output = np.zeros(len(self.timeArray))
        
        for k in range(len(self.timeArray)):
            self.output[k] = self.amp*np.sin(2*np.pi*self.timeArray[k]*self.hz+self.offset) + self.offset
      

stoyArray = []

for i in range(3):
    stoyArray.append(stoy(start = 0,stop = 100, Ts = 0.01, hz = 0, amp = 1, offset = 0))
    #print(stoyArray[i].hz)

timeArray = stoyArray[0].timeArray
sinus = np.zeros(len(stoyArray[0].timeArray))

for i in stoyArray:
    sinus = sinus + i.output/len(stoyArray)

sinus2 = np.zeros(len(stoyArray[0].timeArray))
for k in range(len(timeArray)):
    sinus2[k] = 3*np.sin(2*3.14*timeArray[k]/30)

sinus1 = sinus + sinus2

fig, ax = plt.subplots(nrows=3,ncols=1,figsize=(16,8))
ax[0].set_title("Plot Tittel")
ax[0].plot(timeArray, sinus, label="lable")
ax[1].set_title("Plot Tittel")
ax[1].plot(timeArray, sinus1, label="lable")
ax[2].set_title("Plot Tittel")
ax[2].plot(timeArray, sinus2, label="lable")


fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
for i in range(len(stoyArray)):
    ax.plot(stoyArray[0].timeArray, stoyArray[i].output, label="lable")
#ax.grid(True)
#ax.legend()
    
tic = time.time()
print("################################################")
print("Elapsed time: {:04.4f}s".format(tic - toc))
print("################################################")
print()