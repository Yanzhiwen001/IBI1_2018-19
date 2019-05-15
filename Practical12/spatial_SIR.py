#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:47:06 2019

@author: yanzhiwen
"""

import numpy as np
import matplotlib.pyplot as plt

population = np.zeros((100, 100))
outbreak = np.random.choice(range(100),2) 
population[outbreak[0],outbreak[1]] = 1

plt . figure ( figsize =(6,4),dpi=150)
#plt.imshow(population,cmap='viridis',interpolation='nearest')

beta = 0.3
gamma = 0.05

# find infected points
infectedIndex = np.where(population==1)

# loop through all infected points
count = 0
while count<=100:
    count += 1
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        
        if population[x,y]==1:
            population[x,y]=np.random.choice(range(3),1,p=[0,1-gamma,gamma])[0]
        
        # infect each neighbour with probability beta
        # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
             for yNeighbour in range(y-1,y+2):
                # don't infect yourself! (Is this strictly necessary?)no i think
                if (xNeighbour,yNeighbour) != (x,y):
                # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                    # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    infectedIndex = np.where(population==1)
    recoveredIndex = np.where(population==2)
        
plt.imshow(population,cmap='viridis',interpolation='nearest')

                      