""" 
- 탈출하기 위해 움직여야 하는 최소 칸의 개수

1. 입력 받기
    - 가로 N 세로 M
    - 미로 정보
        - (1, 1) 입구 (N, M) 출구
        - 괴물 0 괴물X 1
2. 괴물 없는 곳 (1)으로 이동하기 <- BFS
    - 이전 칸 + 1 씩 하면서 최단 거리 찾기
"""

from collections import deque

# 1. 입력 받기
N, M = map(int, input().split())    # 미로 가로 크기, 세로 크기
maps = []   # 미로 정보
for _ in range(N):
    maps.append(list(map(int, input())))

dx = (-1, 1, 0, 0)  # 상, 하, 좌, 우
dy = (0, 0, -1, 1)


queue = deque([(0, 0)])   # 방문 칸 추가

while queue :
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M :
            continue

        # 괴물이면 무시
        if maps[nx][ny] == 0 :
            continue
        
        # 처음 방문할 때만 최단 거리에 기록하기
        if maps[nx][ny] == 1:
            maps[nx][ny] = maps[x][y] + 1
            queue.append((nx, ny))

print(maps[N-1][M-1])
