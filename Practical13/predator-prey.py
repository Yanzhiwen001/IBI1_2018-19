#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:04:46 2019

@author: yanzhiwen
"""
import os
os.chdir("/Users/wanwan/Documents/IBI/IBI1_2018-19/Practical13")

def xml_to_cps():
    import os
    import xml.dom.minidom
    
    # first, convert xml to cps 
    os.system("/Applications/COPASI/CopasiSE -i predator-prey.xml -s predator-prey.cps")
    
    # now comes the painful part. Just copy and paste this ok
    
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w")
    cpsTree.writexml(cpsFile)
    cpsFile.close()

#run copasi within python 
xml_to_cps()

    
input= open('modelResults.csv','r')
result=input.read()
import re

string= re.split(',',result) 
string= re.split(r'[\n]',result)
A=[]
B=[]
n=0
for i in string:
    if n==0:
        names=re.split(r',+',i)
        n=1
    else:
        i=re.split(',',i)
        A.append(float(i[1]))
        B.append(float(i[2]))

#make plot
import matplotlib.pyplot as plt
plt.plot(A, label='predator(b=0.02,d=0.4)')
plt.plot(B,label='prey(b=0.1,d=0.02')
plt.xlabel('time')
plt.ylabel('population size')
plt.title('Time course')
plt.legend()
plt.show()

#to show the relationship between A and B
plt.plot(A,B)
plt.xlabel('predator population')
plt.ylabel('prey population')
plt.title('Limit cycle')
plt.show()


# import files and get content in tag parameter
import xml.dom.minidom
DOMTree=xml.dom.minidom.parse("predator-prey.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName('parameter')
print(terms)
#change all the parameter at one time
for term in terms:
    discribtion = term.getAttribute('parameter')
    #change value of parameter in the string
    #put the new attribute into tag parameter
#save this modified file and then rerun the whole code



import numpy
#loop for 100times
n=0
while n<=100:
    n=n+1
    count=0
    for term in terms:
        if count==0:
            discribtion = term.getAttribute('parameter')
            value=numpy.random.sample()
            #change value of parameter in the string
            #put the new attribute into tag parameter
            count=1
        if count==1:
            discribtion = term.getAttribute('parameter')
            value=numpy.random.sample()
            count=2
        if count==2:
            discribtion = term.getAttribute('parameter')
            value=numpy.random.sample()
            count=3
        if count==3:
            discribtion = term.getAttribute('parameter')
            value=numpy.random.sample()
            count=0
#save this modified file and then rerun the whole code
        
    
