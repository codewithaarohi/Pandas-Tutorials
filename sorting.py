import pandas as pd

df = pd.read_csv('dataset/career_choices_2026.csv')

#print(df.sort_values("Expected_Salary_LPA",ascending=False))# descending order high to low  # True


#print(df.sort_values("Expected_Salary_LPA",ascending=True))


#print(df.sort_values("Expected_Salary_LPA")) # default value is ascending = True

print(df.sort_values("Expected_Salary_LPA",ascending=False).head(3))