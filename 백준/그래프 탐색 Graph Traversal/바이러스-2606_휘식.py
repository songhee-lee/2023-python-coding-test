n = int(input())
m = int(input())

edges = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, input().split())
  edges[a].append(b)
  edges[b].append(a)
  
def dfs(v):
  visited[v] = 1
  
  for nxt in edges[v]:
    if not visited[nxt]:
      dfs(nxt)

dfs(1)

print(visited.count(1) - 1)