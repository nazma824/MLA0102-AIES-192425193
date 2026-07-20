graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)
        print(node, end=" ")

        for i in graph[node]:
            dfs(i)

dfs('A')
