#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Numpy Array
#np.array([[1,4]])
#List arrays
#data=[[1,4],[2,5]]

import pandas as pd
import numpy as np

#creando un array
data= np.array([[1,4],[2,5],[3,6]])


#Creando un array
df = pd.DataFrame(data, index=['row', 'row2', 'row3'],
                   columns=['col1', 'col2'])

#Mostrando el dataframe
df

#Creando un array en forma de lista
data = [[1,4],[2,5],[3,6]]

#Creando un dataframe
df = pd.DataFrame(data, index=['row', 'row2', 'row3'],
                   columns=['col1', 'col2'])

df

#listas usadas para el ejemplo
states = ["Jaliscc","Nuevo Leon","CDMX","Oaxaca"]
population=[39613493,29730311,21944577,1929998]

#Almacenado listas en un diccionario
dict_states = {'States': states,'Population':population}

#creando el dataframe
df_population = pd.DataFrame(dict_states)

df_population

#leyendo el archivo csv
df_exams = pd.read_csv('C:/actividad/StudentsPerformance.csv')

#Mostrando el dataframe
df_exams

import pandas as pd

#leyendo el archivo csv
df_exams = pd.read_csv('C:/actividad/StudentsPerformance.csv')

df_exams.head()

#mostrar ultimas 5 filas del dataframe
df_exams.tail()

#mostrar ultimas n filas del dataframe
df_exams.tail(10)

#accediendo al atributo shape
df_exams.shape

#mostrar "n" filas
pd.set_option('display.max_rows',1000)
df_exams

