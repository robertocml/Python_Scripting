import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
np.random.seed(0)

# Cargamos del dataset de ejemplo 
iris = load_iris()
# Creamos un df con la informacion
df = pd.DataFrame(iris.data, columns=iris.feature_names)
# Checamos los primeras filas para ver que esta en orden
#print(df.head())

#Ahora vamos a añadir una nueva columna de "Especies al df"
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Veamoslo de nuevo..
#print(df.head())

# Creamos un train set del 75% aprox y un test set del 25%
train,test = train_test_split(df, test_size=0.2)
# print("len of train set:", len(train))
# print("len of test set", len(test))

# Ahora hagamos una lista con los features para usarla mas adelante..
features = df.columns[:4]
print(features)