# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 08:51:12 2019

@author: jp
"""




class model:
        
    def __init__(self):
        # Defining model States
        self.__T_env         = 28.0 # envirement temperature
        self.__T_k           = 28.0 # initial temperature
        
        #define model constants
        self.__theta_const   = 23.0# model Time constant
        self.__gain          = 3.5
        
    
    def timeDelay(self, inn):
        # Time delay:
        out = self.__delay_array[-1]
        delay_array_sliced = self.__delay_array[:-1]
        self.__delay_array = np.insert(delay_array_sliced, 0, inn)
        return out
    
    def AirHeater(self, u_k, d_k, Ts):
        
        # Solving diff eq:
        dT_dt_k = (1/self.__theta_const)*((self.__T_env - self.__T_k) + self.__gain*(u_k + d_k))
        T_kp1 = self.__T_k + Ts*dT_dt_k
        self.__T_k = T_kp1
        return T_kp1

if __name__ == "__main__":
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    airheater = model()
    
    
    start = 0
    stop = 100
    Ts = 0.1
    ns = int((stop-start)/Ts+1)
    
    t_array = np.linspace(start, stop, ns)
    temp_array = np.zeros(len(t_array))
    
    for k in range(len(t_array)):
        temp_array[k] = airheater.AirHeater(2,0,Ts)
    
    
    
    fig, ax = plt.subplots(2,1,figsize=(16,7))
    
    ax[0].set_title("Nivå i meter")
    ax[0].plot(t_array,temp_array,'r',label="setpoint [h (m)]")
