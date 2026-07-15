graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = []
queue = []

visited.append('A')
queue.append('A')

while queue:
    node = queue.pop(0)
    print(node, end=" ")

    for i in graph[node]:
        if i not in visited:
            visited.append(i)
            queue.append(i)
