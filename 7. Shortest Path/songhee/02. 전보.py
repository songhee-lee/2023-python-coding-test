import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, C = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = [INF] * (N+1)

q = []
distance[C] = 0
heapq.heappush(q, (0, C))

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist :
        continue

    for i in graph[now]:
        cost = dist + i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

cnt, t = 0, 0
for x in distance:
    if x > 0 and x < INF :
        cnt += 1
        t = max(t, x)

print(cnt, t)