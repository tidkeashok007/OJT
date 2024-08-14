#mnist dataset
#import the libraries
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, MaxPooling2D, Conv2D
from tensorflow.keras.utils import to_categorical
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#load the MNIST DATASET
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#normalize the dataset
x_train = x_train / 255.0
x_test = x_test / 255.0

#reshape the data for CNN
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

#one-hot encode the labels
#pass the images into 28*28 for the 1D vector
y_train_oh = to_categorical(y_train,10)
y_test_oh = to_categorical(y_test,10)

#build an ANN Model

ann_model = Sequential([
(Flatten(input_shape=(28,28))) ,


#first hidden layer
Dense(128, activation='relu'),

#second hidden layer
Dense(64, activation='relu'),

Dense(10, activation='softmax'),
])
#compile the model
ann_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#train ANN model
ann_model.fit(x_train, y_train_oh, epochs=5, batch_size=32, validation_data=(x_test, y_test_oh))












from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Build the CNN model
cnn_model = Sequential([
    # First convolutional layer
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    # Pooling layer
    MaxPooling2D((2, 2)),
    
    # Second convolutional layer
    Conv2D(64, (3, 3), activation='relu'),
    # Pooling layer
    MaxPooling2D((2, 2)),
    
    # Flatten layer
    Flatten(),
    # Fully connected layer
    Dense(64, activation='relu'),
    # Output layer
    Dense(10, activation='softmax'),
])

# Compile the model
cnn_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
cnn_model.fit(x_train, y_train_oh, epochs=5, batch_size=32, validation_data=(x_test, y_test_oh))







#Build the model with KNN
x_train_knn = x_train.reshape(-1,28*28)
x_test_knn = x_test.reshape(-1, 28*28)

#standardisation of the data
scaler = StandardScaler()
x_train_knn = scaler.fit_transform(x_train_knn)
x_test_knn = scaler.transform(x_test_knn)

#create model
knn_model = KNeighborsClassifier(n_neighbors=3)

#train the model
knn_model.fit(x_train_knn, y_train)

# Evaluate the model
knn_accuracy = knn_model.score(x_test_knn, y_test)

print(f"KNN Accuracy: {knn_accuracy*100:.2f}%")