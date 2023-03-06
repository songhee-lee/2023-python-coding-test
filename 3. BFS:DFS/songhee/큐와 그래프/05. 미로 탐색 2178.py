
""" 
- 1초 192MB

- 미로 최소 경로
"""
from collections import deque

def bfs(start):
    # queue 생성
    q = deque([start])

    # 하우좌상 이동 좌표
    dx = (1, 0, 0, -1)
    dy = (0, 1, -1, 0)
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    return graph[N-1][M-1]


N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

print(bfs( (0, 0) ))
