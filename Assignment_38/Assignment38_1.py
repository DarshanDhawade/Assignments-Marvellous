
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

Border = "-"*40

#####################################################################
# QUESTION 1
#####################################################################
print(Border)
print("Step 1")
print(Border)

DatasetPath= "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded successfully....")
print("First 5 entries from dataset : ")
print(df.head())

print("Last 5 entries from dataset : ")
print(df.tail())

print("(Rows,Columns) :",df.shape)
print("column names :",list(df.columns))

print("Data Type of columns")
print(df.dtypes)

#####################################################################
# QUESTION 2
#####################################################################
print(Border)
print("Step 2")
print(Border)

total_students = len(df)
print("Total Number of Students :",total_students)

print("No of Students Passed")
print((df["FinalResult"]==1).sum())

print("No of Students Failed")
print((df["FinalResult"]==0).sum())

#####################################################################
# QUESTION 3
#####################################################################

print(Border)
print("Step 3")
print(Border)

print("Average Study Hours")
print((df["StudyHours"].mean()))

print("Average Attendance")
print((df["Attendance"].mean()))

print("Maximum Previous Score")
print((df["PreviousScore"].max()))

print("Minimum Sleep Hours")
print((df["SleepHours"].min()))

#####################################################################
# QUESTION 4
#####################################################################

print(Border)
print("Step 4")
print(Border)

perc = df["FinalResult"].value_counts(normalize=True)* 100
print(perc)

#DATA SET IS NOT PERFECTLY BALANCED AS IT IS NOT 50-50 BUT 60-40

#####################################################################
# QUESTION 5
#####################################################################

#YES, HIGHER STUDY HOURS DO INCREASE THE CHANCES OF PASSING THERE ARE SOME OUTLIERS AS WELL
#YES, EVEN THE HIGHER ATTENDANCE HELPS IN FINAL RESULT
#LOWER THE ATTENDANCE THE STUDENTS HAVE BEEN FAILED 
#AND EVEN LOW STUDY HOURS ARE IN THE FAVOUR OF FAILED STUDENTS

#####################################################################
# QUESTION 6
#####################################################################

print(Border)
print("Step 6")
print(Border)

sns.histplot(df["StudyHours"])

plt.show()

#THE HISTOGRAM OF STUDY HOURS HELPS US TO UNDERSTAND  
#THAT THE MOST STUDENTS STUDY IN DURATION OF 1-2 , 6-8
#HOURS AND IT HELPS IN DIRECTING US TO PREDICT THE FINAL #RESULT OF FAILING AND PASSING

####################################################################
# QUESTION 7
#####################################################################

print(Border)
print("Step 7")
print(Border)

# SCATTER PLOT
plt.figure(figsize=(7,5))

for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == sp]
    plt.scatter(temp["StudyHours"],temp["PreviousScore"], label = sp)

plt.title("StudyHours vs PreviousScore")
plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")

plt.legend()
plt.grid(True)
plt.show()

####################################################################
# QUESTION 8
#####################################################################

print(Border)
print("Step 8")
print(Border)

sns.boxplot(df["Attendance"])
plt.show()

# NO OUTLIERS ARE THERE

####################################################################
# QUESTION 9
#####################################################################

print(Border)
print("Step 9")
print(Border)

sns.boxplot(x="FinalResult",y="AssignmentsCompleted",data=df)
plt.show()

#THE MORE ASSIGNMENTS ARE COMPLETED THE FINAL RESULT IS PASSED 

####################################################################
# QUESTION 10
#####################################################################

print(Border)
print("Step 10")
print(Border)

plt.figure(figsize=(7,5))

for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == sp]
    plt.scatter(temp["StudyHours"],temp["FinalResult"], label = sp)

plt.title("StudyHours vs FinalResult")
plt.xlabel("StudyHours")
plt.ylabel("FinalResult")

plt.legend()
plt.grid(True)
plt.show()

# FOR PASSING MORE THAN 4 HOURS OF STUDY IS REQD OR ELSE FAILED