#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Numpy Array
#np.array([[1,4]])
#List arrays
#data=[[1,4],[2,5]]


# In[7]:


import pandas as pd
import numpy as np


# In[12]:


#creando un array
data= np.array([[1,4],[2,5],[3,6]])


# In[13]:


#Creando un array
df = pd.DataFrame(data, index=['row', 'row2', 'row3'],
                   columns=['col1', 'col2'])


# In[14]:


#Mostrando el dataframe
df


# In[15]:


#Creando un array en forma de lista
data = [[1,4],[2,5],[3,6]]


# In[16]:


#Creando un dataframe
df = pd.DataFrame(data, index=['row', 'row2', 'row3'],
                   columns=['col1', 'col2'])


# In[17]:


df


# In[18]:


#listas usadas para el ejemplo
states = ["Jaliscc","Nuevo Leon","CDMX","Oaxaca"]
population=[39613493,29730311,21944577,1929998]


# In[19]:


#Almacenado listas en un diccionario
dict_states = {'States': states,'Population':population}


# In[20]:


#creando el dataframe
df_population = pd.DataFrame(dict_states)


# In[21]:


df_population


# In[28]:


#leyendo el archivo csv
df_exams = pd.read_csv('C:/actividad/StudentsPerformance.csv')


# In[29]:


#Mostrando el dataframe
df_exams


# In[30]:


import pandas as pd


# In[31]:


#leyendo el archivo csv
df_exams = pd.read_csv('C:/actividad/StudentsPerformance.csv')


# In[32]:


df_exams.head()


# In[33]:


#mostrar ultimas 5 filas del dataframe
df_exams.tail()


# In[34]:


#mostrar ultimas n filas del dataframe
df_exams.tail(10)


# In[35]:


#accediendo al atributo shape
df_exams.shape


# In[36]:


#mostrar "n" filas
pd.set_option('display.max_rows',1000)
df_exams


# In[ ]:




