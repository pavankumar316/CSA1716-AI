# Decision Tree for Simple Classification

# Training dataset
data = [
    ["Sunny", "No"],
    ["Sunny", "No"],
    ["Rainy", "Yes"],
    ["Rainy", "Yes"],
    ["Cloudy", "Yes"]
]

# Classification function
def predict(weather):
    for row in data:
        if row[0] == weather:
            return row[1]
    return "Unknown"

# Test the model
weather = "Sunny"

result = predict(weather)

print("Decision Tree Classification")
print("Weather:", weather)
print("Play Outside:", result)
