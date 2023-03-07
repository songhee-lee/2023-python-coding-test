# 공간 : NxM (2이상 50이하)
# 한 칸에 한마리만 들어갈 수 있음
# 0 : 빈칸, 1 : 상어
# 안전 거리 : 거리가 가장 가까운 아기 상어와의 거리
# 이동 : 인접한 8방향 (상하좌우대각선)
# 출력 : 안전거리가 가장 큰 칸
import sys
from collections import deque

N, M = map(int,input().split()) # 공간 크기
space = [list(map(int,sys.stdin.readline().split())) for _ in range(N)] # 공간 정보

# 상어 위치
shark=deque()
for i in range(N):
    for j in range(M):
        if space[i][j] == 1 :
            shark.append((i,j))
visited = [[0]*M for _ in range(N)]

D = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]  #상하좌우,대각선(북서,북동,남동,남서)

def bfs():
    while shark:
        x,y=shark.popleft() # 현 위치
        for dx,dy in D :
            nx,ny=x+dx,y+dy                 # 현위치에서 이동
            if 0<=nx<N and 0<=ny<M :        # 이동 위치가 space 안이라면
                if space[nx][ny]==0:
                    shark.append((nx,ny))
                    space[nx][ny]=space[x][y]+1 # 이동위치까지 이동 횟수 = 현위치까지의 이동횟수 + 1

bfs()
safe = 0
for i in range(N):
    for j in range(M):
        safe = max(safe,space[i][j])

print(safe-1)