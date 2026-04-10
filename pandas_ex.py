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
# df = pd.read_csv("pandas_nulls.csv")
# print(df.isnull())
# print(df.notnull())
# print(df.dropna())
# print(df.fillna(0))

#Ex 9
# df = pd.read_csv("student_data.csv")
# print(df.sort_values("Marks", ascending=False))

#Ex 10
# data = {
#     "Dept" : ["IT","IT","HR","HR"],
#     "Salary" : [50000,60000,45000,40000]
# }
# df = pd.DataFrame(data)
# print(df.groupby("Dept")["Salary"].sum())
# print(df.groupby("Dept")["Salary"].mean())
# print(df.groupby("Dept")["Salary"].median())
# print(df.groupby("Dept")["Salary"].min())
# print(df.groupby("Dept")["Salary"].max())
# print(df.groupby("Dept")["Salary"].std())
# print(df.groupby("Dept")["Salary"].describe())

#Ex 11
# df1 = pd.DataFrame({
#     "ID" : [101,102],
#     "Name" : ["std1","std2"]
# })
# df2 = pd.DataFrame({
#     "ID" : [103,104],
#     "Marks" : [90,95]
# })
# print(pd.merge(df1,df2,on="ID"))

# Ex 12
# df = pd.read_csv("student_data.csv")
# print(df.head())
# df["Age"] = df["Age"].apply(lambda x: x+10)
# print(df)

#Ex 13
# df = pd.read_csv("students.csv")
# print(df.value_counts("Marks"))
# df.describe()

#Ex 14
data = {
    "Name" : ["Ravi","Sita","Jhon","Ravi"],
    "Dept" : ["IT","HR","IT","IT"],
    "Marks" :[85,90,None,85]
}
df = pd.DataFrame(data)
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print(df.drop_duplicates().groupby("Dept")["Marks"].mean())


