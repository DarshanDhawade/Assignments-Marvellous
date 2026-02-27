import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier,plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)


#####################################################################
# DATASET LOADING
#####################################################################
Border = "-"*40
print(Border)
print("DATASET LOADING")
print(Border)


print(Border)
print("Step 1")
print(Border)

DatasetPath= "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)
print("Dataset gets loaded successfully....")

#####################################################################
# DECIDE INDEPENDENT AND DEPENDENT VARIABLES
#####################################################################
print(Border)
print("DECIDE INDEPENDENT AND DEPENDENT VARIABLES")
print(Border)

# X : INDEPENDENT VARIABLES / FEATURES
# Y : DEPENDENT VARIABLES / LABELS

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]
Y = df["FinalResult"]

print("X shape :",X.shape)
print("Y shape :",Y.shape)

#####################################################################
# SPLIT THE DATA SET FOR TRAINING AND TESTING
#####################################################################
print(Border)
print("SPLIT THE DATA SET FOR TRAINING AND TESTING")
print(Border)

# TEST SIZE = 50% 
# TRAIN SIZE = 50%

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.5,
    random_state=42
)

print("Data splitting activity done")

print("X - Independent :",X.shape) #(30,5)
print("Y - Dependent :",Y.shape) #(30,)

print("X_train :",X_train.shape) #(15,5)
print("X_test :",X_test.shape) #(15,5)

print("Y_train :",Y_train.shape) #(15,)
print("Y_test :",Y_test.shape) #(15,)

#####################################################################
# BUILD THE MODEL
#####################################################################
print(Border)
print("BUILD THE MODEL")
print(Border)

print("WE Are GOING TO USE THE DECISION TREE CLASSIFIER")

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=None,
    random_state=42,

)

print("Model successfully created :",model)


#####################################################################
# TRAIN THE MODEL
#####################################################################
print(Border)
print("TRAIN THE MODEL")
print(Border)

model.fit(X_train,Y_train)

print("model training completed")

#####################################################################
# EVALUATE THE MODEL
#####################################################################
print(Border)
print("EVALUATE THE MODEL")
print(Border)

Y_pred = model.predict(X_test)
X_pred = model.predict(X_train)

print("Model Evaluation (testing) Complete")

print(Y_pred.shape)

print("Expected ans :")
print(Y_test)

print("Predicted ans :")
print(Y_pred)

#####################################################################
#EVALUATE THE MODEL PERFORMANCE
#####################################################################
print(Border)
print("EVALUATE THE MODEL PERFORMANCE")
print(Border)

train_accuracy = accuracy_score(Y_train,X_pred)
print("Accuracy of training model is :",train_accuracy*100)

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of testing model is :",accuracy*100)

cm = confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix :")
print(cm)

print("Classification Report :")
print(classification_report(Y_test,Y_pred))

#####################################################################
#FINAL CONCLUSION
#####################################################################
print(Border)
#print("FINAL CONCLUSION")
print(Border)

# the confusion matrix is [[7 0]
#                          [1 7]]
# Type 1 error which is false positive

# this model is slighly overfitting as 100% training accuracy and 93.3% test accuracy

# MAX DEPTH 1 = Train Accuracy : 100 and Test Accuracy : 93.3 No change
# MAX DEPTH 3 = Train Accuracy : 100 and Test Accuracy : 93.3 No change
# MAX DEPTH None = Train Accuracy : 100 and Test Accuracy : 93.3 No change

new_stud= np.array([[6,85,66,7,7]])

prediction = model.predict(new_stud)
print("Prediction Result of New Student :",prediction) # The New Student passes with those features

#####################################################################
#MODEL.FEATURE_IMPORTANCES
#####################################################################
print(Border)
print("MODEL.FEATURE_IMPORTANCES")
print(Border)


feature_imp = pd.Series(model.feature_importances_,index=X.columns)

print("Feature Important Scores :\n")
print(feature_imp)

print("\nMost important feature :")
print(feature_imp.idxmax())

print("\nLeast important feature :")
print(feature_imp.idxmin())

# MOST IMPORTANT FEATURE IS ATTENDACE AND LEAST IS STUDY HOURS WHICH CONTRIBUTES IN FINAL RESULT 

#####################################################################
#REMOVING SLEEPHOURS COLUMN
#####################################################################
print(Border)
print("REMOVING SLEEPHOURS COLUMN")
print(Border)

X_new = X.drop("SleepHours",axis=1)

####################################################################
#TRAINING MODEL AGAIN
#####################################################################
print(Border)
print("TRAINING MODEL AGAIN")
print(Border)

X_train_new,X_test_new,Y_train_new,Y_test_new = train_test_split(X_new,Y,test_size=0.3,random_state=42)

model_new = DecisionTreeClassifier(max_depth=5,random_state=42)
model_new.fit(X_train_new,Y_train_new)

Y_pred_new = model_new.predict(X_test_new)
new_accuracy = accuracy_score(Y_test_new,Y_pred_new)

print("Previous Accuracy : 93.3%")
print("New Accuracy After Removing SleepHours :",new_accuracy * 100)

# BY REMOVING STUDYHOURS THE ACCURACY DROPPED TO 88.88% THIS DID LOWER THE PERFORMANCE BY 5% PERCENT

####################################################################
#TRAINING MODEL USING STUDYHOURS AND ATTENDANCE
#####################################################################
print(Border)
print("TRAINING MODEL USING STUDYHOURS AND ATTENDANCE")
print(Border)

X_small = X[["StudyHours","Attendance"]]

X_train_small,X_test_small,Y_train_small,Y_test_small = train_test_split(
    X_small,Y,test_size=0.3,random_state=42
)

