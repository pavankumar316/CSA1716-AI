
import random

# Objective function
def fitness(x):
    return x * x

# Generate initial population
population = [random.randint(0, 31) for _ in range(6)]

# Genetic Algorithm
for generation in range(20):

    # Selection
    population.sort(key=fitness, reverse=True)
    parents = population[:3]

    # Crossover and Mutation
    new_population = parents.copy()

    while len(new_population) < 6:
        p1 = random.choice(parents)
        p2 = random.choice(parents)

        # Crossover
        child = (p1 + p2) // 2

        # Mutation
        if random.random() < 0.2:
            child = random.randint(0, 31)

        new_population.append(child)

    population = new_population

# Find best solution
best = max(population, key=fitness)

print("Best Solution:", best)
print("Maximum Fitness:", fitness(best))
