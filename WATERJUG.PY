from collections import deque

JUG1 = 3
JUG2 = 5
GOAL = 4

visited = set()
queue = deque([((0, 0), [])])

while queue:
    (x, y), path = queue.popleft()

    if (x, y) in visited:
        continue

    visited.add((x, y))
    path = path + [(x, y)]

    if x == GOAL or y == GOAL:
        print("Solution:")
        for state in path:
            print(state)
        break

    states = [
        (JUG1, y),                          # Fill Jug1
        (x, JUG2),                          # Fill Jug2
        (0, y),                             # Empty Jug1
        (x, 0),                             # Empty Jug2
        (max(0, x-(JUG2-y)), min(JUG2, x+y)),  # Pour Jug1 → Jug2
        (min(JUG1, x+y), max(0, y-(JUG1-x)))   # Pour Jug2 → Jug1
    ]

    for s in states:
        if s not in visited:
            queue.append((s, path))
