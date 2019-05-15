#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:44:32 2019

@author: yanzhiwen
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:59:48 2019

@author: yanzhiwen
"""


# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#use n to count, while to loop
#add 1000 people to vaccination every new loop
v=0
while v<=10000:
    infected = [1]
    beta = 0.3
    gamma = 0.05
    # the initial value of population, infected, recovered, vaccinated and susceptible
    p=10000
    i=1
    r=0
    s=int(10000-v) 
    n=0
    while n <= 1000:
        n = n+1
        #choose susceptible people to be infected, remove from s, add to i
        x = sum(np.random.choice(range(2),s,p=[1-beta*i/p,beta*i/p]))
        #choose infected people to be recovered, remove from i, add to r
        y = sum(np.random.choice(range(2),i,p=[1-gamma,gamma]))
        s = s-x
        i = i+x-y
        r = r+y
        #record infected number in every loop
        infected.append(i)
    v=v+1000  
    #make plot
    plt.plot(infected,label=str(v/10000))
    plt.xlabel('time')
    plt.ylabel('number of people')
    plt.legend(loc='upper right')
    plt.title('SIR model')      