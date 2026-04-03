import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

#=================================================
# STEP 1 : LOAD THE DATASET
#=================================================

df = pd.read_csv("diabetes.csv")

#=================================================
# STEP 2 : EXPLORATORTY DATA ANALYSIS
#=================================================

print("FIRST 5 ROWS :")
print(df.head())

print("SHAPE OF DATASET :")
print(df.shape)

print("MISSING VALUES :")
print(df.isnull().sum())

print("DESCRIPTION OF DATASET :")
print(df.describe())

sns.histplot(df)
plt.show()

sns.boxplot(df)
plt.show()

sns.pairplot(df)
plt.show()

#=================================================
# STEP 3 : DATA PREPROCESSING
#=================================================

# HANDLE GLUCOSE COLUMN

Glucose_median = df["Glucose"].median()
print("MEDIAN OF GLUCOSE COLUMN :",Glucose_median)

# REPLACE MISSING VALUES WITH MEDIAN

df["Glucose"] = df["Glucose"].fillna(Glucose_median)


# HANDLE BLOODPRESSURE COLUMN

BP_median = df["BloodPressure"].median()
print("MEDIAN OF BLOOD PRESSURE COLUMN :",BP_median)

# REPLACE MISSING VALUES WITH MEDIAN

df["BloodPressure"] = df["BloodPressure"].fillna(BP_median)


#-------------------------
# STEP 4 : SELECT FEATURES AND TARGET
#-------------------------

print("STEP : SELECT FEATURES")

X = df[["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]]
Y = df["Outcome"]

print("SELECTED FEATURES :")
print(X.head())

print("SHAPE OF SELECTED FEATURES")
print(X.head())

#-------------------------
# STEP 5 : SCALE THE DATA
#-------------------------

print("STEP : SCALE THE DATA")

scalar = StandardScaler()
X_scaled = scalar.fit_transform(X)

print("DATA AFTER SCALING :")
print(X_scaled[:5])

#-------------------------
# STEP 6 : SPLIT THE DATA
#-------------------------

X_train,X_test,Y_train,Y_test = train_test_split(X_scaled,Y,test_size=0.2,random_state=42)

#-------------------------
# STEP 7 : TRAIN THE MODEL
#-------------------------

Model1 = DecisionTreeClassifier()
Model1.fit(X_train,Y_train)

Model2 = LogisticRegression()
Model2.fit(X_train,Y_train)

#-------------------------
# STEP 8 : EVALUATE THE MODEL
#-------------------------

# PREDICTIONS
y_pred1 = Model1.predict(X_test)
y_pred2 = Model2.predict(X_test)

# ACCURACY
print("DECISION TREE ACCURACY:", accuracy_score(Y_test, y_pred1))
print("LOGISTIC REGRESSION ACCURACY:", accuracy_score(Y_test, y_pred2))

# CONFUSION MATRIX
print(confusion_matrix(Y_test, y_pred1))

# CLASSIFICATION REPORT
print(classification_report(Y_test, y_pred1))

#-------------------------
# STEP 9 : VISUALIZATION
#-------------------------

sns.heatmap(confusion_matrix(Y_test, y_pred1), annot=True, fmt='d')
plt.title("CONFUSION MATRIX")
plt.show()

predictions = Model1.predict(X_test)

print("PREDICTIONS:")
print(predictions)

# SAVE CSV

pd.DataFrame(predictions, columns=["Predicted"]).to_csv("predictions.csv", index=False)