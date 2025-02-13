import tensorflow as tf
import tensorflow.keras as keras
import numpy as np

mnist = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


train_images = train_images / 255
test_images = test_images / 255

model = keras.Sequential ([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation = tf.nn.relu),
    keras.layers.Dense(10, activation = tf.nn.softmax)
])


model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy',
             metrics = ['accuracy'])

model.fit(train_images, train_labels, epochs = 5)


test_loss, test_acc = model.evaluate(test_images, test_labels)
print(test_acc)
