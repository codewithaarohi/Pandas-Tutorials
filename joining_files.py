import pandas as pd

df1 = pd.read_csv('a.csv')
df2 = pd.read_csv('b.csv')

#print(df1.head(1))
#print(df2.head(1))

# concat function
#print(pd.concat([df1,df2], axis = 0)) #stack rows

#print(pd.concat([df1,df2], axis = 1)) #stack columns


# merge
# Data is related through a common column (joining two tables using a common ID)

'''
Types of Merge - 
pd.merge(df1, df2, on="Student_ID", how="inner")   # common only
pd.merge(df1, df2, on="Student_ID", how="left")    # all from left
pd.merge(df1, df2, on="Student_ID", how="right")   # all from right
pd.merge(df1, df2, on="Student_ID", how="outer")   # everything
'''

df_inner_join = pd.merge(df1, df2, on="Student_ID", how="inner") 
#df_inner_join.to_csv('df_inner_join_data.csv', index=False)


df_left_join = pd.merge(df1, df2, on="Student_ID", how="left") 
df_left_join.to_csv('df_left_join_data.csv', index=False)



df_left_join = pd.merge(df1, df2, on="Student_ID", how="right") 
df_left_join.to_csv('df_left_join_data.csv', index=False)

df_left_join = pd.merge(df1, df2, on="Student_ID", how="outer") 
df_left_join.to_csv('df_left_join_data.csv', index=False)