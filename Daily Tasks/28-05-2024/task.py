import pandas as pd

# Step 1: Convert the CSV file into a DataFrame
df = pd.read_csv("air-pollution.csv", header=None)
df.columns = ["Country", "Country Code", "Year", "Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7", "Column8"]

# Step 2: Create a filter based on the country
country_filter = df["Country"] == "Botswana"

# Step 3: Calculate median, mean, and standard deviation for each numeric column grouped by country
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
summary_df = df[country_filter].groupby("Country")[numeric_cols].agg(['median', 'mean', 'std'])

# Step 4: Delete the repeated entries
df.drop_duplicates(inplace=True)

# Step 5: Replace null values with 0
df.fillna(0, inplace=True)

# Displaying the summary DataFrame
print(summary_df)
