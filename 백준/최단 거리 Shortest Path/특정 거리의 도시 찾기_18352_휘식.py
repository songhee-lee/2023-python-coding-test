from heapq import heappush, heappop
import sys

INF = int(1e9)
n, m, k, x = map(int, sys.stdin.readline().split())

edges = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  edges[a].append(b)

def dijkstra(x):
  dist[x] = 0
  q = []
  heappush(q, (0, x))
  
  while q:
    cost, v = heappop(q)
    
    if dist[v] < cost:
      continue
      
    for nxt in edges[v]:
      if dist[nxt] > cost + 1:
        dist[nxt] = cost + 1
        heappush(q, (cost + 1, nxt))

dijkstra(x)

answer = []
for i in range(1, n + 1):
  if dist[i] == k: answer.append(i)

if len(answer) == 0: print(-1)
else:
  for d in answer:
    print(d)