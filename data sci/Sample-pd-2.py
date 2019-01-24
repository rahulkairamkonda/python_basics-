# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 10:17:53 2018

@author: Deepali Vora
"""
#%%
import pandas as pd

url ="girls_age_weight_height_2_8.csv"
#url = "d:\\phd\\Impl\\Dataset-All-New.xlsx"
#names = ['AGE','WEIGHT','HEIGHT']
#Read Data if excel then use this
#dataframe = pd.read_excel(url, names=names)
#use for CSV
#,skiprows=1)
#df=pd.DataFrame(dataf,columns=['AGE','WEIGHT','HEIGHT'])
df = pd.read_csv(url)
#%%
#dataf.mean()
df.head()
df.describe()
df.info()
df.shape
rows=df.shape[0]
cols=df.shape[1]

X=df.iloc[:,0:cols-1]  # copy only age and height cols-1 (number of column 1) clos is taken from shape
Y=df.iloc[:,cols-1:cols] # X print 1 and 2 line and this line will print 3 column 
print(Y)

df.iloc[:,0:1].mean()
#%%
#read excel file
url ="girls_age_weight_height_2_8.xlsx"
names = ['AGE','WEIGHT','HEIGHT']
df1=pd.read_excel(url,names=names)

df1.head()
df1['AGE'].head(5)

#print weight of person with max age
print(df1['WEIGHT'][df1['AGE']==df1['AGE'].max()])

#print values sorted by weight
print(df1.sort_values(by='WEIGHT', ascending=False))


