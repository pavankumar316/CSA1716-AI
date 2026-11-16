
# SVM Binary Classification using Python

# Training dataset
X = [
    [1, 2],
    [2, 3],
    [3, 3],
    [6, 5],
    [7, 7],
    [8, 6]
]

# Class labels
y = [-1, -1, -1, 1, 1, 1]

# Initial weights and bias
w1 = 0
w2 = 0
b = 0

learning_rate = 0.01
epochs = 1000

# Training using a simple hinge-loss update
for epoch in range(epochs):
    for i in range(len(X)):
        x1, x2 = X[i]

        condition = y[i] * (w1*x1 + w2*x2 + b)

        if condition < 1:
            w1 += learning_rate * y[i] * x1
            w2 += learning_rate * y[i] * x2
            b += learning_rate * y[i]

# Prediction function
def predict(x1, x2):
    result = w1*x1 + w2*x2 + b

    if result >= 0:
        return 1
    else:
        return -1

# Test data
test_data = [
    [2, 2],
    [7, 6]
]

print("SVM Binary Classification")
print("-------------------------")

for point in test_data:
    result = predict(point[0], point[1])

    if result == -1:
        print(point, "Class: 0")
    else:
        print(point, "Class: 1")

print("\nTraining Completed")
print("Weight 1:", round(w1, 2))
print("Weight 2:", round(w2, 2))
print("Bias:", round(b, 2))
