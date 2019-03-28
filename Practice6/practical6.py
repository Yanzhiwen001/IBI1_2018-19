#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:29:35 2019

@author: yanzhiwen
"""
#open file
input = open(r'address_information.csv','r')
aString = input.read()
import re 
string= re.split(r'[,\n]',aString)
#select right address and set up tuples
new=[]
final=[]
for i in range(0,len(string),3):
    new.append((string[i],string[i+1],string[i+2]))

for i in range(1,len(new)):
    if re.match(r'.+\d+.+',new[i][1]):
        final.append(new[i])
        print(new[i][1],':Correct aAddress!')
    elif re.match(r'.+\W\D+',new[i][1]):
        print(new[i][1],':Wrong aAddress!')

#sending emails

import smtplib
from email.header import Header
from email.mime.text import MIMEText
n=0

for items in final:  
    to_addr = items[1]
    from_addr = '3180111430@zju.edu.cn'
    password = 'XXXXXXXXX'
    smtp_server = 'smtp.zju.edu.cn'

    text=open('body.txt','r')
    text1=text.read()
    text1 = re.sub(r'User',items[0],text1) 
    
    msg = MIMEText(text1, 'plain', 'utf-8')
    msg['From'] = Header(from_addr, 'utf-8')
    msg['To'] = Header(to_addr, 'utf-8')
    subject=items[2]
    msg['Subject'] = Header(subject, 'utf-8')
    n=n+1

    try:
        server = smtplib.SMTP(smtp_server, 25)
        loginname='3180111430'
        server.login(loginname, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        print('Mail sent successfully!')
      
    except smtplib.SMTPException:
        print('error')

input.close()

