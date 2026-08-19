from collections import deque

def bfs(grid, start, goal):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        r, c = current

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc

            if (nr, nc) in grid:
                if grid[(nr, nc)] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))

    return None


grid = {
    (0,0): 0, (0,1): 0, (0,2): 0,
    (1,0): 0, (1,1): 0, (1,2): 0,
    (2,0): 0, (2,1): 0, (2,2): 0
}

start = (0,0)
goal = (2,2)

print("Initial Path:")
path = bfs(grid, start, goal)
print(path)

# Robot discovers an obstacle
grid[(1,1)] = 1

print("\nObstacle discovered at (1,1)")
print("Replanning...")

path = bfs(grid, start, goal)

print("New Path:")
print(path)
