#!/usr/bin/env python
# coding: utf-8

# In[39]:


# Use should be able to find the nth power of the x.(i.e x*x*x*x...n times)
# You must implement it using Class
# Sample Input:
# x: 10
# n: 2
# Sample Output:
# 100
class powerofx:
    def __init__(self,x,n):
        self.x=x
        self.n=n
    def power(self):
        print(self.x,self.n)
print()
a=powerofx(10*5,2)
print(a.x*a.n)


# In[47]:


class powerofx:
    def __init__(self,x,n):
        self.x=x*5
        self.n=n
    def power(self):
        print(x=10,n=2)
print()
a=powerofx(10,2)
print(a.x)
print(a.n)
print(a.x*a.n)


# In[ ]:




