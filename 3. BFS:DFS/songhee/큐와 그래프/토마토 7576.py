""" 
- 익은 토마토 주변은 하루 지나면 상하좌우 인접 토마토가 익게 됨
- 모든 토마토가 익는데 걸리는 최수 일수
"""
from collections import deque

def check():
    # 모든 토마토가 익었는지 확인
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                return 0
    return max([ max(m) for m in maps])

# 1. 입력 받기
M, N = map(int, input().split())
maps = []
tomato_loc = set()  # 최초 익은 토마토 위치 기록
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 1:
            tomato_loc.add((i, j))   # x좌표, y좌표
    maps.append(line)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

q = deque(tomato_loc)
result = -1

while q:
    x, y = q.popleft()

    # 네 방향으로 전이
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M : continue
        if maps[nx][ny] == 0:
            maps[nx][ny] = maps[x][y] + 1
            q.append((nx, ny))

print(check()-1)