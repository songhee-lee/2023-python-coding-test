from heapq import heappop, heappush

INF = int(1e9)

def preprocess(n, fares):
    graph = [[] for _ in range(n + 1)]

    for fare in fares:
        src, dst, cost = fare[0], fare[1], fare[2]
        graph[src].append([dst, cost])
        graph[dst].append([src, cost])

    return graph

def dijkstra(graph, src, dst):
    n = len(graph)
    distance = [INF] * n
    distance[src] = 0
    pq = [(0, src)]

    while pq:
        w, x = heappop(pq)

        if distance[x] < w:
            continue

        for neighbor, weight in graph[x]:
            new_distance = weight + w
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heappush(pq, (new_distance, neighbor))

    return distance[dst]

def solution(n, s, a, b, fares):
    graph = preprocess(n, fares)
    cost = dijkstra(graph, s, a) + dijkstra(graph, s, b)

    for i in range(1, n + 1):
        if s != i:
            cost = min(cost, dijkstra(graph, s, i) + dijkstra(graph, i, a) + dijkstra(graph, i, b))

    return cost
