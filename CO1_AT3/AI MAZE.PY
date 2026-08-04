from collections import deque

maze = [
    ['S', '.', '.', '#', '.', '.'],
    ['#', '#', '.', '#', '.', '#'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '#', 'G']
]

rows = len(maze)
cols = len(maze[0])

for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 'S':
            start = (i, j)
        if maze[i][j] == 'G':
            goal = (i, j)

directions = [(-1,0),(1,0),(0,-1),(0,1)]

queue = deque([start])
visited = set([start])
parent = {}

found = False

while queue:
    x, y = queue.popleft()

    if (x, y) == goal:
        found = True
        break

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < rows and 0 <= ny < cols:
            if maze[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))

if found:
    path = []
    cur = goal

    while cur != start:
        path.append(cur)
        cur = parent[cur]

    path.append(start)
    path.reverse()

    print("Shortest Path:")
    print(path)

    print("\nNumber of Steps:", len(path)-1)

    for x, y in path:
        if maze[x][y] == '.':
            maze[x][y] = '*'

    print("\nMaze Path:")
    for row in maze:
        print(" ".join(row))
else:
    print("No Path Found")
