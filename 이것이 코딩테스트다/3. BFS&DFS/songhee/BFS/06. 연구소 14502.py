""" 

1. 입력 받기
    - 0 빈칸 1 벽 2 바이러스
2. 벽 세개 설치하기
3. 바이러스 퍼트리기
4. 안전 영역 크기 계산
5. 출력

"""

from itertools import combinations
import copy


# 1. 입력 받기
N, M = map(int, input().split())    # 지도 세로, 가로 크기
maps = []   # 지도
for _ in range(N):
    maps.append(list(map(int, input().split())))


def virus(x, y, maps):
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0 <= nx < N and 0 <= ny < M :
            if maps[nx][ny] == 0 :
                maps[nx][ny] = 2
                virus(nx, ny, maps)

def calculate(maps):
    safety_zone = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                safety_zone += 1
    return safety_zone

# 2. 벽 세개 설치하기
zero = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            zero.append((i, j))
result = 0
for partition in combinations(zero, 3):
    # 벽 3개 설치하기
    tmp = copy.deepcopy(maps)
    for i, j in partition:
        tmp[i][j] = 1
    
    # 3. 바이러스 퍼트리기
    for a in range(N):
        for b in range(M):
            if tmp[a][b] == 2:
                virus(a, b, tmp)
    
    # 4. 안전 영역 계산
    safety_zone = calculate(tmp)
    result = max(result, safety_zone)

print(result)