"""Psuedo Code
https://www.acmicpc.net/problem/3190

1. 입력 받기
    - 보드 크기 N, 사과 개수 K 입력받기
    1-2. 보드 만들기
        - 벽은 -1, 사과는 1 나머지는 0
    - 사과 위치
    - 뱀의 방향 변환 횟수, 변환 정보
2. 뱀 이동시키기
    - 맨 위 맨 좌측에서 오른쪽으로 시작
    - 다음 칸에 사과가 있으면 몸을 늘리고, 없으면 그 칸으로 이동
"""

# 1. 입력 받기
N = int(input())    # 보드 크기
K = int(input())    # 사과 개수

# 1-2. 보드 만들기
maps = [ [-1 for _ in range(N+2)]]
for _ in range(N):
    lines = [0 for _ in range(N)]
    lines.insert(0, -1)
    lines.append(-1)
    maps.append(lines)
maps.append([-1 for _ in range(N+2)])

### 사과 위치 저장
for _ in range(K):
    x, y = map(int, input().split())
    maps[x][y] = 1

### 뱀의 방향 변환 정보 
L = int(input())
moves = {}
for _ in range(L):
    X, C = input().split()
    moves[int(X)] = C


# 2. 뱀 이동시키기
count = 0           # 게임 진행 초
dy = (1, 0, -1, 0)  # 우, 상, 좌, 하
dx = (0, -1, 0, 1)

maps[1][1] = -2     # 뱀의 현 위치 표시
snake = [(1 , 1)]    # 뱀의 위치
d = 0               # 뱀 방향


while True:

    count += 1  # 째깍
    nx, ny = snake[-1][0] + dx[d], snake[-1][1] + dy[d] # 다음 위치

    if maps[nx][ny] < 0 : # 1) 벽이거나 자신의 몸이면 종료
        break
    elif maps[nx][ny] == 0 : # 2) 이동이면
        x_t, y_t = snake.pop(0) # 꼬리 위치
        maps[x_t][y_t] = 0  
        snake.append((nx, ny))  # 머리 위치      
        maps[nx][ny] = -2

    else:                   # 3) 사과면
        snake.append((nx, ny))
        maps[nx][ny] = -2

    # 현재 초에 방향 전환 있으면
    if count in moves.keys():
        if moves[count] == 'D' : # 오른쪽
            d = (d-1) % 4
        elif moves[count] == 'L' : # 왼쪽
            d = (d+1) % 4

print(count)

