
import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Input values
inputs = np.array([1, 0])

# Weights and bias for hidden layer
weights_hidden = np.array([
    [0.5, 0.4],
    [0.3, 0.7]
])

bias_hidden = np.array([0.1, 0.2])

# Hidden layer calculation
hidden_input = np.dot(inputs, weights_hidden) + bias_hidden
hidden_output = sigmoid(hidden_input)

# Weights and bias for output layer
weights_output = np.array([0.6, 0.8])
bias_output = 0.1

# Output layer calculation
output_input = np.dot(hidden_output, weights_output) + bias_output
final_output = sigmoid(output_input)

# Display results
print("Input:", inputs)
print("Hidden Layer Output:", hidden_output)
print("Final Network Output:", final_output)
