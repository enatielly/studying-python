import pandas as pd
csv_path = '/home/enatielly/workspace/studying-python/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)
df.head()

# Access to the column Length
x = df[['Length']]
x

# Get the column as a series
x = df['Length']
x

# Get the column as a dataframe
x = type(df[['Artist']])
x


# Access to multiple columns
y = df[['Artist','Length','Genre']]
y

# Access the value on the first row and the first column
df.iloc[0, 0]

# Access the value on the second row and the first column
df.iloc[1,0]

# Access the value on the first row and the third column
df.iloc[0,2]

# Access the column using the name
df.loc[1, 'Artist']

# Access the column using the name
df.loc[1, 'Artist']

# Access the column using the name
df.loc[0, 'Released']

# Access the column using the name
df.loc[1, 'Released']

# Slicing the dataframe
df.iloc[0:2, 0:3]

# Slicing the dataframe using name
df.loc[0:2, 'Artist':'Released']

# Use a variable q to store the column Rating as a dataframe
q=df[['Rating']]
q

#Assign the variable q to the dataframe that is made up of the column Released and Artist:
q=df[['Released','Artist']]
q

#Access the 2nd row and the 3rd column of df:
df.iloc[1,2]

#Use the following list to convert the dataframe index df to 
# characters and assign it to df_new; find the element corresponding to
# the row index a and column 'Artist'. Then select the rows a through d for the column 'Artist'
new_index=['a','b','c','d','e','f','g','h']
df_new=df
df_new.index=new_index
df_new.loc['a','Artist']
df_new.loc['a':'d','Artist']

