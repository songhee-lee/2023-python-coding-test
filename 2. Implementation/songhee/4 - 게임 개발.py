"""Psuedo Code
1. 맵 크기, 캐릭터 좌표와 맵 정보입력받기
2. 캐릭터 움직이기
    1. 왼쪽 방향으로 회전 후 한 칸
    2. 왼쪽 방향으로 회전
    3. 모두 가봤거나 바다면 뒤로 한 칸
        - 뒤도 바다라 움직일 수 없다면 멈추기
"""

# 1. 입력받기
N, M = map(int, input().split())    # 맵 크기
x, y, d = map(int, input().split()) # 캐릭터 좌표와 방향

maps = []   # 맵 정보
for i in range(N):
    maps.append(list(map(int, input().split())))

# 2. 캐릭터 움직이기
if d % 3 == 1:
    d = (d + 2) % 4
dx = (0, -1, 0, 1)  # 북, 서, 남, 동
dy = (-1, 0, 1, 0)

count = 1   # 캐릭터가 움직인 횟수
rot = 0     # 회전 횟수
maps[x][y] = -1 # 현재 위치 방문 표시
while True:
    d = (d+1) % 4   # 왼쪽으로 회전
    nx, ny = x + dx[d], y + dy[d]   # 다음 위치
    # 2-1. 왼쪽으로 이동 가능한 경우
    if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 0 :
        x, y = nx, ny
        maps[x][y] = -1   # 현 위치 방문 표시
        count += 1
        rot = 0
        continue
    # 2-2. 왼쪽 칸으로 갈 수 없는 경우
    else :
        rot += 1

    # 2-3. 움직일 수 없는 경우
    if rot == 4:
        nx, ny = x - dx[d], y - dy[d]   # 뒤로 한 칸 이동시 위치

        # 뒤로 이동 가능할 때
        if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == -1 :
            x, y = nx, ny
        # 불가능 할 때
        else :
            break
        rot = 0

print(count)