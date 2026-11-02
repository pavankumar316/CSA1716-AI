# Neural Network for Image Classification
# Without external libraries

# Training data: simplified image features
X = [
    [1, 0, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [0, 1, 0, 0]
]

# Class labels
y = [0, 0, 1, 1]

# Initialize weights and bias
weights = [0.1, 0.2, 0.3, 0.4]
bias = 0.1
learning_rate = 0.1

# Train the neural network
for epoch in range(1000):
    for i in range(len(X)):
        total = sum(
            X[i][j] * weights[j] for j in range(4)
        ) + bias

        prediction = 1 if total >= 0.5 else 0
        error = y[i] - prediction

        for j in range(4):
            weights[j] += learning_rate * error * X[i][j]

        bias += learning_rate * error

# Test the network
test_image = [1, 0, 0, 1]

total = sum(
    test_image[j] * weights[j] for j in range(4)
) + bias

prediction = 1 if total >= 0.5 else 0

print("Neural Network Image Classification")
print("Input Image Features:", test_image)
print("Predicted Class:", prediction)
print("Class 0 or Class 1")
