# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:57:03 2019

@author: jp
"""

import matplotlib.pyplot as plt
import numpy as np


def model(x1_k, u_k, Fout, ts, w):
    A_tank = 0.1
    K_p = 0.002
    x1_kp1 = x1_k + (ts / A_tank) * (K_p * u_k - Fout) + w
    return x1_kp1

#Simulation time parameters
start = 0
stop = 250
Ts = 0.1
ns = (stop-start)/Ts+1

#simulation arrays
t_array     = np.linspace(start,stop,ns)
sp_array     = t_array*0
u_array     = t_array*0
Fout_array  = t_array*0
w_array     = t_array*0
h_array     = t_array*0
error_array = t_array*0

Kp_array  = t_array*0
Ti_array     = t_array*0
Td_array     = t_array*0

Kp = 10
Ti = 2
Td = 5


integral_e_km1 = 0
e_km1 = 0
h_k = 0


sp_array[int(50/Ts):] = 10
sp_array[int(120/Ts):] = 0
#for k in range(int(30/Ts)):
#    sp_array[int(125/Ts)+k:] = k
#    #print(k)


for k in range(len(t_array)):
    
#    ###########################
#    ### Generating Setpoint ###
#    ###########################
#    if t_array[k] > 100:
#        sp_array[k] = math.sin(2*3.14*t_array[k]/40)
    #######################
    ### PID controller: ###
    #######################
    #Control error:
    e_k = sp_array[k] - h_k
    error_array[k] = e_k
    #proportional
    up_k = Kp*e_k   
    Kp_array[k] = up_k
    #integral
    integral_e_k = integral_e_km1 + Ts*e_k
    ui_k = (Kp/Ti)*integral_e_k   
    Ti_array[k] = ui_k
    #Derivative term:
    de_k = (e_k - e_km1)/Ts
    ud_k = Kp*Td*de_k   
    Td_array[k] = ud_k
    #controler output
    u_k = up_k + ui_k#  + ud_k
    u_array[k] = u_k
    
    #########################
    ### simulating MODEL: ###
    #########################
    h_kp1 = model(h_k, u_k, 0.02, Ts, 0)
    #h_kp1 = model(h_k, u_k, 0.02*h_k, Ts, 0)
    h_array[k] = h_kp1
    
    #timeshift
    integral_e_km1 = integral_e_k
    e_km1 = e_k
    h_k = h_kp1
    
fig, ax = plt.subplots(2,1,figsize=(16,7))

ax[0].set_title("Nivå i meter")
ax[0].plot(t_array,sp_array,'r',label="setpoint [h (m)]")
ax[0].plot(t_array,h_array,'g',label="h_array [h (m)]")

ax[1].set_title("Nivå i meter")
ax[1].plot(t_array,u_array,label="controler output [h (m)]")

for i in range(len(ax)):
    ax[i].grid(True)
    ax[i].legend()
    #ax[i].set_ylim([0.280, 0.3])
    #ax[i].set_xlim([100, 200])
    
fig, ax = plt.subplots(3,1,figsize=(16,6))

ax[0].plot(t_array,error_array,label="Proportional")
ax[0].plot(t_array,Kp_array,label="Proportional")
ax[1].plot(t_array,Ti_array,label="Integral output")
ax[2].plot(t_array,Td_array,label="Derivate output")

for i in range(len(ax)):
    ax[i].grid(True)
    ax[i].legend()
    #ax[i].set_ylim([0.280, 0.3])
    #ax[i].set_xlim([100, 200])
print()
print("Kp = {Kp}\nTi = {Ti}\nTd = {Td}".format(Kp = Kp, Ti = Ti, Td = Td))