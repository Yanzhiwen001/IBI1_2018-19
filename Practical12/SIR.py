#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:59:48 2019

@author: yanzhiwen
"""


# import necessary libraries
import numpy as np
import matplotlib . pyplot as plt

population = []
susceptible = [9999]
infected = [1]
recovered = []
beta = 0.3
gamma = 0.05

s = list(range(9999))
#print(len(s))
i = [1]
r = []

#use n to count, for while to loop
n = 0
while n <= 1000:
    n = n+1
    #choose susceptible people to be infected, remove s, add i
    x = np.random.choice(range(2),len(s),p=[1-beta*len(i)/10000,beta*len(i)/10000])
    m = 0
    for xi in x:
        if xi == 1:
            m = m+1
            i.append(xi)
            s.pop()
    #choose infected people to be recovered, remove i, add r
    y = np.random.choice(range(2),len(i),p=[1-gamma,gamma])
    q = 0
    for yi in y:
        if yi == 1:
            q = q+1
            r.append(yi)
            i.pop()
    susceptible.append(len(s))
    infected.append(len(i))
    recovered.append(len(r))

#print(susceptible,infected,recovered)     

plt.figure(figsize =(6,4),dpi=100)
plt.plot(susceptible, label='susceptible')
plt.plot(infected,label='infected')
plt.plot(recovered,label='recovered')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()
plt.savefig('/Users/wanwan/Documents/IBI/L12/fig1' ,type='.png')
plt.show()

            