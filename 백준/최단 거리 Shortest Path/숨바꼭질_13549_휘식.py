from collections import deque
import heapq

n, k = map(int, input().split())

#1. 다익스트라
def dijkstra(n, k):
  dist = [int(1e9)] * 100001
  dist[n] = 0
  q = []
  heapq.heappush(q, (0, n))
  
  while q:
    t, x = heapq.heappop(q)
    
    if dist[x] < t:
      continue
    
    for nx in [x - 1,  x + 1, x * 2]:
      if 0 <= nx <= 100000:
        if nx == x * 2:
          if dist[nx] > t:
            dist[nx] = t
            heapq.heappush(q, (t, nx))
        else:
          if dist[nx] > t + 1:
            dist[nx] = t + 1
            heapq.heappush(q, (t + 1, nx))
  return dist[k]

ret = dijkstra(n, k)
print(ret)

#2. BFS
def bfs(n, k):
  q = deque([(n, 0)])
  visited = [0] * 100001
  
  while q:
    x, t = q.popleft()
    
    if x == k:
      return t
    
    for nx in [x - 1, x + 1, x * 2]:
      if 0 <= nx <= 100000 and not visited[nx]:
        if nx == x * 2:
          q.appendleft((nx, t))
          visited[nx] = 1
        else:
          q.append((nx, t+1))
          visited[nx] = 1

ret = bfs(n, k)
print(ret)