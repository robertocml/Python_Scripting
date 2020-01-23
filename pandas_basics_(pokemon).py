import pandas as pd

# This config is to show every column of the csv
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 15)

df = pd.read_csv('pokemon_data.csv')
# print(df.head(5))


# Read the headers...
# print(df.columns)

# Read specific column...
# print(df['Name'].head(5))

# Read random columns...
# print(df[['Name', 'Speed', 'Legendary']].head(5))

# Read each row... (in this case row 0)
# print(df.iloc[0])

# Read multiple rows... (in this case from 0 to 3)
# print(df.iloc[0:3])

# Read a specific location... (Row,Column)
# print(df.iloc[2, 1])

# Iterate through each row.. (in this case only printing the names)
# for index,row in df.iterrows():
#     print(index, row['Name'])

# loc used for finding spesific data that is NOT Integer based, is more text based
print(df.loc[df['Type 1'] == 'Fire'])