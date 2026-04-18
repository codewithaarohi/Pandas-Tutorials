import pandas as pd

df = pd.read_csv('dataset.csv')
#print(df)

#print(df.isna())
#print(df.isna().sum())

#print(df.isna().sum() / len(df) *100)


df['Product'] = df['Product'].fillna('Unknown')
#print(df)

df['Price'] = df['Price'].fillna(df['Price'].mean())
#print(df)

df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())
#print(df)

df['Discount'] = df['Discount'].fillna(0)
print(df)