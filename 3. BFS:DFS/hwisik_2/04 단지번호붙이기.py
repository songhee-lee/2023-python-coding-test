import sys
from collections import deque

n = int(input())

graph = []
visited = [[0] * n for _ in range(n)] 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ret = []

for _ in range(n):
    input_data = list(input())
    graph.append(input_data)

def bfs(i, j):
    queue = deque([(i, j)])
    visited[i][j] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if visited[nx][ny] == 1 or graph[nx][ny] == '0': continue
            
            visited[nx][ny] = 1
            queue.append((nx, ny))
            cnt += 1
    return cnt

total_home_count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == '1':
            out = bfs(i, j)
            ret.append(out)
            total_home_count += 1

print(total_home_count)

ret.sort()
for x in ret:
    print(x)