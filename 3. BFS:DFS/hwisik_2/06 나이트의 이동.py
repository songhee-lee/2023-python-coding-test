'''
나이트가 가고자 하는 칸까지 최소 몇번만에 이동할 수 있는가? -> ✅'BFS'
'''
from collections import deque

def bfs(sx, sy):
    queue = deque([(sx, sy)])
    dist[sx][sy] = 0
    # visited[sx][sy] = 1
    
    while queue:
        x, y = queue.popleft()
        if x == ex and y == ey:
            return dist[ex][ey]
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l: continue
            if dist[nx][ny] != -1: continue
            
            dist[nx][ny] = dist[x][y] + 1
            # visited[nx][ny] = 1
            queue.append((nx, ny))
    return 0
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

t = int(input())

for _ in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    dist = [[-1] * l for _ in range(l)]
    # visited = [[0] * l for _ in range(l)]
    
    out = bfs(sx, sy)
    
    print(out)