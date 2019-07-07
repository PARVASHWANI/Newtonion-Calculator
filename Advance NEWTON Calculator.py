#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests,json


# In[17]:


print('List of Operations(!LowerCase!):-')
print()
print("'simplify' - Simplify")
print("'factor' - Factor")
print("'derive' - Derive")
print("'integrate' - Integrate")
print("'zeroes' - Find 0's")
print("'tangent' - Find Tangent")
print("'area' - Area Under Curve")
print("'cos' - Cosine")
print("'sin' - Sine")
print("'tan' - Tangent")
print("'arccos' - Inverse Cosine")
print("'arcsin' - Inverse Sine")
print("'arctan' - Inverse Tangent")
print("'abs' - Absolute Value")
print("'log' - Logarithm")
print("*****************************")


# In[24]:


baseurl = "https://newton.now.sh/"
op = input("Enter The Operation From The Above Given List(lowercase):")
eq = input("Enter The Expression :-")
complete_url = baseurl + op + '/' + eq


# In[25]:


complete_url


# In[26]:


response = requests.get(complete_url)


# In[27]:


data  = response.json()


# In[28]:


print("Appplying The Operation",data['operation'],"on Expression","'",data['expression'],"'")


# In[30]:


print("Answer:",data["result"])


# In[ ]:
input()
