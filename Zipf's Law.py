#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
import matplotlib.pyplot as plt 
import numpy as np

fp = open('Alice.txt','r',encoding='UTF-8')
line = fp.readline()
my_dict = {}

while line:
    s = line.split()
    for x in s:
        if x not in my_dict:
             my_dict[x] = 1
        else:
             my_dict[x] += 1
    line = fp.readline()
    
fp.close()

num = []

for key in my_dict:
    num.append(my_dict[key])

print(len(num))
num.sort()
num.reverse()


lognum=np.log(num)
a=plt.hist(lognum,bins=20)


dx=(a[1][1]-a[1][0])
bin_center=np.array(a[1][0:-1])+dx/2


from scipy import optimize
def test_func(x,amp,alpha):
    return amp*x**alpha

params,params_covariance=optimize.curve_fit(test_func,bin_center,a[0])
plt.plot(bin_center,test_func(bin_center,params[0],params[1]),'r*',label='Fitted Function')
print(params[0],params[1])
plt.show()


#plt.loglog(range(len(num)),num)
plt.xlabel('Rank of the word')
plt.ylabel('Number of the occurance')
plt.show()

