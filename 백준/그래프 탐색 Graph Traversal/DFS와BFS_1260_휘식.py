from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
for i in range(1, n + 1):
  graph[i].sort()


def dfs(v):
  visited[v] = 1
  dfs_ret.append(v)
  for nxt in graph[v]:
    if not visited[nxt]:
      dfs(nxt)

def bfs(v):
  visited[v] = 1
  q = deque([v])
  
  while q:
    cur = q.popleft()
    bfs_ret.append(cur)
    for nxt in graph[cur]:
      if not visited[nxt]:
        visited[nxt] = 1
        q.append(nxt)
        

visited = [0] * (n + 1)
dfs_ret = []
dfs(v)

visited = [0] * (n + 1)
bfs_ret = []
bfs(v)

print(*dfs_ret)
print(*bfs_ret)