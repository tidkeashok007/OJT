# custom_loss.py
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Define a custom loss function
def custom_loss(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))

# Build a simple model
model = Sequential([
    Dense(10, activation='relu', input_shape=(10,)),
    Dense(1)
])

# Compile the model with custom loss
model.compile(optimizer=Adam(), loss=custom_loss)

# Save the model
model.save('custom_loss_model.h5')
