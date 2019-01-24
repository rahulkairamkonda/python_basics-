# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 19:52:16 2018

@author: Deepali Vora

train.csv is titatic ka data set to chk survival of ppl 

this ready made versiom of sample-lr-1.py which was core linear regression 

data should be clean before u give to fit function 
"""
import pandas as pd
#import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
# %%
df1=pd.read_csv("train.csv",names=['Age','Ht','X','Y'],header=0);
df1.head()
df1.drop('X',axis='columns', inplace=True);# Indicates that Column X is required to be removed.
df1.head()
df1.drop('Y',axis='columns', inplace=True);
df1.head()
#%%
cols = df1.shape[1] 
print(cols )

#%%
X = df1.iloc[:,0:cols-1]  
X.head()

#%%
y = df1.iloc[:,cols-1:cols] 
y.head()
#%%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
#%%
# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = regr.predict(X_test)
#%%
print(y_pred) 
#%%
fig, ax = plt.subplots(figsize=(12,8))  
#ax.plot(X_test, y_test, 'r', label='Prediction')  
ax.scatter(X_test, y_pred, label='Prediction', color='red')  
ax.scatter(X_train, y_train, label='Traning Data')  
ax.legend(loc=2)  
ax.set_xlabel('Age')  
ax.set_ylabel('Height')  
ax.set_title('Predicted Height vs. Age') 
#%%This will plot actual prediction of height and actual height for the test data
fig, ax = plt.subplots(figsize=(12,8)) 
ax.scatter(X_test,y_test,label='Actual Data',color='blue')
ax.scatter(X_test,y_pred,label='Predicted Data',color='red')
ax.legend(loc=2)  
ax.set_xlabel('Age')  
ax.set_ylabel('Height')  
ax.set_title('Predicted Height vs. Age') 
#%%This will plot actual prediction of height and actual height for the test data 
fig, ax = plt.subplots(figsize=(12,8)) 
ax.scatter(X_test,y_test,label='Actual Data',color='blue')
ax.plot(X_test,y_pred,label='Predicted Data',color='red')
ax.legend(loc=2)  
ax.set_xlabel('Age')  
ax.set_ylabel('Height')  
ax.set_title('Predicted Height vs. Age') 
#%%
print("Mean squared error: %.2f"% mean_squared_error(y_test, y_pred))
print('Variance score: %.2f' % r2_score(y_test, y_pred))