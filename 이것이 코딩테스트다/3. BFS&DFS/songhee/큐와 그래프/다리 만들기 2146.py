""" 
- 가장 짧은 다리로 두 대륙을 연결하기

1. 대륙 찾고,
2. 각 대륙의 (x,y) 좌표 비교해서 차이가 가장 적은 값 찾기



< 푸는 중 >
"""
from collections import deque

def bfs(i, j):
    # i,j 에서 시작되는 대륙 찾기
    q = deque([(i, j)])
    maps[i][j] = -1

    loc = set()    # 대륙의 좌표 모으기
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < N :
                if maps[nx][ny] == 1:
                    maps[i][j] = -1
                    q.append((nx, ny))
                else:
                    loc.add((x,y))
    return loc

def distance(i):
    # i 대륙과 다른 대륙의 최소 거리 찾기
    global answer
    dist = [[-1]*N for _ in range(N)]
    q = deque(continents[i])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            # map 밖이면 out
            if nx < 0 or nx >= N or ny < 0 or ny >= N : continue
            # 다른 대륙과 만나면 거리 비교
            if maps[nx][ny] == -1 and (nx, ny) not in continents[i]:
                answer = min(answer, dist[x][y])
                return
            # 바다 만나면 거리 증가
            if maps[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y]+1    
                q.append((nx,ny))

# 1. 입력 받기
N = int(input())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

# 상하좌우 이동
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 2. 대륙 찾기
continents = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            continents.append(bfs(i, j))

# 3. 가장 짧은 다리 찾기
answer = 1e9
for i in range(len(continents)):
    distance(i)

print(answer)