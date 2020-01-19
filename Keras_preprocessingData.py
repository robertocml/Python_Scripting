import numpy as np
from random import randint
from sklearn.preprocessing import MinMaxScaler


train_labels = []
train_samples = []

 #Datos para este caso

'''
Datos de ejemplo:

- Un medicamento fue probado en individuos de 13 a 100 años
- La prueba incluia 2100 personas, la mitad por debajo de los 65 años
  y la otra mitad por encima de los 65 años
- 95% de los pacientes mayores de 65 años, tuvieron efectos secundarios
- 95% de los pacientes menores de 65 años NO tuvieron efectos secundarios
'''
# 0 si no presentaron efectos secundarios y 1 si presentaron efectos secundarios
for i in range(1000):
    rand_joven = randint(13,64)
    train_samples.append(rand_joven)
    train_labels.append(0)

    rand_viejo = randint(65,100)
    train_samples.append(rand_viejo)
    train_labels.append(1)


for i in range(50):
    rand_joven = randint(13,64)
    train_samples.append(rand_joven)
    train_labels.append(1)

    rand_viejo = randint(65,100)
    train_samples.append(rand_viejo)
    train_labels.append(0)

# for i in train_labels:
#     print(i)



#Keras solo trabaja con arreglos de numPy..
train_labels = np.array(train_labels)
train_samples = np.array(train_samples)


scaler = MinMaxScaler(feature_range=(0,1))
scaled_train_samples = scaler.fit_transform((train_samples).reshape(-1,1))

for i in scaled_train_samples:
    print(i)