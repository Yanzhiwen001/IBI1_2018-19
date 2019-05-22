#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:09:47 2019

@author: yanzhiwen
"""

import pandas as pd
df=pd.read_excel('Final_Fluview_Practical_dataset.xlsx')
#df.info()
#print(df.head(5))

df_regress=df[['Virus Strain','Age','Gender','Hospitalized?','Swine Contact?','Attended Agricultural Event?']]
df_regress[df_regress.isna().any(axis=1)]
df_regress=df_regress.dropna()
#df_regress.info()

for y in df_regress:
    print(y,df_regress[y].unique())

df_regress['Age']=df_regress['Age'].map({'<18 Years':0,'>=18 Years':1})
df_regress['H1N2v']=df_regress['Virus Strain'].map({'Influenza A H3N2v':0,'Influenza A H1N1v':0,'Influenza A H1N2v':1,'Influenza A H7N2':0})
df_regress['Gender']=df_regress['Gender'].map({'Male':0,'Female':1,'male':0,'female':1})
df_regress['Hospitalized?']=df_regress['Hospitalized?'].map({'Yes':1,'No':0,'yes':1,'no':0})
df_regress['Swine Contact?']=df_regress['Swine Contact?'].map({'Yes':1,'No':0,'yes':1,'no':0})
df_regress['Attended Agricultural Event?']=df_regress['Attended Agricultural Event?'].map({'Yes':1,'No':0,'yes':1,'no':0})

for y in df_regress:
    print(y,df_regress[y].unique())

import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np

endog=df_regress['H1N2v']
exog=sm.add_constant(df_regress[['Age','Gender','Hospitalized?','Swine Contact?','Attended Agricultural Event?']])
logit=smf.Logit(endog,exog)
result=logit.fit()
print(result.summary())
print('Odds ratios:')
print(np.exp(result.params))
