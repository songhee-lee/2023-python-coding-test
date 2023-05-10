""" 
- 0 빈칸, 1 벽, 2 바이러스 놓을 수 있는 칸
- 바이러스는 상하좌우로 복제됨
- 모든 빈 칸에 바이러스 퍼뜨리는 최소 시간 구하기

- 바이러스를 놓을 칸 선택하기 (M개)
- 바이러스 퍼뜨리기 (BFS)
- 최소 시간 구하기
"""
from itertools import combinations
from collections import deque

# 바이러스 퍼뜨리기
def spread(q):
    new_q = deque() # 새로운 바이러스 위치

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 :
                visited[nx][ny] = 2
                new_q.append((nx,ny))
    return new_q

# 바이러스 모두 퍼졌는지 확인하기
def check():
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                return False
    return True

# 1. 입력 받기
N, M = map(int, input().split())    # 연구소 크기, 바이러스 개수
maps = []
virus_loc = set()
for i in range(N):
    line = list(map(int, input().split()))
    maps.append(line)

    # 바이러스 위치 기록
    for j in range(N):
        if line[j] == 2:
            virus_loc.add((i,j))
            maps[i][j] = 0

# 상하좌우 이동
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

time = 1e9  
# 2. 바이러스 놓을 칸 선택하기 (M개)
# M 이 10 이므로 조합 사용
for virus in combinations(virus_loc, M):
    
    q = deque()
    visited = [ m[:] for m in maps ]
    
    # 바이러스 표시
    for x, y in virus: 
        visited[x][y] = 2
        q.append((x, y))
    
    # 3. 바이러스 퍼뜨리기
    t = 0
    while q:
        q = spread(q)
        t += 1 

    # 4. 모든 칸에 퍼졌는지 확인
    if check():
        time = min(time, t)
if time == 1e9 :
    print(-1)
else:
    print(time-1)
    