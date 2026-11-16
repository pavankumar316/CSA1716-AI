
# Dimensionality Reduction using PCA
# Without external libraries

import math

# Dataset with two features
data = [
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6],
    [6, 7]
]

# Calculate mean
mean_x = sum(row[0] for row in data) / len(data)
mean_y = sum(row[1] for row in data) / len(data)

# Center the data
centered = [
    [row[0] - mean_x, row[1] - mean_y]
    for row in data
]

# Calculate covariance matrix
n = len(data)

a = sum(row[0]**2 for row in centered) / (n - 1)
b = sum(row[0]*row[1] for row in centered) / (n - 1)
c = sum(row[1]**2 for row in centered) / (n - 1)

# Calculate largest eigenvalue
trace = a + c
det = a*c - b*b

eigenvalue = (trace + math.sqrt(trace**2 - 4*det)) / 2

# Calculate eigenvector
if abs(b) > 1e-10:
    vx = b
    vy = eigenvalue - a
else:
    vx = 1
    vy = 0

# Normalize eigenvector
length = math.sqrt(vx**2 + vy**2)
vx = vx / length
vy = vy / length

# Project data onto first principal component
reduced_data = []

for row in centered:
    value = row[0]*vx + row[1]*vy
    reduced_data.append(round(value, 3))

# Display results
print("Original Dataset:")
for row in data:
    print(row)

print("\nOriginal Dimensions: 2")

print("\nReduced Dataset:")
for value in reduced_data:
    print(value)

print("\nReduced Dimensions: 1")
print("PCA Completed Successfully!")
