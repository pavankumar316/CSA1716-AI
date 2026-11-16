
# Recommendation System using Collaborative Filtering

# User movie ratings
ratings = {
    'User1': {'Movie1': 5, 'Movie2': 4, 'Movie3': 1},
    'User2': {'Movie1': 5, 'Movie2': 4, 'Movie4': 5},
    'User3': {'Movie1': 1, 'Movie3': 5, 'Movie4': 2},
    'User4': {'Movie2': 4, 'Movie3': 1, 'Movie4': 5}
}

# Select target user
target_user = 'User1'

# Calculate similarity between two users
def similarity(user1, user2):
    common = set(ratings[user1]) & set(ratings[user2])

    if not common:
        return 0

    numerator = sum(
        ratings[user1][m] * ratings[user2][m]
        for m in common
    )

    sum1 = sum(ratings[user1][m]**2 for m in common)
    sum2 = sum(ratings[user2][m]**2 for m in common)

    denominator = (sum1 * sum2) ** 0.5

    return numerator / denominator if denominator else 0

# Find similar users
scores = {}

for user in ratings:
    if user != target_user:
        scores[user] = similarity(target_user, user)

# Generate recommendations
recommendations = {}

for user, score in scores.items():
    for movie, rating in ratings[user].items():
        if movie not in ratings[target_user]:
            recommendations[movie] = (
                recommendations.get(movie, 0) + score * rating
            )

# Display results
print("Recommendation System")
print("----------------------")
print("Target User:", target_user)

print("\nSimilar Users:")
for user, score in scores.items():
    print(user, "Similarity:", round(score, 2))

print("\nRecommended Movies:")

if recommendations:
    for movie, score in sorted(
        recommendations.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        print(movie, "Score:", round(score, 2))
else:
    print("No recommendations available")
