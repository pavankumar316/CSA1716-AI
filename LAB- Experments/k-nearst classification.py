import math

# Training data
data = [
    ([1, 2], "A"),
    ([2, 3], "A"),
    ([3, 3], "A"),
    ([6, 7], "B"),
    ([7, 8], "B"),
    ([8, 7], "B")
]

# Test point
test_point = [5, 6]
k = 3

# Calculate Euclidean distance
distances = []

for point, label in data:
    distance = math.sqrt(
        (point[0] - test_point[0]) ** 2 +
        (point[1] - test_point[1]) ** 2
    )
    distances.append((distance, label))

# Sort by distance
distances.sort(key=lambda x: x[0])

# Select K nearest neighbours
neighbors = distances[:k]

# Count class labels
votes = {}

for distance, label in neighbors:
    votes[label] = votes.get(label, 0) + 1

# Predict the class
prediction = max(votes, key=votes.get)

print("Test Point:", test_point)
print("Nearest Neighbors:", neighbors)
print("Predicted Class:", prediction)
