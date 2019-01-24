# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 16:27:07 2018

@author: Deepali Vora

"""

#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%
# evenly sampled time at .2 intervals 
t= np.arange(0., 5., 0.2) 
# red dashes, blue squares and green triangles 
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.axis([0, 6, 0, 150]) # x and y range of axis  (size of graph)
plt.show() # will display the graph 

#%%
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.axis([0, 6, 0, 150])
plt.show()

fig = plt.figure()

ax = fig.add_subplot(311)
plt.plot(t,t**2,'bs')
plt.show()

ax = fig.add_subplot(312)
plt.plot(t,t**2,'g^')
plt.show()

ax = fig.add_subplot(313)
plt.plot(t,t**2,'r--')
plt.show()


#%%
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
ax.set_xlim(0.5, 4.5) # set the limit for x-axis
plt.show()

#%%
mu, sigma = 100, 15 
x = mu + sigma * np.random.randn(10000) 
# the histogram of the data 
n,bins,patches=plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability') 
plt.title('Histogram of IQ') 
plt.text(60, .025, r'$\mu=100,\ \sigma=15$') #TeX equations 
plt.axis([40, 160, 0, 0.03]) #x and y axis margins
plt.grid(True) 
plt.show() 
#%%
url ="girls_age_weight_height_2_8.xlsx"
names = ['AGE','WEIGHT','HEIGHT']
df1=pd.read_excel(url,names=names)
df1.head()
#%%
x=df1['AGE']
y=df1['HEIGHT']
z=df1['WEIGHT']
#%%
plt.plot(x,ls='solid')
plt.show()
#%%
plt.scatter(x,x)
plt.show()


