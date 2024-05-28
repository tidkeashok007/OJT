# dataframes is two dimentional which is in a tabular format.
import pandas as pd

# create a dataframe with a dictionary
data = {
     'Name':['kigini','tuttu','ikka'],
     'Age': [24,23,24],
     'Place': ['koovode','mavoor','punoor']
}

# convert the data into dataframes
df = pd.DataFrame(data)

# print(df)
# print(df[['Name','Place']])

# for accessing each row from the dataframe we need to use the inbuilt function
# print(df.iloc[2])

print(df[df['Age']>23])