import heapq
from sys import stdin
input = stdin.readline
INF = int(1e9)

n,m,start = map(int,input().split())

graph=[[] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q=[]

    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now = heapq.heappop(q)
        if distance[now]<dist: continue

        for i in graph[now]:
            cost=dist+i[1]

            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

cnt = 0
max_dist = 0

for d in distance:
    if d != INF:
        cnt +=1
        max_dist=max(max_dist, d)

print(cnt-1, max_dist)