def can_fly(bird):
    if bird.lower() == "penguin":
        print("No, a penguin cannot fly.")
    elif bird.lower() in ["parrot", "pigeon", "sparrow", "eagle"]:
        print("Yes, a", bird, "can fly.")
    else:
        print("Bird not found in the database.")

bird = input("Enter a bird name: ")
can_fly(bird)
