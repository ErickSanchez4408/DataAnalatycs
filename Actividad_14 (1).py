#!/usr/bin/env python
# coding: utf-8

#Sanchez Diaz Erick David
#215474408
#Analitica de Datos 2023A

#Atributos, Metodos y Funciones
#JAOT 1 de Marzo de 2023
import pandas as pd


#reading the csv file
df_exams = pd.read_csv('C:/actividad/StudentsPerformance.csv')


#mostrando el datframe
df_exams

#obteniendo acceso al atriuto shape
df_exams.shape

#obteniendo acceso al atributo index
df_exams.index

#obteniendo acceso al atributo columns
df_exams.columns

#tipo de dato de cada columna
df_exams.dtypes

#mostrando las 5 primeras filas
df_exams.head()


#mostrando informacion del dataframe
df_exams.info()

#Obteniendo valores estadisiticos del DataFrame
df_exams.describe

#Obentener el tamaño del DataFrame (Filas)
len(df_exams)


#Obtener el maximo index
max(df_exams.index)

#Obtener el minimo index
min(df_exams.index)


#Obtener el tipo de dato
type(df_exams)


#Redondear valores del DataFrame
round(df_exams, 2 )

