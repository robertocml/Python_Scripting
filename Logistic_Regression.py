# OJO: Este código se hizo meramente como práctica, con la única finalidad de comprender la implementación del
# algoritmo usando sklearn y matplotlib
# La explicación detallada detras de las implementaciones de las librerias y el código original puedes
# encontrarlo aqui: https://www.youtube.com/watch?v=E8MoFjYITW8&feature=emb_logo

from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pandas as pd

# Generación del dataset ejemplo
x, y = make_classification(
    n_samples=100,
    n_features=1,
    n_classes=2,
    n_clusters_per_class=1,
    flip_y=0.03,
    n_informative=1,
    n_redundant=0,
    n_repeated=0
)

# Graficamos la información
plt.scatter(x, y, c=y, cmap='rainbow')
plt.title('Gráfica Regresión Logística')
plt.show()

# Generamos nuestros subsets de entrenamiento y testing

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

# Generamos un objeto de tipo regression logisitca y ajustamos nuestro modelo

regression = LogisticRegression()
regression.fit(x_train, y_train)

# Output de la regresion. ()
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
          penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
          verbose=0, warm_start=False)

# Vamos a revisar el coef e intercept..
print('-----------Coef e Intercept----------------')
print(regression.coef_)
print(regression.intercept_)

# Vamo a hacer las predicciones..
y_pred = regression.predict(x_test)

# Ahora vamos a checar el performance del modelo usando la matriz de confusión.
confMat = confusion_matrix(y_test, y_pred)

print('-----Matriz de Confusión-----')
print(confMat)