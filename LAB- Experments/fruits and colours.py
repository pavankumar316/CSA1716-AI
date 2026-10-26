fruits = ["Apple", "Banana", "Grapes"]
colors = ["Red", "Yellow", "Green"]

assignment = {}

def backtrack(index):
    if index == len(fruits):
        print(assignment)
        return

    fruit = fruits[index]

    for color in colors:
        assignment[fruit] = color
        backtrack(index + 1)
        del assignment[fruit]

backtrack(0)
