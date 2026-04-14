import numpy as np
import matplotlib.pyplot as plt

#Example 5 pipechat

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
categories = ["Rent","Food","Travel","shopping","Others"]
expenses = [15000,6000,3000,4000,2000]
max_index = expenses.index(max(expenses))
colors = ['red','green','blue','yellow','orange']

explode = [0] * len(expenses)
explode[max_index] = 0.1

plt.figure(figsize=(6,6))
plt.pie(expenses,labels=categories,explode=explode,autopct='%1.1f%%',shadow=True,colors=colors)
plt.title('Monthly Expenses Distribution')
plt.show()