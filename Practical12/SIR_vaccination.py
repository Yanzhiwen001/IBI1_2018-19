#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:59:48 2019

@author: yanzhiwen
"""


# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#s = list(range(10000-v))


#use n to count, use while to loop
v=0
while v<=10000:
    n = 0
    s = list(range(10000-v))
    population = []
    susceptible = [9999]
    infected = [1]
    recovered = []
    beta = 0.3
    gamma = 0.05
    i = [1]
    r = []

    while n <= 1000:
        n = n+1
    #choose susceptible people to be infected, remove s, add i
        x = np.random.choice(range(2),len(s),p=[1-beta*(len(i)/10000),beta*(len(i)/10000)])
        m = 0
        #find every infected person in susceptible group
        for xi in x:
            if xi == 1:
                m = m+1
                i.append(xi)
                s.pop()
    #choose infected people to be recovered, remove i, add r
        y = np.random.choice(range(2),len(i),p=[1-gamma,gamma])
        q = 0
        #find every recovered person in infected group
        for yi in y:
            if yi == 1:
                q = q+1
                r.append(yi)
                i.pop()
        #record infected number in every loop
        infected.append(len(i))
#make polt   
    plt.plot(infected,label=str(v/10000))
    plt.xlabel('time')
    plt.ylabel('number of people')
    plt.legend(loc='upper right')
    plt.title('SIR model')
    v=v+1000       
