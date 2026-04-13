import pandas as pd

df = pd.read_csv('dataset/career_choices_2026.csv')

#print(df.head(2)) # 5 records

#print(df.tail(2)) #5

#print(df.shape) # (200, 7)

#print(df.columns)

print(df.info())