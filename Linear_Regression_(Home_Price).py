import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LinearRegression 

#Implementacion sencilla de regresón lineal
#Para poder predecir el costo de una casa en base a su area

#importamos el csv como dataframe
df = pd.read_csv('home_prices.csv')


# Graficamos los datos antes de la regresion
# plt.title('Casas')
# plt.xlabel('Area (sqr ft)')
# plt.ylabel('Precio (Dlls)')
# plt.scatter(df.area,df.precio,color='red', marker='+')
# #plt.show()


# Separamos los datos en X y y

X = df.drop('precio',axis='columns')
y = df.precio

# Llamamos al metodo de regresion lineal de sklearn y ajustamos
reg = linear_model.LinearRegression()
reg.fit(X,y)

#predecimos una nueva instancia (Para una casa de 3300 sqr ft)
print(reg.predict([[3300]]))

# ------ Vamos a predecir todas los precios de areas.csv
#Creamos del df
df_areas = pd.read_csv('areas.csv')
#Y predecimos
predictions = reg.predict(df_areas)

#Le anexamos las predicciones como columna al df
df_areas['precio prediccion'] = predictions
print(df_areas)

#Y por ultimo convertimos ese nuevo df en un csv
df_areas.to_csv('Predicciones_(Home_Price).csv')

