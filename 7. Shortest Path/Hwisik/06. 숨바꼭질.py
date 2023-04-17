import sys, heapq

INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

# 개선된 다익스트라 알고리즘
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

# 숨어야 하는 헛간 번호, 해당 헛간까지의 거리, 해당 헛간과 같은 거리를 갖는 헛간의 수
barn_num, barn_dist, barn_cnt = 0, 0, 0
_max = 0 # 최단 거리 중 최댓값(최단 거리가 가장 먼 헛간의 거리)

# 가장 먼 최단 거리를 찾는다.
for d in dist:
    if d != INF:
        _max = max(_max, d)

# 가장 먼 최단 거리를 갖는 헛간의 수를 찾는다.
for d in dist:
    if d != INF:
        if d == _max:
            barn_cnt += 1

# 가장 먼 최단 거리를 갖는 헛간의 번호를 찾는다.(가장 작은 번호)
barn_num = dist.index(_max)

print(barn_num, _max, barn_cnt)            