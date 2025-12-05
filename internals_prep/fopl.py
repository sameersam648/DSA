import numpy as np

def tsp_nearest_neighbour(graph, start = 0):
    n = len(graph)
    visited = [False] * n
    tour = [start]
    visited[start] = True
    total_cost = 0
    current = start

    for _ in range(n - 1):
        nearest_city = None
        min_dist = float ('inf')

        for city in range(n):
            if not visited[city] and graph[current][city] < min_dist:
                min_dist = graph[current][city]
                nearest_city = city

        tour.append(nearest_city)
        visited[nearest_city] = True
        total_cost += min_dist
        current = nearest_city

    total_cost += graph[current][start]
    tour.append(start)

    return tour, total_cost

graph = np.array([
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
])

tour, cost = tsp_nearest_neighbour(graph, start = 0)
print("Tour:", tour)
print("Total Cost:", cost)