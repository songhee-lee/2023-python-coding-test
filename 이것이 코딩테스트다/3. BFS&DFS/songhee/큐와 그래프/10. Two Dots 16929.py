""" 
- 2초 / 512MB

- 사이클 존재하는지 여부 확인
    - 색상 별로 확인
    - 점이 4개 이상
    - 각 점이 인접
"""
import sys
sys.setrecursionlimit(100000)

def check_cycle(start, now, cnt):
    global flag
    x, y = now # 현재 위치

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        # 이동할 수 있는 위치인지 확인
        if (nx, ny) not in graph:
            continue

        # 사이클 존재하면
        if cnt >= 4 and nx == start[0] and ny == start[1]:
            flag = True
            return
        
        # 방문하지 않은 점이라면 방문
        if visited[nx][ny]:
            visited[nx][ny] = False
            check_cycle(start, (nx, ny), cnt+1)
            visited[nx][ny] = True

N, M = map(int, input().split())    # 게임판 크기 N x M

if N < 2 or M < 2 : # 사이클을 만들 수 없는 게임판 크기
    print("No")
    exit(0)

# 색상별로 좌표 저장
maps = {} 
for i in range(N):
    line = list(input())

    for j in range(M):
        x = line[j]

        if x not in maps:
            maps[x] = set()
        maps[x].add((i, j))

flag = False    # 사이클 유무

# 상하좌우 이동
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 색상 별로 확인
for color in maps:
    graph = maps[color]

    if len(graph) < 4 : # 점 개수가 4개보다 작으면 X
        continue
    
    for dot in graph:   # 각 점을 사이클 시작점으로 뒀을 때 확인
        visited = [[True] * M for _ in range(N)]
        visited[dot[0]][dot[1]] = False
        check_cycle(dot, dot, 1)

        if flag:    # 사이클 찾았으면 탐색 그만
            print("Yes")
            exit(0)

print("No")