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

#%%
y = np.arange(35).reshape(5,7) 
#[start:stop:step]
print(y[1:5:2,::3])

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

#Array vs Matrix
A = np.array([ [1, 2, 3], [2, 2, 2], [3, 3, 3] ])
B = np.array([ [3, 2, 1], [1, 2, 3], [-1, -2, -3] ])
R = A * B  #Element wise operation
print(R)

MA = np.mat(A)
MB = np.mat(B)
R = MA * MB # Matrix operarion
print(R)