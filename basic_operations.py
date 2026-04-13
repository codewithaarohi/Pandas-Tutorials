import pandas as pd

df = pd.read_csv('dataset/career_choices_2026.csv')

#print(df['Preferred_Career_2026'])

#print(df[['Preferred_Career_2026','Age']])

#Slicing - 2 ways ( loc and iloc)
# loc

#print(df.loc[0:5,["Preferred_Career_2026","Age"]])

#print(df.iloc[0:5,[2,5]])

print(df.iloc[0:5,2:5])

print(df.iloc[:,2:5]) # : means all rows

print(df.loc[:,["Preferred_Career_2026","Age"]])
