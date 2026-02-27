import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier,plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)
import numpy as np

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

