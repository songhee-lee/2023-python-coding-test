import sys, heapq

INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    
    while q:
        d, cur = heapq.heappop(q)
        
        if dist[cur] < d:
            continue
        
        for i in graph[cur]:
            cost = d + i[1]
            
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)

barn_num, barn_dist, barn_cnt = 0, 0, 0
_max = 0

for d in dist:
    if d != INF:
        _max = max(_max, d)

for d in dist:
    if d != INF:
        if d == _max:
            barn_cnt += 1

barn_num = dist.index(_max)

print(barn_num, _max, barn_cnt)            