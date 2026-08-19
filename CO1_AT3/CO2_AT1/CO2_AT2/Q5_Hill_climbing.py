from itertools import combinations

def route_distance(route, distance):
    total = 0

    for i in range(len(route)):
        total += distance[route[i]][route[(i + 1) % len(route)]]

    return total


def hill_climbing(route, distance):

    current = route[:]

    while True:

        current_cost = route_distance(current, distance)

        best_route = current[:]
        best_cost = current_cost

        for i, j in combinations(range(1, len(current)), 2):

            neighbor = current[:]

            neighbor[i], neighbor[j] = \
                neighbor[j], neighbor[i]

            cost = route_distance(neighbor, distance)

            if cost < best_cost:
                best_route = neighbor
                best_cost = cost

        if best_cost < current_cost:
            current = best_route
        else:
            break

    return current, route_distance(current, distance)


distance = {
    'A': {'A':0, 'B':10, 'C':15, 'D':12, 'E':8},
    'B': {'A':10, 'B':0, 'C':9, 'D':11, 'E':14},
    'C': {'A':15, 'B':9, 'C':0, 'D':7, 'E':13},
    'D': {'A':12, 'B':11, 'C':7, 'D':0, 'E':6},
    'E': {'A':8, 'B':14, 'C':13, 'D':6, 'E':0}
}

route = ['A', 'B', 'C', 'D', 'E']

best_route, cost = hill_climbing(route, distance)

print("Initial Route:", " -> ".join(route) + " -> A")
print("Best Route:", " -> ".join(best_route) + " -> A")
print("Total Distance:", cost)
