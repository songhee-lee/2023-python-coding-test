""" 

"""
from collections import deque

def bfs(i, j, color):
    q = deque([(i, j)])
    visited[i][j] = False

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny]:
                if maps[nx][ny] in color:
                    visited[nx][ny] = False
                    q.append((nx, ny))

                
# 1. 입력 받기
N = int(input())
maps = []
for _ in range(N):
    maps.append(list(input()))

# 상하좌우 이동
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 색약 X
cnt = 0
visited = [[True]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] :
            bfs(i, j, maps[i][j])
            cnt += 1

# 색약 O
cnt_weak = 0
visited = [[True]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            color = maps[i][j]
            if color == 'B':
                bfs(i, j, 'B')
            else:
                bfs(i, j, {'R', 'G'})
            cnt_weak += 1
            
print(f"{cnt} {cnt_weak}")
