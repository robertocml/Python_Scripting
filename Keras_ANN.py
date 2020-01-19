import keras
from keras import backend as K
from keras.models import  Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy

#linear stack of layers, accept an array and within has elements , each one represent a layer
model = Sequential([
    Dense(16, input_shape=(1,), activation=relu),
    Dense(32, input_shape=(1,), activation=relu),
    Dense(2, input_shape=(1,), activation=softmax)
])