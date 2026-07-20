import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

def ucs(graph, start, goal):
    pq = [(0, start)]
    visited = set()

    while pq:
        cost, node = heapq.heappop(pq)

        if node == goal:
            print("Minimum Cost:", cost)
            return

        if node not in visited:
            visited.add(node)
            for neighbour, weight in graph[node]:
                heapq.heappush(pq, (cost + weight, neighbour))

ucs(graph, 'A', 'F')
