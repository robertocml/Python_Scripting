import matplotlib as plt
from sklearn import datasets
from sklearn import svm
import pandas as pd
import pickle
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


data = pd.read_csv('wineq.csv')

#Dejamos todos los datos como flotantes
#y rellenamos los Nulls con 0.0
data = data.astype(float).fillna(0.0)

#es la columa de nuestro dataset 'Quality' (La clasificacion)
y = data.quality
#Definimos las caracteristicas para la clasificacion
X = data.drop('quality', axis=1)


#Imprimimos en consola la clasificacion
print(data['quality'].value_counts())

#Creamos los X y Y train y test sets
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)


#Estandarizamos los valores de nuestro dataset para que se manejen en una misma escala
#Esto para que los clasificadores trabajen mejor
sc = StandardScaler()

X_train_array = sc.fit_transform(X_train.values)
X_train = pd.DataFrame(X_train_array, index = X_train.index, columns = X_train.columns)
X_test_array = sc.fit_transform(X_test.values)
X_test = pd.DataFrame(X_test_array, index = X_test.index, columns = X_test.columns)

#Ahora asi empezamos a trabajar con SVC
clf = SVC(kernel='rbf').fit(X_train,y_train)        

#verificamos que tan bien se comporta el clasificador
print(clf.score(X_test,y_test))


