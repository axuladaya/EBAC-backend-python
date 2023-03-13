#!/usr/bin/env python
# coding: utf-8

# # Formas de crear Tuplas

# In[1]:


my_tuple = ("Juan", "Pedro", 23.4,2023)
print(type(my_tuple))
print(my_tuple)


# #sin parentesis

# In[2]:


my_tuple = "Juan", "Pedro", 23.4,2023
print(type(my_tuple))
print(my_tuple)


# In[3]:


my_list = [12,13,14,15,16,17]
my_tuple = tuple(my_list)
print(type(my_tuple))
print(my_tuple)


# # Método SORT en tuplas

# In[11]:


my_tuple = (5,3,6,3,1,4,5,8)
my_sorted_tuple = (sorted(my_tuple))
my_sorted_tuple_2 = tuple(sorted(my_tuple))

print(type(my_tuple))
print(my_tuple)

print(type(my_sorted_tuple))
print(my_sorted_tuple)

print(type(my_sorted_tuple_2))
print(my_sorted_tuple_2)


# # Método All en tuplas

# In[12]:


my_tuple = (5,4,2,7,1,4)
print(all(my_tuple))


# In[13]:


my_tuple = (5,4,2,7,1,0)  #hay un cero
print(all(my_tuple))


# In[14]:


my_tuple = (5,4,2,7,1,"")  #hay un espacio vacio
print(all(my_tuple))


# #Sirve para validar que no falte algun elemento

# In[16]:


my_tuple = (5,4,2,7,1, None)  #hay un espacio vacio
print(all(my_tuple))


# # Metodo Any en tuplas
# 

# In[17]:


my_tuple = (5,4,2,7,1,4)
print(any(my_tuple))


# In[18]:


my_tuple = (5,4,2,0,1,4)
print(all(my_tuple))


# In[19]:


my_tuple = (0,0,0,0,0,0,1)
print(all(my_tuple))


# In[20]:


my_tuple = ("",None,False,0)
print(all(my_tuple))


# In[21]:


my_tuple = ("",None,False,0,5)
print(all(my_tuple))


# In[22]:


my_tuple = ("",None,False,0,45)
print(all(my_tuple))


# # Método LEN en tuplas

# In[24]:


my_tuple = (5,4,2,7,1,4)
print(len(my_tuple))


# In[26]:


my_tuple = (5,4,2,7,1,4)
print(type(my_tuple))
print(any(my_tuple))


# # Indexacion en tuplas

# In[28]:


my_tuple = (5,4,2,7,1,4)
print(type(my_tuple))
print(my_tuple)
print(my_tuple[3])


# In[29]:


#Sirve para ver en que posicion esta el valor


# In[30]:


my_tuple = (5,4,2,7,1,4)
print(type(my_tuple))
print(my_tuple)
print(my_tuple[3])
print(my_tuple[0])
print(my_tuple[-1])


# # Conversiones de tuplas

# # Cadena a Tupla

# In[31]:


my_string = "Backend Pyhton"
my_tuple = (tuple(my_string))

print(my_string)
print(my_tuple)


# # De lista a tupla

# In[32]:


my_list = ["python","javascript","java","scala","go"]
my_tuple = tuple(my_list)

print(my_list)
print(my_tuple)


# In[33]:


#la lista entre corchetes
#la tupla entre parentesis


# # De tupla a cadena

# In[37]:


my_tuple =('B', 'a', 'c', 'k', 'e', 'n', 'd', ' ', 'P', 'y', 'h', 't', 'o', 'n')
my_string = "".join(my_tuple)
print(my_tuple)
print(my_string)


# # De tupla a lista

# In[38]:


my_tuple =('python', 'javascript', 'java', 'scala', 'go')
my_list = list (my_tuple)
print(my_tuple)
print(my_list)


# In[ ]:




