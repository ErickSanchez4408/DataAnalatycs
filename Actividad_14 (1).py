#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sanchez Diaz Erick David
#215474408
#Analitica de Datos 2023A


# In[5]:


#Atributos, Metodos y Funciones
#JAOT 1 de Marzo de 2023
import pandas as pd


# In[8]:


#reading the csv file
df_exams = pd.read_csv('C:/actividad/StudentsPerformance.csv')


# In[9]:


#mostrando el datframe
df_exams


# In[10]:


#obteniendo acceso al atriuto shape
df_exams.shape


# In[11]:


#obteniendo acceso al atributo index
df_exams.index


# In[12]:


#obteniendo acceso al atributo columns
df_exams.columns


# In[14]:


#tipo de dato de cada columna
df_exams.dtypes


# In[15]:


#mostrando las 5 primeras filas
df_exams.head()


# In[16]:


#mostrando informacion del dataframe
df_exams.info()


# In[17]:


#Obteniendo valores estadisiticos del DataFrame
df_exams.describe


# In[18]:


#Obentener el tamaño del DataFrame (Filas)
len(df_exams)


# In[19]:


#Obtener el maximo index
max(df_exams.index)


# In[20]:


#Obtener el minimo index
min(df_exams.index)


# In[21]:


#Obtener el tipo de dato
type(df_exams)


# In[22]:


#Redondear valores del DataFrame
round(df_exams, 2 )


# In[ ]:




