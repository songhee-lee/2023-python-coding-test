from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(n):
  graph.append(list(map(int, input())))

def bfs(x, y):
  q = deque([(x, y)])
  while q:
    x, y = q.popleft()
    
    for dx, dy in zip([1, -1, 0, 0,], [0, 0, 1, -1]):
      nx, ny = x + dx, y + dy
      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx, ny))
  
bfs(0, 0)

print(graph[-1][-1])