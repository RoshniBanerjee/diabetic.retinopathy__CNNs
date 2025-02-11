from time import time
import datetime
import os

import keras.backend as K
from keras.models import Sequential, Model
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, Dropout, Flatten, BatchNormalization
from keras.optimizers import Adam
from keras.callbacks import TensorBoard
K.image_data_format()

from sklearn.model_selection import train_test_split

'''
log_dir = os.path.join(
    "logs",
    "fit",
    datetime.datetime.now().strftime("%Y%m%d-%H%M%S"),
)
'''

def build_model():
    model = Sequential()

    model.add(Conv2D(32, (3,3), padding="same", activation='relu', input_shape=(512, 512, 1), data_format="channels_last"))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(padding="same"))

    model.add(Conv2D(32, (3,3), padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(padding="same"))

    model.add(Conv2D(64, (3,3), padding="same",activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(padding="same"))

    model.add(Conv2D(64, (3,3), padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(padding="same"))

    model.add(Conv2D(128, (3,3), padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(padding="same"))

    model.add(Conv2D(128, (3,3), padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(padding="same"))

    model.add(Conv2D(256, (3,3), padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(padding="same"))

    model.add(Conv2D(256, (3,3), padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(padding="same"))

    model.add(Conv2D(512, (3,3), padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(padding="same"))

    model.add(Conv2D(512, (3,3), padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(padding="same"))

    model.add(Dropout(0.20))

    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.20))

    model.add(Dense(1024, activation='relu'))

    model.add(Dense(4, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    #tensorboard = TensorBoard(log_dir="logs/{}".format(time()))
    tensorboard = TensorBoard(log_dir=os.path.join(
        "logs",
        datetime.datetime.now().strftime("%Y%m%d-%H%M%S"),
    ))

    return model, tensorboard
