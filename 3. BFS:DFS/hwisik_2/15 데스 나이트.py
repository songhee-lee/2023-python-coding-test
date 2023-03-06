from collections import deque
import sys

def bfs():
    queue = deque([(r1, c1)])
    dist[r1][c1] = 0
    
    while queue:
        x, y = queue.popleft()
        if x == r2 and y == c2:
            return
        for i in range(6):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

dist = [[-1] * n for _ in range(n)]
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

bfs()

ret = -1 if dist[r2][c2] == -1 else dist[r2][c2]

print(ret)