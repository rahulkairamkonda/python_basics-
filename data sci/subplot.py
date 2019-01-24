import numpy as np 
import matplotlib.pyplot as plt 

def f(t): 
    return np.exp(-t) * np.cos(2*np.pi*t) 

t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.axis([0, 6, 0, 150])

t1 = np.arange(0.0, 5.0, 0.1) 
t2 = np.arange(0.0, 5.0, 0.02) 
plt.figure(1) # Called implicitly but can use 
              # for multiple figures 
plt.subplot(211) # 2 rows, 1 column, 1st plot 
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k') 

plt.subplot(212) # 2 rows, 1 column, 2nd plot 
plt.plot(t2, np.cos(2*np.pi*t2), 'r--') plt.show() 
 plt.show() 