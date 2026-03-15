# WRITE A PYTHON PROGRAM THAT CALCULATES STANDARD SCALAR OF DATASET BY FEATURE SCALING

from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[25,20000],
              [30,40000],
              [35,80000]])

SS = StandardScaler()

X_scaled = SS.fit_transform(X)

print("ORIGINAL DATA :")
print(X)

print("SCALED DATA :")
print(X_scaled)