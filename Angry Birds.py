#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import math
import random

v0=100
theta=0.5
g=9.8
a=2*v0*math.sin(theta)/g
b=2*v0*math.sin(theta)/g*v0*math.cos(theta)
t=np.arange(0,a,0.01)
x=v0*(np.cos(theta))*t
y=v0*(np.sin(theta))*t+1/2*(-g)*t**2
aa=int(a)
bb=int(b)
pigx=random.randint(0,bb)
pigy=random.randint(0,aa)
plt.plot(x,y)
plt.plot(pigx,pigy,"o")
print(pigx,pigy)

if pigx in x and pigy in y:
    print('HITS')
else:
    print('OH NO')


# In[3]:


pig_size = 3
y=x[x<pig_size]
print(y)
print(np.shape(y)[0])
if np.shape(y)[0]>0:
    print("HITS")

