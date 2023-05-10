import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)


count = 0
for i in range(1, n+1):
    if visited[i] == False:
        count += 1
        dfs(i)

print(count)
