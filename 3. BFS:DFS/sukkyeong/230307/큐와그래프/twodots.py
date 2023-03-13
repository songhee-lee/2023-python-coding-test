''''''
import sys

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(input()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y, level, visited):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and graph[x][y] == graph[nx][ny]:
            if level < 3:
                if not (nx, ny) in visited:
                    dfs(nx, ny, level+1, visited+[(nx, ny)])
            else:
                if not (nx, ny) in visited:
                    dfs(nx, ny, level+1, visited+[(nx, ny)])
                else:
                    if visited[0] == (nx, ny):
                        print("Yes")
                        sys.exit()


for a in range(n):
    for b in range(m):
        dfs(a, b, 1, [(a, b)])

print("No")
