n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(cur):
    visited[cur] = 1
    
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt)

connected_component_cnt = 0
for cur in range(1, n + 1):
    if not visited[cur]:
        dfs(cur)
        connected_component_cnt += 1

print(connected_component_cnt)