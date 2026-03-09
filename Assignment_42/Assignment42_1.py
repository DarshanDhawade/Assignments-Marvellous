import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# -------------------------------
# PART 1 : SIMPLE LINEAR REGRESSION (WITHOUT ML LIBRARY)
# -------------------------------

# Given Dataset
X = [1,2,3,4,5]
Y = [3,4,2,4,5]

n = len(X)

# Calculate mean values
mean_x = sum(X)/n
mean_y = sum(Y)/n

print("Mean of X =", mean_x)
print("Mean of Y =", mean_y)

# Calculate slope (m)
num = 0
den = 0

for i in range(n):
    num += (X[i] - mean_x) * (Y[i] - mean_y)
    den += (X[i] - mean_x) ** 2

m = num / den

# Calculate intercept (c)
c = mean_y - (m * mean_x)

print("Slope (m) =", round(m,2))
print("Intercept (c) =", round(c,2))

print("Regression Equation : Y =", round(m,2),"X +",round(c,2))

# Predict Y when X = 6
x_new = 6
predicted_y = m * x_new + c

print("Predicted Y when X = 6 :", round(predicted_y,2))


# -------------------------------
# PART 2 : MODEL PERFORMANCE (MSE AND R²)
# -------------------------------

# Predict Y values for the whole dataset
predictions = []

for x in X:
    predictions.append(m*x + c)

print("\nActual Y values :", Y)
print("Predicted Y values :", predictions)

# Calculate Mean Squared Error (MSE)
error_sum = 0

for i in range(n):
    error_sum += (Y[i] - predictions[i])**2

mse = error_sum / n
print("Mean Squared Error =", round(mse,3))

# Calculate R² Score
ss_res = 0
ss_tot = 0

for i in range(n):
    ss_res += (Y[i] - predictions[i])**2
    ss_tot += (Y[i] - mean_y)**2

r2 = 1 - (ss_res/ss_tot)

print("R2 Score =", round(r2,3))


# -------------------------------
# PART 3 : LINEAR REGRESSION USING SKLEARN
# -------------------------------


# Dataset
experience = np.array([1,2,3,4,5]).reshape(-1,1)
salary = np.array([20000,25000,30000,35000,40000])

# Train model
model = LinearRegression()
model.fit(experience, salary)

# Predict salary for 6 years experience
pred_salary = model.predict([[6]])

print("\nPredicted Salary for 6 Years Experience: ₹", int(pred_salary[0]))

# Plot graph
plt.scatter(experience, salary)
plt.plot(experience, model.predict(experience))

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary Prediction")

plt.show()


# ===============================================================
# THEORY QUESTIONS (Written as comments)
# ===============================================================

# Q4: Why is KNN called a lazy learner?
# Answer:
# KNN is known as a lazy learner because it does not create an explicit
# training model. Instead, it simply stores the training dataset and
# performs computation only when a prediction is required.

# Q5: What happens if K is too small?
# Answer:
# If the value of K is very small (for example K = 1), the algorithm
# becomes highly sensitive to noise in the dataset and may lead to
# overfitting.

# Q6: What happens if K is too large?
# Answer:
# If K is too large, many neighbors from other classes may be considered.
# This makes the model too generalized and may result in underfitting.

# Q7: Why does Linear Regression minimize squared error?
# Answer:
# Linear regression minimizes the squared error because squaring the
# residual values penalizes large errors more and also makes the
# mathematical optimization easier using calculus.

# Q8: Difference between MSE and R²
# Answer:
# Mean Squared Error (MSE) measures the average squared difference
# between predicted and actual values. Smaller MSE indicates a better model.
# R² score represents how well the independent variable explains
# the variance of the dependent variable. Values closer to 1 indicate
# better performance.

# Q9: Why R² cannot be greater than 1?
# Answer:
# R² is defined as 1 - (SS_res / SS_tot). Since the residual sum of squares
# cannot exceed the total variance by definition of the metric, the value
# of R² normally lies between 0 and 1 for standard regression models.

# Q10: Can KNN be used for regression?
# Answer:
# Yes. In KNN regression, the predicted value is obtained by taking the
# average of the target values of the K nearest neighbors.