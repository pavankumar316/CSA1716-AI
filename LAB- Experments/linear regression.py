# Linear Regression Without External Libraries

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

n = len(x)

mean_x = sum(x) / n
mean_y = sum(y) / n

numerator = sum((x[i] - mean_x) * (y[i] - mean_y)
                for i in range(n))

denominator = sum((x[i] - mean_x) ** 2
                  for i in range(n))

slope = numerator / denominator
intercept = mean_y - slope * mean_x

# Predict output
new_x = 6
prediction = slope * new_x + intercept

print("Slope:", slope)
print("Intercept:", intercept)
print("Prediction for input 6:", prediction)
