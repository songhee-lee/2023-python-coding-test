""" 
[ 조건 ]
- 공간 : 0 빈칸, 1~6 물고기 크기, 9 아기 상어

- 자신의 크기보다 작은 물고기만 먹을 수 있고,
    크기가 같은 물고기는 지나칠 수 있음
- 먹을 수 있는 물고기 없으면 Time out
- 먹을 수 있는 물고기 중 가장 가까운 물고기 먹으러 감
    - 같은 거리 내에서는 가장 위+왼쪽 물고기 먹기
- 아기 상어 이동은 1초
- 자신의 크기와 같은 수의 물고기 먹으면 크기가 1 증가함

[ Flow ]
- 아기 상어, 물고기의 위치 기록
1. 아기 상어 크기보다 작은 물고기까지의 거리 구하기
2. 가장 가까운 물고기 먹으러 go
3. 자신보다 작은 물고기가 존재하지 않으면 엄마 호출
"""

from collections import deque

def calc_distance():
    q = deque([shark_loc])
    visited = [[-1] * N for _ in range(N)]
    visited[shark_loc[0]][shark_loc[1]] = 0
    distance = []
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            # 지도 밖
            if nx < 0 or nx >= N or ny < 0 or ny >= N : continue
            
            # 방문하기
            if maps[nx][ny] <= shark_size and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                
                if maps[nx][ny] < shark_size and maps[nx][ny] != 0:
                    distance.append( (nx, ny, visited[nx][ny]))
    
    return sorted(distance, key=lambda x : (-x[2], -x[0], -x[1]))

# 1. 입력 받기
N = int(input())    # 공간 크기

maps = []   # 공간 상태
shark_loc = (0, 0)  # 상어 위치
for i in range(N):
    line = list(map(int, input().split()))
    
    for j in range(N):
        if line[j] == 9:
            shark_loc = (i, j)
            line[j] = 0
    maps.append(line)

# 상하좌우 이동
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

shark_size = 2   # 아기 상어 크기
eaten_fish = 0   # 먹은 물고기 숫자
time = 0    # 시간 초

while True:
    # 2. 상어보다 작은 물고기까지의 거리 구하기
    distance = calc_distance()

    # 먹을 수 있는 물고기가 없으면 Time out
    if len(distance) == 0:
        break
    
    # 3. 가장 가까운 물고기에게 Go
    nx, ny, d = distance[-1]

    maps[nx][ny] = 0          # 물고기 먹고 빈칸됨
    shark_loc = (nx, ny)      # 상어가 물고기 위치로 이동
    time += d                 # 틱톡

    if eaten_fish == shark_size-1:
        shark_size += 1
        eaten_fish = 0
    else:
        eaten_fish += 1
        
print(time)