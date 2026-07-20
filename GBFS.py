import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 0
}

def greedy(start, goal):
    visited = set()
    pq = [(heuristic[start], start)]

    while pq:
        h, node = heapq.heappop(pq)

        if node in visited:
            continue

        print(node, end=" ")
        visited.add(node)

        if node == goal:
            break

        for neighbour in graph[node]:
            heapq.heappush(pq, (heuristic[neighbour], neighbour))

greedy('A', 'F')
