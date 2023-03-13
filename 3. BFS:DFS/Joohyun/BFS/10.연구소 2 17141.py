"""
<< 바이러스 유출 >>
특정 위치에 있는 바이러스 M 개가 동시에 퍼진다

바이러스 개수 : M
연구소 크기 : N x N
연구소 구성 : 빈 칸, 벽, 바이러스를 놓을 수 있는 칸
    0 : 빈칸
    1 : 벽
    2 : 바이러스를 놓을 수 있는 칸
바이러스 ) 1초만에 상하좌우로 인접한 모든 빈 칸으로 동시에 복제
"""

"""
< 알아야 하는 것 >
1. 바이러스를 놓을 수 있는 칸의 위치 = '2' 의 위치
2. 빈칸,벽의 위치 : '0'과 '1'의 위치

< FLOW >
1. 입력
    바이러스를 놓을 수 있는 칸 : '2'
    벽 : '1' -> '-'로 변환
    빈칸 : '0' -> 개수 세기 (empty+=1)
    바이러스를 놓을 수 있는 위치 : viruses = []
    걸린시간 : times = []
2. M개의 바이러스 놓기
    virus : 값이 '2'인 칸 중에서 M개를 선택 -> '조합'
    for v in virus : 모든 조합의 경우의 수만큼 반복
        바이러스를 놓고 남은 바이러스 자리는 빈칸 처리 : '2' -> '0'
        걸린 시간 : time = 0
        bfs(바이러스 위치, 걸린시간)
    2-1. bfs :
        queue에서 하나씩 뽑는다 : 현위치
        현위치에서 상하좌우로 이동
            이동 위치가 연구소 안이고 이동위치 값이 0이면
                이동위치값 = 현위치값 + 1
                empty -= 1 # 바이러스가 안 퍼진 칸 수
                시간 update : time = max(time, 이동위치값)
                이동위치를 queue에 삽입
    2.2. 현재 초기바이러스 위치에서 걸린 시간 추가
        if empty :              # 바이러스가 다 퍼졌을 경우
            times.append(time)
        else : times.append(-1) # 바이러스가 다 안 퍼졌을 경우
3. 최소 시간 출력 :
    while -1 in times:      # 바이러스가 다 안 퍼진 경우 제거
        times.remove(-1)
    if max(times) == -1 : print(min(times)) # 바이러스를 모든 빈 칸에 퍼뜨릴 수 있는 경우, 최소 시간 출력
    else : print(-1)                        # 바이러스를 어떻게 놓아도 모든 빈 칸에 퍼뜨릴 수 없는 경우, -1 출력
"""
import sys, copy
from itertools import combinations
from collections import deque

# 현재 바이러스 위치에서 바이러스가 다 퍼지는 시간 구하기
def bfs (virus):
    time,cnt=0,0    # 걸린 시간 | 바이러스가 퍼진 칸 수
    q = deque()
    for v in virus:
        q.append(v)       # 바이러스 위치 삽입
    while q:
        x,y = q.popleft() # 현재 바이러스 위치
        for dx,dy in D:
            nx, ny = x+dx, y+dy                         # 상하좌우로 이동
            if 0<=nx<n and 0<=ny<n and lab_[nx][ny]==0: # 이동위치가 연구소 안이고, 아직 바이러스가 퍼지지 않은 칸일 경우
                lab_[nx][ny]=lab_[x][y]+1               # 이동위치까지 바이러스가 퍼지기까지 걸린 시간 update
                cnt += 1                                # 바이러스가 퍼진 칸의 수 증가
                time = max(time, lab_[nx][ny])          # 바이러스가 다 퍼지기까지 걸린 최종 시간 update
                q.append((nx,ny))                       # 이동위치 큐에 삽입
    return (time,cnt)
    

# 1. 입력 : 연구실 및 바이러스를 놓을 수 있는 위치
n,m = map(int,input().split())      # 연구소 크기:nxn  |  바이러스 개수:m
lab, viruses, times = [], [], []    # 연구실 정보 | 바이러스를 놓을 수 있는 칸 위치 | 걸린 시간
empty = 0                           # 빈칸 개수
D = [(-1,0), (1,0), (0,-1), (0,1)]  # 상하좌우

for i in range(n):
    l = list(map(int,sys.stdin.readline().split()))
    for j in range(n):
        if l[j] == 0 : empty+=1           # 0 : 빈칸                  >> 빈칸 개수 empty 1 증가
        elif l[j] == 1 : l[j] = '-'       # 1 : 벽                   >> 1 -> '-'
        else : viruses.append((i,j))      # 2 : 바이러스를 놓을 수 있는 칸 >> 위치 저장
    lab.append(l)   # 연구실 정보 update
empty += len(viruses)-m

# 2. M개의 바이러스 놓기
for virus in combinations(viruses,m):
    lab_ = copy.deepcopy(lab)                # 바이러스 위치마다 연구실 초기화
    for x,y in viruses: 
        if not (x,y) in virus : lab_[x][y] = 0   # 바이러스를 놓고 남은 바이러스 자리는 빈칸 처리

    # 2.1 ) 현재 바이러스 위치에서 바이러스가 다 퍼지는 시간 구하기
    time,cnt = bfs(virus) # 바이러스 퍼뜨리기

    # 2.2 ) 걸린 시간 추가
    if not empty-cnt : times.append(time-2)

# 3. 최소 시간 출력
if times : print(min(times))    # 바이러스가 모든 빈칸에 다 퍼진 경우가 있으면, 최소 걸린 시간 출력
else : print(-1)                  # 바이러스가 모든 빈칸에 다 퍼진 경우가 없으면, -1 출력