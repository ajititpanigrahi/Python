import numpy as np
import pandas as pd

#Ex 1
# data = [10,20,30,40,50]
# res= pd.Series(data)
# print(res)

#Ex 2
# data = {
#         "Name": ["std1", "std2", "std3","std4"],
#         "Marks": [60,70,80,90],
# }
# res = pd.DataFrame(data)
# print(res)

#Ex 3
# df = pd.read_csv('student_data.csv')
# print(df)
# print(df.head()) # display first 5 records
# print(df.tail()) # display last 5 records
# print(df.describe()) #statistics
# print(df.shape) #rows , columns
# print(df.columns) #columns
# print(df.index)
# print(df.values) #display column names
# print(df.info()) #structure

#Ex 4
#df = pd.read_csv('student_data.csv')
# print(df["Name"]) #display Name column
# print(df[["Name","Age"]]) # display Name and Age column
# print(df[df["Age"]]>20)
# print(df[((df["Age"]>20) & (df["Age"]<25) )])

#Ex 4
# df = pd.read_csv('student_data.csv')
# print(df.loc[0]) #display 0th row
# print(df.loc[0:2]) # display 0,1,2 rows (3 rows)
# print(df.loc[[0,2,4]])

#Ex 6
# data = {
#         "Name": ["std1", "std2", "std3","std4"],
#         "Marks": [60,70,80,90],
# }
# res = pd.DataFrame(data)
# print(res.iloc[0]) # 0th row
# print(res.iloc[0:2]) # 0th will include 2nd will exclude
# print(res.iloc[[0,2]]) # multiple rows
#
# print(res.iloc[0,1]) # only number supported by iloc
# print(res.loc[0,"Marks"]) # both number and label supported by loc

#Ex 7
# data = {
#         "Name": ["std1", "std2", "std3","std4"],
#         "Marks": [60,70,80,90],
# }
# res = pd.DataFrame(data)
# res["Grade"]=["A","B","C","D"] # newly adding one more column
# res["Marks"]=res["Marks"] + 10 # Marks column increased by 10
# print(res)

#Ex 8
df = pd.read_csv("pandas_nulls.csv")
print(df.isnull())
print(df.notnull())
print(df.dropna())
print(df.fillna(0))


