
# Sentiment Analysis using Python NLP

# Positive and Negative words
positive_words = [
    "good", "great", "excellent", "happy",
    "love", "amazing", "wonderful", "best",
    "awesome", "nice"
]

negative_words = [
    "bad", "worst", "terrible", "sad",
    "hate", "poor", "awful", "angry",
    "boring", "disappointed"
]

# Get input from user
text = input("Enter a sentence: ")

# Convert text into lowercase words
words = text.lower().split()

# Count positive and negative words
positive_count = sum(1 for word in words if word.strip(".,!?") in positive_words)
negative_count = sum(1 for word in words if word.strip(".,!?") in negative_words)

# Display sentiment
print("\n----- SENTIMENT ANALYSIS -----")

if positive_count > negative_count:
    print("Sentiment: POSITIVE")
elif negative_count > positive_count:
    print("Sentiment: NEGATIVE")
else:
    print("Sentiment: NEUTRAL")

print("Positive Words:", positive_count)
print("Negative Words:", negative_count)
