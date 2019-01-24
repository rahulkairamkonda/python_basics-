#NumPy sample file 1

#Import the library
import numpy as np

#declare some variables of diffrent type
#%%
x = np.float32(1.0) 
y = np.int_([1,2,4])
z = np.arange(3, dtype=np.uint8)

#%%
print(x)
print(y)
print(z)
#%%
#find out the type of variable 
print(z.dtype)
print(x.dtype)

#%% Arrange
print(np.zeros((2,2),dtype=np.uint8))
print(np.ones((10,2), dtype=np.uint8))
#Create array with step arange(start,stop,step,dtype)
p=np.arange(2,8,2,dtype=np.uint8)
print(p)
p=np.arange(10)
print(p)
#%%
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
print (student)
#%%
print(np.linspace(1., 4., 6) )
print(np.random.random((2,3)) )

#%% step operator in 5 x 7 
y = np.arange(35).reshape(5,7) 
print(y)
#[start:stop:step]
print(y[1:5:2,::3])   # row,column ()

#%%
y=np.arange(20).reshape(4,5)
print(y)
#%%
print(y[0:3,3])
print(y[3,0:3])
print(y[0:3,0:3])

#%%Boolean indexing
print(y[y>10])
#%%
y=np.array([1,2,np.nan])
print(np.isnan(y))

#%% indexing by creating a 10 x 10 of 100 items and displaying 3x3 (1:4) coz 4 is -1

y=np.arange(100).reshape(10,10)
print(y)
print(y[1:4,1:4])

#%% operators 
a=np.arange(5)
b=np.arange(5)
a+b
a-b
a*b

#%% print those element from y 4x5 to disp values which is less than 10

y=np.arange(20).reshape(4,5)
print(y[y<10])

#%% matrix in pd data sci folder same name 

#%%  axis 0 column wise max 1 max in row wise 

a=np.random.random((2,3))
a
#a.sum()
#a.min()
#a.max()
#a.max(axis=0) # max in row 
a.min(axis=1) # min in a column

a.transpose()
a.shape=(2,3)
a.shape
a.ravel()