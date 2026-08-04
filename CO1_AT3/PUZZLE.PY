from queue import PriorityQueue

goal = ((1,2,3),
        (4,5,6),
        (7,8,0))

start = ((1,2,5),
         (4,0,8),
         (7,3,6))

def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def neighbors(state):
    state = [list(row) for row in state]

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j

    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    result = []

    for dx, dy in moves:
        nx, ny = x+dx, y+dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            temp = [row[:] for row in state]
            temp[x][y], temp[nx][ny] = temp[nx][ny], temp[x][y]
            result.append(tuple(tuple(r) for r in temp))

    return result

pq = PriorityQueue()
pq.put((heuristic(start),0,start))

visited = set()

while not pq.empty():
    f,g,state = pq.get()

    if state == goal:
        print("Goal State Reached!")
        for row in state:
            print(row)
        print("Total Moves:",g)
        break

    if state in visited:
        continue

    visited.add(state)

    for nxt in neighbors(state):
        if nxt not in visited:
            pq.put((g+1+heuristic(nxt),g+1,nxt))
