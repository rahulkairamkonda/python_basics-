# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 09:39:17 2018

@author: Deepali Vora
"""
#%%
import pandas as pd;
import numpy as np;
b=3.14512
a=np.ceil(b);
print (a);
#%%
data = pd.DataFrame({'group': ['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'],
                 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]});

print (data);
print('------------');
print (data.describe()); # gives count min max std etc abt the data 
print ('-----------');
print (data.info());
print ('-----------');
data.sort_values(by=['group','ounces'], ascending=[False, True], inplace=True);
print(data);

data = pd.DataFrame({'k1': ['one'] * 3 + ['two'] * 4, 'k2': [3, 2, 1, 3, 3, 4, 4]})
data.sort_values(by='k2')
print(data)
print ('-------------------------------');
print(data.drop_duplicates());  # by default, duplicate is defined by all columns
#print(data)
print ('-------------------------------');
print(data.drop_duplicates(subset='k1'));  # duplicate in column k1 only second row first occurance is kept
#print(data)
print ('-------------------------------');

 
df = pd.DataFrame({'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)});
#%%
#Add a new column to the dataset
print(df.assign(ratio = df['data1'] / df['data2']));
print ('-------------------------------');
#%%
#binning data into intervals
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32];
bins = [18, 25, 35, 60, 100];
#%%
#pd.cut(X,bins)
cats = pd.cut(ages, bins);# will put the values in bins
print(cats);
print(pd.value_counts(cats));# will count values in each bin


group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior'];
print(pd.cut(ages, bins, labels=group_names));
print(pd.value_counts(pd.cut(ages, bins, labels=group_names)));

#%%
