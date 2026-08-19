import heapq

def a_star(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start, [start])]
    visited = set()

    while pq:
        f, cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path, cost

        for neighbor, distance in graph[node]:
            if neighbor not in visited:
                new_cost = cost + distance
                new_f = new_cost + heuristic[neighbor]
                heapq.heappush(
                    pq,
                    (new_f, new_cost, neighbor, path + [neighbor])
                )

    return None, None
