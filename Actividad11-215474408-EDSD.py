#!/usr/bin/env python
# coding: utf-8

# #Erick David Sanchez Diaz
# #215474408
# #21 de Febrero del 2023
# #Actividad 11 Analitica de Datos 2023-A LTIN
# 

# Hello World
# 

# In[2]:


print("Hello world")


# Tipos de Datos

# Interger/Float
# 

# In[3]:


#La funcion type, nos permite saber el tipo de datos que estamos
#insertando dentro de la funion
type(2.3)


# Operaciones
# °Adicion:+
# °Substraccion:-
# °Multiplicacion:*
# °Division:/
# °Exponente:**
# °Residuo:%
# °Division entera://
# 

# In[5]:


1 + 2 


# In[6]:


5 - 2


# In[7]:


5*10


# In[8]:


100/2


# In[9]:


5**2


# In[10]:


50%2


# In[11]:


50.50//2


# Boolean
# Este tipo de dato determina la verdad o falso

# In[12]:


type(True)


# String (Cadena de Texto)

# In[13]:


#Este nos permite cambiar todas las letras a mayusculas
print("Hello World".upper())
#Este nos permite cambiar todas las letras a minusculas
print("Hello World".lower())
#Este nos permite cambiar las primeras letras de cada palabra
#a mayusculas
print("Hello World".title())

#Cuentas la cantidad de letras que insertamos en la funcion
print("Hello World".count('l'))

#Remplaza las letras dentro de la cadena de texto
print("Hello World".replace('o','u'))


# Variables

# In[15]:


#Le asignamos un objeto a la variable
message_1="Estoy aprendiendo Python"


# In[16]:


#En este caso, llamamos a la variable sin necesidad de utilizar
#el print
message_1 


# In[26]:


message_2="y es divertido!"


# In[28]:


message_2


# In[29]:


#Estamos concatenando dos variables junto con un espacio en blanco
message_1 + " " + message_2


# In[34]:


#Se asginan las dos variables a una sola
message = f'{message_1}{message_2}'
message


# Listas

# In[36]:


#Le asignamos objetos a la lista
countries = ['United States','India', 'China', 'Brazil']


# In[37]:


#Imprimimos los valores de la lista
countries


# In[38]:


#Imprimimos el objeto que se encuentra en la posicion 0 de la lista
countries[0]


# In[39]:


#Imprimimos el objeto que se encuentra en la posicion 1 de la lista
countries[1]


# In[40]:


#Imprimimos el objeto que se encuentra en la posicion 2 de la lista
countries[2]


# In[41]:


#Imprimimos el objeto que se encuentra en la posicion 3 de la lista
countries[3]


# In[42]:


#Se imprime el valor -1 en este caso es el ultimo
countries[-1]


# Rebanada/Slicing

# In[43]:


countries


# In[44]:


#Se imprime un rango de objetos de la lista
countries[0:3]


# In[45]:


#Se imprimen los valores de la posicion 1 a infinita
countries[1:]


# In[46]:


#Se imprimen los valores de la posicion 2 a la 0
countries[:2]


# Operaciones y Metodos

# In[47]:


countries


# In[49]:


#Se añade a la cola de la lista un objeto
countries.append('Canada')


# In[50]:


countries


# In[51]:


#Se añade un objeto al inicio de la lista
countries.insert(0,'Argentina')


# In[52]:


countries


# In[53]:


countries_2= ['UK','Alemania','Australia']


# In[54]:


#Concatenamos las dos listas
countries + countries_2


# In[56]:


#Asignamos las dos listas a una sola variable
nueva_lista=[countries,countries_2]


# In[57]:


nueva_lista


# Eliminar Elementos

# In[58]:


#Eliminas un valor de la lista mensionado en la funcion
countries.remove('Canada')


# In[59]:


countries


# In[60]:


#Se dropea el valor 0 de la lista
countries.pop(0)


# In[61]:


countries


# In[62]:


#Eliminamos el valor en la posicion 0
del countries[0]


# In[63]:


countries


# Ordenar una Lista

# In[70]:


numbers=[5,7,4,6,8]


# In[71]:


numbers


# In[72]:


#Se ordenas los valores del menor al mayor
numbers.sort()


# In[73]:


numbers


# In[74]:


#Se ordenan los valores de reversa del mayor al menor
numbers.sort(reverse=True)


# In[75]:


numbers


# In[77]:


#Añadimos un valor en la posicion 0 de la lista, al incio
numbers[0]= 1000


# In[78]:


numbers


# Copiar una lista

# In[79]:


countries.append('Argentina')


