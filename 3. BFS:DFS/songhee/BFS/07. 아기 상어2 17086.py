""" 
1. 상어 위치 구하고
2. 상어 별로 ~N번까지 거리 구하기
3. 최댓값 출력
"""
from collections import deque

N, M = map(int, input().split())
shark = deque() # 상어 위치
maps = []       # 전체 맵
for i in range(N):
    line = list(map(int, input().split()))

    for j in range(M):  
        if line[j] == 1:    # 상어 위치 추가
            shark.append((i,j))
    maps.append(line)

# 이동 방향 : 상하좌우 대각선
dx = (-1, -1, -1, 0, 1, 1, 1, 0)
dy = (-1, 0, 1, 1, 1, 0, -1, -1)

while shark:
    x, y = shark.popleft()
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 0:
            shark.append((nx,ny))
            maps[nx][ny] = maps[x][y] + 1

print(max([ max(line) for line in maps ]) -1)