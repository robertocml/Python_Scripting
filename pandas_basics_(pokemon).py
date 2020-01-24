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

# loc used for finding specific data that is NOT Integer based, is more text based
# print(df.loc[df['Type 1'] == 'Fire'])

# It gives a buch of (sometimes) useful information
# print(df.describe())

# Sorting the pokemons by alphabetical orden.. from z to a (because asc = False) and by attack power from low to high
# print(df.sort_values(['Name', 'Attack'], ascending=[1, 0]))

# Now lets add a new column of Total... which is the sum of all culmuns...
# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# print(df.head(5))

# Now just let drop that Total column...
# df = df.drop(columns=['Total'])
# print(df)

# Now let's add the total column again but in a different way...
# df['Total'] = df.iloc[:, 4:10].sum(axis=1)
# print(df.head(5))

# Now lets put the total next to the name...
# cols = list(df.columns)
# df = df[cols[0:2] + [cols[-1]] + cols[2:12]]

# print(df.head(5))

# So now lets export this modified version of the csv...
# df.to_csv('Pokemon(modified).csv', index=False)

# So now lets do some filtering data...
# Lets first filter by [Type 1] = Grass
# print(df[df['Type 1'] == 'Grass'])
# print("total grass pokes = ",df[df['Type 1'] == 'Grass'].shape[0])

