""" 

- 데스나이트 이동 경우의 수 6개
- bfs로 점진 탐색
"""
from collections import deque

N = int(input())    # 체스판 크기
r1, c1, r2, c2 = map(int, input().split())

# 데스나이트 이동 경우의 수 
dx = (-2, -2, 0, 0, 2, 2)
dy = (-1, 1, -2, 2, -1, 1)

check = [ [-1] * (N+1) for _ in range(N+1)]   # 이동 횟수 기록
q = deque([(r1, c1)])
check[r1][c1] = 0

while q:
    x, y = q.popleft()

    if x == r2 and y == c2:
        break
    
    for i in range(6):
        nx, ny = x+dx[i], y+dy[i]

        # 체스판 밖
        if nx < 0 or nx >= N or ny < 0 or ny >= N :
            continue
        
        # 방문하기
        if check[nx][ny] == -1:
            check[nx][ny] = check[x][y] + 1
            q.append((nx,ny))

print(check[r2][c2])