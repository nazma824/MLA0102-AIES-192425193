import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('F', 2)],
    'E': [('F', 1)],
    'F': []
}

heuristic = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

def astar(start, goal):
    pq = [(heuristic[start], 0, start)]
    visited = set()

    while pq:
        f, g, node = heapq.heappop(pq)

        if node == goal:
            print("Minimum Cost:", g)
            return

        if node not in visited:
            visited.add(node)

            for neighbour, cost in graph[node]:
                new_g = g + cost
                new_f = new_g + heuristic[neighbour]
                heapq.heappush(pq, (new_f, new_g, neighbour))

astar('A', 'F')