# In[80]:


countries


# In[81]:


nueva_lista_3= countries


# In[82]:


nueva_lista_3


# In[83]:


nueva_lista=countries.copy()


# In[84]:


nueva_lista


# In[87]:


nueva_lista_2=countries[:]


# In[88]:


nueva_lista_2


# Diccionarios

# In[90]:


#Creamos el diccionario
mi_diccionario = {'key1':'value1','key2':'value2'}


# In[91]:


#Le asigamos valores al diccionario
my_data = {'nombre':'erick','edad':23}


# In[92]:


#Impimimos los valores del diccionari
my_data


# In[93]:


#Imprimimos un valor en especifico
my_data['nombre']


# In[94]:


#Imprimimos las llaves o los nombre de los datos
my_data.keys()


# In[95]:


#Imprimimos los valores del diccionario
my_data.values()


# In[96]:


#Imprimimos los valores con cada uno de sus llaves
my_data.items()


# Agregar/Actualizar elementos

# In[100]:


my_data={'nombre':'Erick','edad':26}


# In[102]:


my_data['estatura']=1.75


# In[103]:


my_data


# In[115]:


#Le implementamos dos elementos mas al diccionario seleccionado
my_data.update({'estatura':1.9, ' lenguages':['Ingles','Español']})


# In[116]:


my_data


# Copiar Diccionario

# In[117]:


#Copiamos el diccionario a otro diccionario para copiar
nuevo_diccionario= my_data.copy()


# In[118]:


nuevo_diccionario


# Eliminar Elementos

# In[119]:


my_data


# In[120]:


#Se borra el dato mencionado en la funcion
my_data.pop('estatura')


# In[124]:


my_data


# In[128]:


#Eliminar un dato en especifico
del my_data[' lenguages']


# In[129]:


my_data


# In[130]:


#Borrar todo el contenido del diccionario
my_data.clear()


# In[131]:


my_data


# Condicional If
# Sirve para darle una condicional a una funcion, como en este caso es determinar si tu edad es mayor a ciertas edad, es lo que se imprime, realizar ciertas restricciones

# In[132]:


edad=24


# In[134]:


if edad>=18:
    print("Eres mayor de Edad")
elif edad>=13:
    print("Eres un adolecente")
else:
    print("Eres un niño")


# In[135]:


countries=['united states', 'India', 'China','Brazil']


# In[137]:


if "Colombia"in countries:
    print("Pais esta en la lista")
else:
    print("Pais NO esta en la lista")


# For loop(Bucle for)
# Sirve para la cracion de ciclos, se puede determinar cuantas veces se puede realizar cierto ciclo con ciertas restricciones, junto tambien con una accion determinada en ella

# In[138]:


for pais in countries:
    print(pais)


# In[139]:


#Ciclo for con una condicion if
for pais in countries:
    if pais =="united states":
        print(pais)


# In[140]:


my_data={'nombre':'Erick','edad':23}


# In[141]:


my_data


# In[142]:


my_data.items()


# In[143]:


for key, value in my_data.items():
    print(key)
    print(value)


# Funciones pre-fabricadas

# In[144]:


countries


# In[145]:


#Contar la cantidad de objetos dentro de la lista
len(countries)


# In[146]:


#Numero maximo de la lista de numeros
max(16,83,31,1,10)


# In[147]:


#Muestra el minimo de la lista de numeros
min(16,83,31,1,10)


# In[148]:


#Tipo de dato de countries
type(countries)


# In[149]:


#tipo de dato de my_data
type(my_data)


# In[150]:


#Redondear a un determinado numero de decimales
round(2.333,2)


# In[151]:


#Imprimir numeros del 1 al 10 con aumento de 2 en 2
for i in range(1,10,2):
    print(i)


# Crear una funcion

# In[152]:


#Crear funciones la cual realiza la suma de dos numeros 
def sumar_numeros(a,b):
    suma_final = a+b
    return suma_final


# In[155]:


#Llamar a la funciones asignandole dos numeros para realizar la accion
sumar_numeros(6,4)


# Modulos
# Podemos acceder a un modulo usanod la palabra import

# Modulos OS

# In[156]:


#Importacion de libreria os
import os


# In[157]:


#Obtencion de direccion
os.getcwd()


# In[159]:


#Monstrar enlistado de lo que se encuentra en esa direccion
os.listdir()


# In[161]:


#Insertar una carpeta en esa direccion
os.makedirs("Nueva Carpeta")


# In[162]:


#Nos Aseguramos que se haya creado la carpeta
os.listdir()


# In[ ]:




