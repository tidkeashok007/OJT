import pandas as pd

# df = pd.read_csv('data.csv',
               #   dtype={'Age':int,'Salary':float},
               #   usecols=['Name','Age','Place'])

# print(df)
df = pd.read_csv('data.csv')
print(df)

df_cleaned_row = df.dropna(how="all")
print(df_cleaned_row)

df_cleaned_col = df.df_cleaned_row.dropna(axis=1, how="all")
print(df_cleaned_col)