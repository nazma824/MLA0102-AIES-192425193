from collections import deque

CAP1 = 11
CAP2 = 9
GOAL = 8

def bfs():
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (a, b), path = queue.popleft()

        if a == GOAL or b == GOAL:
            return path + [(a, b)]

        if (a, b) in visited:
            continue

        visited.add((a, b))

        next_states = []

        next_states.append((CAP1, b))

        next_states.append((a, CAP2))

        next_states.append((0, b))

        next_states.append((a, 0))

        transfer = min(a, CAP2 - b)
        next_states.append((a - transfer, b + transfer))

        transfer = min(b, CAP1 - a)
        next_states.append((a + transfer, b - transfer))

        for state in next_states:
            if state not in visited:
                queue.append((state, path + [(a, b)]))

    return None

solution = bfs()

print("Sequence of States:")
for state in solution:
    print(state)

print("\nGoal Achieved: Exactly 8 litres measured.")
