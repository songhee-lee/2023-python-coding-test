""" 

- L명 이상 R명 이하 인구수가 차이나면 국경선 연다.
- 연합 이루는 각 칸 인구수는 (연합 인구수)//(연합 이루고 있는 칸의 개수)가 됨.

1. 입력 받기
2. 인구 이동
    2-1. 국경선 열기
    3-1. 인구수 정리하기

"""
from collections import deque

def open_borders(x, y):
    nations = [(x, y)]    # 연합한 나라들 리스트
    
    q = deque([(x, y)])
    borders[x][y] = False

    populations = maps[x][y]    # 연합 전체 인구수
    count = 1   # 연합 국가 수

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            # 인근 나라와의 인구수 확인 (L명 이상 R명 이하)
            if 0 <= nx < N and 0 <= ny < N and borders[nx][ny]:
                if L <= abs(maps[x][y] - maps[nx][ny]) <= R :
                    q.append((nx, ny))
                    borders[nx][ny] = False       # 국경선 열림 표시 
                    populations += maps[nx][ny]   # 연합 인구수 더하기   
                    count += 1                    # 연합 국가수 더하기
                    nations.append((nx, ny))      # 연합 국가 추가
    
    for i, j in nations:
        maps[i][j] = populations // count
    
    return len(nations)

# 1. 입력 받기
N, L, R = map(int, input().split())     # 땅 크기, L명 이상 R명 이하
maps = []   # 각 땅의 인구 수
for _ in range(N):
    maps.append(list(map(int, input().split()))) 


# 2. 인구 이동 
dx = (-1, 1, 0, 0)  # 상하좌우
dy = (0, 0, -1, 1)
move_days = 0       # 인구 이동 일수

while True:
    borders = [ [ True for _ in range(N)] for _ in range(N) ]   # 국경선
    flag = False

    # 국경선 열고 인구 이동
    for i in range(N):
        for j in range(N):
            if borders[i][j] :
                country = open_borders(i, j)
                if country > 1:
                    flag = True
    
    # 모든 인구 이동 끝난 경우
    if not flag:
        break

    move_days += 1

print(move_days)