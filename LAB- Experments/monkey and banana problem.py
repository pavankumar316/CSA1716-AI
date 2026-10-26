monkey = "door"
banana = "middle"
box = "window"

print("Monkey and Banana Problem")

if monkey != banana:
    print("Monkey moves to the box.")
    monkey = box

if box != banana:
    print("Monkey pushes the box under the banana.")
    box = banana
    monkey = banana

print("Monkey climbs onto the box.")
print("Monkey takes the banana.")
print("Goal Achieved!")
