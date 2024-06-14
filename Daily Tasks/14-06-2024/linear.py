import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dataset 
height = np.array([150, 160, 164, 165, 173]).reshape(-1, 1)
weight = np.array([50, 65, 63, 68, 72])

# Create a linear regression model
model = LinearRegression()

# Fit the model
model.fit(height, weight)

# Predict weights
predicted_weight = model.predict(height)

# Print intercept and coefficients
print(f"Intercept: {model.intercept_}")
print(f"Coefficient: {model.coef_[0]}")

# Create a scatter plot with the regression line
plt.scatter(height, weight, color='blue', label='Actual weights')
plt.plot(height, predicted_weight, color='red', label='Predicted weights')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Linear Regression')
plt.legend()
plt.savefig('linear_regression_plot.png')  # Save the plot
plt.show()  # Display the plot
