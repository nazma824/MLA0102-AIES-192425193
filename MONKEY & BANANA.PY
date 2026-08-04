# Monkey and Banana Problem

# Initial positions
robot = "A"
box = "B"
banana = "C"
has_banana = False

print("Initial State")
print("Robot Position :", robot)
print("Box Position   :", box)
print("Banana Position:", banana)
print()

# Step 1: Move to the box
if robot != box:
    print("Action 1: Move to the box")
    robot = box

# Step 2: Push the box under the banana
if box != banana:
    print("Action 2: Push the box under the banana")
    box = banana
    robot = banana

# Step 3: Climb the box
print("Action 3: Climb the box")

# Step 4: Pick the banana
has_banana = True
print("Action 4: Pick the banana")

# Goal Check
if has_banana:
    print("\nGoal Achieved! Robot has retrieved the banana.")
