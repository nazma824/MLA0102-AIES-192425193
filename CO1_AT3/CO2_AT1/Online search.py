# Online Search Agent

from collections import deque

graph = {
    'S': ['A'],
    'A': ['S', 'B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'F'],
    'D': ['A', 'E'],
    'E': ['D', 'F'],
    'F': ['E', 'C', 'G'],
    'G': ['F']
}

def search(start, goal, obstacle):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for next_node in graph[node]:
            if next_node != obstacle and next_node not in visited:
                queue.append(path + [next_node])

path = search('S', 'G', 'B')

print("Path:", " -> ".join(path))
