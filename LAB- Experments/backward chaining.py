facts = {"fever", "cough"}

rules = {
    "flu": ["fever", "cough"],
    "take_rest": ["flu"],
    "high_temperature": ["fever"]
}

def backward_chaining(goal):
    if goal in facts:
        return True

    if goal in rules:
        for condition in rules[goal]:
            if not backward_chaining(condition):
                return False
        return True

    return False

goal = input("Enter goal: ")

if backward_chaining(goal):
    print(goal, "is proved.")
else:
    print(goal, "cannot be proved.")
