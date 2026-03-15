# WRITE A PYTHON PROGRAM THAT CALCULTES CLASSIFICATION REPORT

from sklearn.metrics import classification_report

actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

cr = classification_report(actual,predicted)
print(cr)

