import pandas as pd
import numpy as np
from sklearn.model_selection import LeaveOneOut
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load our data
df = pd.read_csv("housing_price.csv")

# Split the dataset into feature and target as (x) and (y) axis
x = df[['size', 'bedrooms']].values
y = df['price'].values

# Initiate or define our model
model = LinearRegression()

# Define our cross-validation method which is LeaveOneOut
loo = LeaveOneOut()
mae_scores = []

for train_index, test_index in loo.split(x):
    x_train, x_test = x[train_index], x[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # Train the model with the set obtained after looping
    model.fit(x_train, y_train)

    # Predict the test set
    y_pred = model.predict(x_test)

    mae = mean_absolute_error(y_test, y_pred)
    mae_scores.append(mae)

average_mae = np.mean(mae_scores)
print(f"Average Mean Absolute Error (Leave-One-Out): {average_mae}")
