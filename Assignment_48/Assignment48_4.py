# WRITE A PYTHON PROGRAM THAT CALCULATES EUCLIDEAN DISTANCE BETWEEN TWO POINTS BEFORE AND AFTER APPLYING FEATURE SCALING AND EXPLAIN THE DIFFERENCE IN RESULTS

from sklearn.preprocessing import StandardScaler
import numpy as np
from scipy.spatial.distance import euclidean

X = np.array([[25,20000],
              [30,40000],
              [35,80000]])

SS = StandardScaler()

X_scaled = SS.fit_transform(X)

print("ORIGINAL DATA :")
print(X)

print("SCALED DATA :")
print(X_scaled)

p1 = X[0]
p2 = X[1]

Old_Distance = euclidean(p1,p2)

scaled_p1 = X_scaled[0]
scaled_p2 = X_scaled[1]

New_Distance = euclidean(scaled_p1,scaled_p2)

print("DISTANCE BEFORE SCALING :",Old_Distance)
print("DISTANCE AFTER SCALING :",New_Distance)

#Difference in Results
#Before scaling: Distance is very large because salary values (20000, 40000) dominate.
#After scaling: Distance becomes balanced because both features are normalized.
