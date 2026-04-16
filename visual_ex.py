import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#matplotlib is used for data visualization
#It supports Line Plots, Bar Chart, Histogram, Scatter Plots, Sub Plots, Custom Stlying

#Example 1
# x = [1,2,3,4] #plan graph
# y = [10,20,25,30]
# plt.plot(x,y)
# #plt.plot(x,y,color='blue',linestyle='--')
# plt.plot(x,y,color='blue',marker='o',linestyle='dashed')
# plt.xlabel('Input Values')  #specify the x label
# plt.ylabel('Results') #specify the y label
# plt.title('Simple Linear Plot') # specify the title
# plt.show() # It will show the graph

#Example 2
# x = [1,2,3,4,5]
# y1 = [10,20,30,40,50]
# y2 = [15,25,35,20,55]
# plt.plot(x,y1,color='red',marker='o',label='plot1')
# plt.plot(x,y2,color='blue',marker='o',label='plot2')
# plt.xlabel('Input Values')
# plt.ylabel('Output Values')
# plt.title('Mutiple plots')
# plt.legend(loc='upper left')
# plt.show()

# Example 3
# students = ['A','B','C','D','E','F','G','H']
# study_hours = [2,3,5,6,8,1,4,7]
# marks = [40,50,65,70,90,35,60,80]
#
# colors =[]
#
# for m in marks:
#     if m >= 75:
#         colors.append('green')
#     elif m >= 50:
#         colors.append('blue')
#     else:
#         colors.append('red')
#
# plt.title("Student Performance Analysis")
# plt.xlabel("Student Hours")
# plt.ylabel("Marks")
# plt.scatter(study_hours,marks,color=colors)
#
# for i in range(len(students)):
#     plt.text(study_hours[i],marks[i],students[i])
#    # plt.text(students[i])
#
# plt.grid(True)
# plt.show()

#Example 4
#Bar Chart
# months = ["jan","feb","mar","apr","may","jun"]
# sales = [20000,25000,18000,30000,28000,22000]
# max_sale = max(sales)
# min_sale = min(sales)
#
# colors = []






#Example 5
# marks = [35,40,45,50,55,60,65,60,75,80,85,90,9560,70,80,55,65,75]
# plt.figure(figsize=(8,5))
# plt.hist(marks, bins=5,edgecolor='black')
# plt.title('Students Marks')
# plt.xlabel('Marks Range')
# plt.ylabel('Number of Students')
#
# mean = np.mean(marks)
# plt.axvline(mean,linestyle='--')
# plt.grid(True)
# plt.show()

#Example - 6
#Pie Chart
# categories = ["Rent","Food","Travel","shopping","Others"]
# expenses = [15000,6000,3000,4000,2000]
# max_index = expenses.index(max(expenses))
# colors = ['red','green','blue','yellow','orange']
#
# explode = [0] * len(expenses)
# explode[max_index] = 0.1
#
# plt.figure(figsize=(6,6))
# plt.pie(expenses,labels=categories,explode=explode,autopct='%1.1f%%',shadow=True,colors=colors)
# plt.title('Monthly Expenses Distribution')
# plt.show()

# Example - 7
# subplots (Dashboard)
df = pd.read_csv("students.csv")
fig, ax = plt.subplots(2,2,figsize=(10,8))

students = df["students"]
marks = df["marks"]
study_hours = df["study_hours"]
subjects=df["subjects"]
subject_marks = df["subject_marks"]

#graph1
valid1 =df[["students","marks"]].dropna()
ax[0,0].plot(valid1["students"],valid1["marks"],marker='o')
ax[0,0].set_title("Marks Trend")

#graph 2
valid2 =df[["students","subject_marks"]].dropna()
ax[0,1].bar(valid2["students"],valid2["subject_marks"])
ax[0,1].set_title("Subjectwise marks Trend")

#graph 3
valid3 =df[["study_hours","marks"]].dropna()
ax[1,0].scatter(valid3["study_hours"],valid3["marks"])
ax[1,0].set_title("study Hours vs marks")

#graph 4
valid4 =df["marks"].dropna()
ax[1,1].hist(valid4,bins=5)
ax[1,1].set_title("marks distribution")

plt.tight_layout()
plt.show()