model_small = DecisionTreeClassifier(max_depth=5,random_state=42)
model_small.fit(X_train_small,Y_train_small)

Y_pred_small = model_small.predict(X_test_small)
small_accuracy = accuracy_score(Y_test_small,Y_pred_small)

print("Full Model Accuracy : 93.3%")
print("Accuracy using only StudyHours and Attendance:",small_accuracy * 100)

#Accuracy using only StudyHours and Attendance is 88.8 it affected the full model accuracy

####################################################################
#NEW DATA FRAME 
#####################################################################
print(Border)
print("NEW DATA FRAME ")
print(Border)

# Create new students data
new_students = pd.DataFrame({
    "StudyHours": [2, 5, 1, 6, 3],
    "Attendance": [60, 85, 40, 90, 75],
    "PreviousScore":[78,89,90,74,65],
    "AssignmentsCompleted": [5, 9, 3, 10, 7],
    "SleepHours": [6, 7, 5, 8, 6]
})

predictions = model.predict(new_students)

new_students['Predicted_Result'] = predictions
new_students['Predicted_Result'] = new_students['Predicted_Result'].map({0: 'Fail', 1: 'Pass'})

print(new_students)

####################################################################
#MANUALLY CALCULATED ACCURACY
#####################################################################
print(Border)
print("MANUALLY CALCULATED ACCURACY")
print(Border)

# MANUALLY CALCULATED ACCURACY IS THE SAME AS SK LEARN 

####################################################################
#IDENTIFY STUDENTS WHERE Y_TEST ! = Y_PRED
#####################################################################
print(Border)
print("IDENTIFY STUDENTS WHERE Y_TEST ! = Y_PRED")
print(Border)

# Find misclassified indices
misclassified = Y_test != Y_pred

# Display those rows from test data
print("Misclassified Students:\n")
print(X_test[misclassified])

# Count them
print("\nNumber of Misclassified Students:", misclassified.sum())

# THERE IS ONE MISCLASSIFIED STUEDENT NO 24

####################################################################
#DIFFERENT RANDOM STATE 
#####################################################################
print(Border)
print("DIFFERENT RANDOM STATE")
print(Border)

for state in [0, 10, 42]:
    X_train_rs, X_test_rs, Y_train_rs, Y_test_rs = train_test_split(
        X, Y, test_size=0.3, random_state=state)

    model_rs = DecisionTreeClassifier(max_depth=5, random_state=state)
    model_rs.fit(X_train_rs, Y_train_rs)

    y_pred_rs = model_rs.predict(X_test_rs)

    acc = (Y_test_rs == y_pred_rs).sum() / len(Y_test_rs)

    print(f"Random State {state} -> Accuracy: {acc * 100}")

#WHEN RANDOM STATE IS 0 ACCURACY IS 100 
#WHEN RANDOM STATE IS 10 ACCURACY IS 88.8
#WHEN RANDOM STATE IS 40 ACCURACY IS 88.8

####################################################################
#DECISION TREE VISUALISATION
#####################################################################
print(Border)
print("DECISION TREE VISUALISATION")
print(Border)

plt.figure(figsize=(12,8))
plot_tree(model, feature_names=X.columns, class_names=['Fail','Pass'], filled=True)
plt.show()

#ATTENDANCE APPEARS AT THE ROOT NODE
# AS IT IS THE MOST IMPORTANT FEATURE THATS WHY IT WAS SELECTED

####################################################################
#CREATE A NEW COLUMN : PERMORMANCE INDEX
#####################################################################
print(Border)
print("CREATE A NEW COLUMN : PERMORMANCE INDEX")
print(Border)

# Create new feature
df['PerformanceIndex'] = (df['StudyHours'] * 2) + df['Attendance']

print(df.head())

####################################################################
#CHECKING ACCURACY WITH : PERMORMANCE INDEX
#####################################################################
print(Border)
print("CHECKING ACCURACY WITH : PERMORMANCE INDEX")
print(Border)

# Define X and y again
X_new = df.drop('FinalResult', axis=1)
Y_new = df['FinalResult']

# Train-test split
from sklearn.model_selection import train_test_split

X_train_pi, X_test_pi, Y_train_pi, Y_test_pi = train_test_split(
    X_new, Y_new, test_size=0.3, random_state=42)

# Train model
from sklearn.tree import DecisionTreeClassifier

model_pi = DecisionTreeClassifier(max_depth=5, random_state=42)
model_pi.fit(X_train_pi, Y_train_pi)

# Calculate accuracy
Y_pred_pi = model_pi.predict(X_test_pi)

accuracy_pi = (Y_test_pi == Y_pred_pi).sum() / len(Y_test_pi)

print("Accuracy with PerformanceIndex:", accuracy_pi * 100)

#NO THE ACCURACY IS THE SAME NO CHANGES 

####################################################################
#TRAIN MODEL WITH MAX DEPTH : NONE
#####################################################################
print(Border)
print("TRAIN MODEL WITH MAX DEPTH : NONE")
print(Border)

# Train full depth tree
model_full = DecisionTreeClassifier(max_depth=None, random_state=42)
model_full.fit(X_train, Y_train)

# Training accuracy
train_pred_full = model_full.predict(X_train)
train_acc_full = (Y_train == train_pred_full).sum() / len(Y_train)

# Testing accuracy
test_pred_full = model_full.predict(X_test)
test_acc_full = (Y_test == test_pred_full).sum() / len(Y_test)

print("Training Accuracy (max_depth=None):", train_acc_full * 100)
print("Testing Accuracy (max_depth=None):", test_acc_full * 100)

#Training Accuracy (max_depth=None): 100.0
#Testing Accuracy (max_depth=None): 93.33333333333333

#THIS IS BECAUSE OF OVERFITTING