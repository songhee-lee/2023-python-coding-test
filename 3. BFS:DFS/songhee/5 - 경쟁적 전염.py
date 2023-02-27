""" 

1. 입력 받기
    - 0 빈칸 1~K 바이러스
    - S초 뒤 X, Y 위치 출력
2. 바이러스 별 위치 기록하기
3. S초 동안 바이러스 퍼트리기
    - 바이러스가 이미 증식되면 다른 바이러스가 들어갈 수 없다
    - X, Y 위치에 바이러스 증식 됐다면 종료
4. X, Y 위치의 시험관 정보 출력
"""

import sys

# 1. 입력 받기
N, K = map(int, input().split())    # 시험관 크기, 바이러스 개수
graph = []  # 시험관 정보
for _ in range(N):
    graph.append( list(map(int, sys.stdin.readline().rstrip().split())))
S, X, Y = map(int, input().split()) # S초 뒤 X, Y 위치

# 바이러스 이동 정보 : 상하좌우
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def spread(virus):
    new_virus = [ [] for _ in range(K+1) ]
    for k in range(1, K+1): # 바이러스 별로 돌아가면서 증식
        for x, y in virus[k]:   # 해당 바이러스의 위치별로
            for i in range(4):  # 상하좌우 확인
                nx, ny = x+dx[i], y+dy[i]
                
                # 시험관 범위 내에서 바이러스 증식
                if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
                    graph[nx][ny] = k
                    new_virus[k].append((nx, ny))   # 새로운 바이러스 위치 기록
    return new_virus

# 2. 바이러스별 위치 기록하기
virus = [ [] for _ in range(K+1)]
for i in range(N):
    for j in range(N):
        k = graph[i][j]
        if k :
            virus[k].append((i, j))

# 3. S초 동안 바이러스 증식
for _ in range(S):
    if graph[X-1][Y-1]: # X, Y 위치에 바이러스 증식 됐다면 종료
        break
    virus = spread(virus)

# 4. X, Y 위치 시험관 정보 출력
print(graph[X-1][Y-1])

