facts = {"fever", "cough"}

rules = [
    ({"fever", "cough"}, "flu"),
    ({"flu"}, "take_rest"),
    ({"fever"}, "high_temperature")
]

def forward_chaining(facts, rules):
    while True:
        new_fact = False

        for conditions, result in rules:
            if conditions.issubset(facts) and result not in facts:
                facts.add(result)
                print("New fact:", result)
                new_fact = True

        if not new_fact:
            break

    print("\nFinal Facts:", facts)

forward_chaining(facts, rules)
