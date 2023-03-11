#Regresion Lineal Simple Modelo de Entrenamiento
#Sanchez Diaz Erick David
#EDSD
#Analitica de Datos LTIN 2023-A

#Importar librerias numpy, matploitlib y pandas

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el Data Set
dataset = pd.read_csv('D:/DataSet/Salary_Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 1].values

# Dividir el data set en conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

#Crear modelo de Regresion Lineal Simple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, Y_train)

#Predecir el conjunto de test
Y_pred = regression.predict(X_test)

#Visualizar los resultados de entrenamiento
#Se le esta implementando las caracteristicas de como queremos visualizar
#el grafico
plt.scatter(X_train, Y_train, color = "red")
plt.plot(X_train, regression.predict(X_train), color = "blue")
plt.title("Sueldo vs Años de Experiencia (Conjunto de Testing")
plt.xlabel("Años de Experiencia")
plt.ylabel("Sueldo (en $)")
plt.show()

#Visualizar los resultados de test
#Se le esta implementando las caracteristicas de como queremos visualizar
#el grafico
plt.scatter(X_test, y_test, color = "red")
plt.plot(X_train, regression.predict(X_train), color = "blue")
plt.title("Sueldo vs Años de Experiencia (Conjunto de Testing)")
plt.xlabel("Años de Experiencia")
plt.ylabel("Sueldo (en $)")
plt.show()






