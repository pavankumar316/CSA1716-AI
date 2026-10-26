# Family Tree

male = ["john", "paul", "tom"]
female = ["mary", "lisa"]

parent = [
    ("john", "paul"),
    ("mary", "paul"),
    ("paul", "tom"),
    ("lisa", "tom")
]

def father(x, y):
    return (x, y) in parent and x in male

def mother(x, y):
    return (x, y) in parent and x in female

def child(x, y):
    return (y, x) in parent

# Display family relationships
print("Father of Paul:")
for x, y in parent:
    if father(x, "paul"):
        print(x)

print("Mother of Paul:")
for x, y in parent:
    if mother(x, "paul"):
        print(x)

print("Children of Paul:")
for x, y in parent:
    if child(x, "paul"):
        print(x)
