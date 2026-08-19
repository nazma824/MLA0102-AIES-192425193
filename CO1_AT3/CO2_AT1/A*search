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

heuristic = {'A':7,'B':6,'C':4,'D':5,'E':2,'F':3,'G':0}

def a_star(start, goal):
    frontier = [(heuristic[start], 0, start, [])]
    visited = set()

    while frontier:
        f, g, node, path = heapq.heappop(frontier)
        if node in visited: 
            continue
        visited.add(node)
        path = path + [node]
        if node == goal:
            return path, g
        for neighbor, cost in graph[node]:
            g_new = g + cost
            f_new = g_new + heuristic[neighbor]
            heapq.heappush(frontier, (f_new, g_new, neighbor, path))
    return None

print("Optimal Path & Cost:", a_star('A','G'))
