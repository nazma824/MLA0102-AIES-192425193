import heapq

graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('D', 4), ('E', 2)],
    'C': [('F', 3)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 5)],
    'G': []
}

heuristic = {
    'A': 7, 'B': 6, 'C': 4,
    'D': 5, 'E': 2, 'F': 3,
    'G': 0
}

def greedy_best_first(start, goal):
    frontier = [(heuristic[start], start)]
    visited = set()
    path = []

    while frontier:
        h, node = heapq.heappop(frontier)
        if node in visited: 
            continue
        visited.add(node)
        path.append(node)
        if node == goal:
            return path
        for neighbor, _ in graph[node]:
            heapq.heappush(frontier, (heuristic[neighbor], neighbor))
    return None

print("Path:", greedy_best_first('A', 'G'))
