import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Debug: Print the current working directory
print("Current working directory:", os.getcwd())

# Step 1: Load the data
file_path = "weather_data.csv"  # Adjusted to the correct path

# Verify file path before reading
if not os.path.isfile(file_path):
    print(f"File not found: {file_path}")
else:
    data = pd.read_csv(file_path)

    # Step 2: Clean and preprocess the data
    # Remove rows with missing values
    data = data.dropna()

    # Convert the Date column to datetime type with flexible format handling
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

    # Drop rows where Date conversion failed
    data = data.dropna(subset=['Date'])

    # Step 3: Calculate statistics for the temperature
    temperature = data['Temperature']
    mean_temp = np.mean(temperature)
    std_temp = np.std(temperature)
    max_temp = np.max(temperature)
    min_temp = np.min(temperature)

    print(f"Mean Temperature: {mean_temp:.2f} °C")
    print(f"Standard Deviation of Temperature: {std_temp:.2f} °C")
    print(f"Maximum Temperature: {max_temp:.2f} °C")
    print(f"Minimum Temperature: {min_temp:.2f} °C")

    # Step 4: Generate visualizations

    # Time series plot for the temperature trend
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Temperature'], label='Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Trend Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Bar chart for average monthly precipitation
    data['Month'] = data['Date'].dt.to_period('M')
    monthly_precipitation = data.groupby('Month')['Precipitation'].mean()

    plt.figure(figsize=(12, 6))
    monthly_precipitation.plot(kind='bar', color='skyblue')
    plt.xlabel('Month')
    plt.ylabel('Average Precipitation (mm)')
    plt.title('Average Monthly Precipitation')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

    # Scatter plot for the relationship between wind speed and temperature
    plt.figure(figsize=(12, 6))
    plt.scatter(data['WindSpeed'], data['Temperature'], alpha=0.5)
    plt.xlabel('Wind Speed (km/h)')
    plt.ylabel('Temperature (°C)')
    plt.title('Relationship Between Wind Speed and Temperature')
    plt.grid(True)
    plt.show()
