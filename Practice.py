#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
import matplotlib.pyplot as plt

x = np.random.random(10)
print(x)


# In[26]:


plt.hist(x,10)

plt.xlabel("x value")
plt.ylabel("numbers of elements")
plt.show()


# In[27]:


mu,sigma = 0,0.1  #mean and standard deviation 
s = np.random.normal(mu,sigma,10000)
plt.hist(s,10)

#plt.xlim(-2,2)
plt.show()


# In[28]:


ss = plt.hist(s,10)
print(ss)


# In[35]:


bins = np.linspace(-0.5,0.5,21,endpoint=True)
print(bins)
plt.hist(s,bins)

#plt.xlim(-2,2)
plt.show()


# In[41]:


#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np 
import matplotlib.pyplot as plt
import math 

#SI unit
h = 6.26*10**-34 #Plank constant
c = 3*10**8      #speed of light
k = 1.38*10**-23 #Boltzman Constant JK^-1

num = 100 #total number of points

v = np.linspace(10**0, 10**15.5,100,endpoint = True)
print(v)

#T=float(input("Input temperaturet"))
T=5500
B = 2*h*v**3/c**2/(math.e**(h*v/k/T)-1)


#plt.xlim(10**11,10**15.2)
#plt.ylim(10**14,10**-6)
plt.plot(v,B,".")
#plt.loglog(v,B,'.')
plt.xlabel=("Frenqence (Hz)")
plt.ylabel=("Intenalty Watta/Hz/m^2")


dB = np.random.normal(0.,10**-8.5,num)
B += dB  #B=B+dB

plt.plot(v,B)
plt.show()

