# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 19:34:21 2018

@author: Deepali Vora
"""
 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'''
heade() gives first 5 values of database 
'''
# %%
df1=pd.read_csv("girls_train.csv",names=['Age','Ht','X','Y'],header=0); # header=0 means no header in csv
df1.head()
df1.drop('X',axis='columns', inplace=True);# Indicates that Column X is required to be removed.
df1.head()
df1.drop('Y',axis='columns', inplace=True);
df1.head()
# In[21]:
df1.insert(0,'Ones',1) # add the column of 1 at the start of the dataframe
#df1.insert(location,column label,value)

# In[23]:
df1.head()
# In[31]:
cols = df1.shape[1] 
print(cols )

# In[26]: 
X = df1.iloc[:,0:cols-1]  
X.head()

# In[27]:
y = df1.iloc[:,cols-1:cols] 
y.head()

# In[32]:
X = np.matrix(X)  #convert data frames to matrix for further calculation
y = np.matrix(y)  
theta = np.matrix(np.array([0,0])) 
'''
x has ones and age and y is only height 
'''

# In[33]:
print(theta)

# %% Function to calculate the cost
def computeCost(X, y, theta):  
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))

# In[35]:
cost=computeCost(X, y, theta) 
print(cost)
# In[36]:
def gradientDescent(X, y, theta, alpha, iters):  
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    cost = np.zeros(iters)

    for i in range(iters):
        error = (X * theta.T) - y

        for j in range(parameters):
            term = np.multiply(error, X[:,j])
            temp[0,j] = theta[0,j] - ((alpha / len(X)) * np.sum(term))

        theta = temp
        cost[i] = computeCost(X, y, theta)

    return theta, cost
# In[37]:
alpha = 0.01  
iters = 1000
# In[38]:
g, cost = gradientDescent(X, y, theta, alpha, iters)

# In[39]:
print(g)

# In[51]:
x = np.linspace(df1.Age.min(), df1.Age.max(), 100)  
#numpy. linspace (start, stop, num=50, endpoint=True, retstep=False, dtype=None)Return evenly spaced numbers over a specified interval.

# In[53]:

#get_ipython().magic('matplotlib inline')
f = g[0, 0] + (g[0, 1] * x)  #computer the new value of height from the values of theta
fig, ax = plt.subplots(figsize=(12,8))  
ax.plot(x, f, 'r', label='Prediction')  
ax.scatter(df1.Age, df1.Ht, label='Traning Data')  
ax.legend(loc=2)  
ax.set_xlabel('Age')  
ax.set_ylabel('Height')  
ax.set_title('Predicted Height vs. Age') 


# In[ ]:

print(f)

