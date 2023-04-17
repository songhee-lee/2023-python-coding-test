import heapq
from sys import stdin
input = stdin.readline
INF = int(1e9)

n,m=map(int,input().split())

graph=[[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

q = []
distance[1]=0
heapq.heappush(q, (0,1))
while q:
    dist,now = heapq.heappop(q)

    if dist > distance[now]: continue

    for i in graph[now]:
        cost = dist+i[1]

        if cost < distance[i[0]]:
            distance[i[0]]=cost
            heapq.heappush(q,(cost, i[0]))

result = 0
max_dist = -INF
cnt = 0

for i in range(1,n+1):
    if (max_dist < distance[i]):
        result = i
        max_dist = distance[i]
        cnt = 0
    elif (max_dist== distance[i]):
        cnt += 1

print(result, max_dist, cnt)