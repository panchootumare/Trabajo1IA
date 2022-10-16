import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv(r"C:/Users/panch/OneDrive/Escritorio/Trabajos/Trabajo1IA/Trabajo 1/data1.txt", delimiter=',', header= None)
x = []
y = []
for i in datos[0]:
    x.append(i)
for j in datos[1]:
    y.append(j)


plt.scatter(x,y, color = 'red', marker='x')
plt.title("Diagrama de dispersión de datos de entrenamiento")
plt.xlabel("Población de la ciudad en 10.000s")
plt.ylabel("Beneficio en $10.000s")
plt.show()
