import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    "Student" : ["A","B","C","D","E","F","G","H","I","J"],
    "Studyhours" : [2,3,4,5,6,7,8,9,10,11],
    "Marks" : [35,40,50,55,65,70,75,89,90,95],
    "Gender":["Male","Feamle","Male","Feamle","Male","Feamle","Male","Feamle","Male","Feamle"],
     "Age" : [18,19,20,18,21,20,19,22,21,20]
}

print(data)
student_df = pd.DataFrame(data)
print(student_df)

sns.scatterplot(x="Studyhours", y="Marks", hue="Gender", data=student_df)
plt.title("Student Hours vs Marks")
plt.xlabel("Student Hours")
plt.ylabel("Student Marks")
plt.show()

df = sns.load_dataset("tips")
print(df)

# sns.regplot(x="StudentHours", y="Marks", data=student_df)
# plt.show()
