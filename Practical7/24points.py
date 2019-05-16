#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:49:07 2019

@author: yanzhiwen
"""
import copy
from fractions import Fraction
#input data
data=input('input integer between 1-23, using ","\n')
numList = data.split(',')
num = list(map(int,numList))  
#check the input numbers
judge=0
for i in num:
    if i>23 or i<0:
        judge=1
        print('please input integers between 1-23')
        break
    
#recursion times
count = 0 
def dfs(n):#n is len(num)
    global count
    global num
    count = count +1
    #test for stop condition
    if n == 1:
        if(float(num[0])==24):
            return 1
        else:
            return 0
    #select two different numbers
    for i in range(0,n):
        for j in range(i+1,n):
            num2=copy.deepcopy(num)
            a = num[i]
            b = num[j]
            
            #try every possible algorithm for two numbers
            num[i] = a+b
            num.pop(j)
            if(dfs(n-1)):
                return 1
            else:
                num=copy.deepcopy(num2)#traceback
            
            num[i] = a-b
            num.pop(j)
            if(dfs(n-1)):
                return 1 
            else:
                num=copy.deepcopy(num2)
            
            num[i] = b-a
            num.pop(j)
            if(dfs(n-1)): 
                return 1
            else:
                num=copy.deepcopy(num2)
            
            num[i] = a*b
            num.pop(j)
            if(dfs(n-1)): 
                return 1  
            else:
                num=copy.deepcopy(num2)
                
            #the problem of floats and test if the dividend is zero 
            if a:
                num[i] = Fraction(b,a)
                num.pop(j)
                if(dfs(n-1)): 
                    return 1 
                else:
                    num=copy.deepcopy(num2)
                
            if b:
                num[i] = Fraction(a,b)
                num.pop(j)
                if(dfs(n-1)): 
                    return 1 
                else:
                    num=copy.deepcopy(num2)
            
    return 0
#if the input is correct then calculate
if judge==0:
    if (dfs(len(num))): 
        print('Yes')
        print('Recursion times:',count)
    else: 
        print('No')
    
#the complexity of this code is n times n