# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 23:40:32 2018

@author: Deepali Vora
"""

import pandas as pd
#%%
'''
simple list to be view in rows and column format (tabular form)
column is column name of the data avaiable 
'''
data = [['A',10,9,9.2],['P',8,8,7.5],['N',9,7,8],['C',8,10,9]]
df = pd.DataFrame(data,columns=['Name','M1','M2','AVG'])
print(df)
#%%
# indexing row,col
'''
location of data using index [rows,columns]
'''
df.iloc[:,1:3]
df.iloc[1:2,0:4]
df.iloc[:]
#%% 
#shape is same as done in numpy

#print the nnumber of rows and columns
df.shape
#print only rows
df.shape[0]
#print only number of columns
df.shape[1]
#%%
'''
if columns have name then we cant use iloc we have to use the header name 
df['name'] or df.iloc(:1) both will read the first column
'''
#operations using DataFrame
print(df[df['M1']>8])
#mean
print(df['M1'].sum())

print(df['M1'].mean())

print(df['M1'].max())
print(df['M1'].min())
print(df['M1'].count())

print(df['AVG'].max())

print(df['Name'][df['AVG']==df['AVG'].max()])   # in prev line avg ka max is found and then left side of 
# searches all the ppl gives the the name 
#Sorting of values as per columns
print(df['Name'][df['M1']>9]) # extra 
print(df.sort_values(by=['M1']))
print(df.sort_values(by=['M1'], ascending=False))
#%%
#Print the name with highest average
MaxName = df['Name'][df['AVG'] == df['AVG'].max()].values
print(MaxName)
#%%
print(df.iloc[:,:][df['AVG']==df['AVG'].min()])
#show selected head and tail data
df.head(2)
df.tail(2)

print(df.sort_values(by=['M1']))

df.sort_values(by=['M1','M2'], ascending=[False, True], inplace=True);
# table is sorted with the first value M1 
# if M1 has same value then it will check M2 else it won't we even see M2 if M1 is unique 
# 

'''
when we sort OG DF(data frame) will not chnage and if we use inplace then OG dtaa value will change 

'''

'''
df.append(list) can be used to add data 

