"""
- (1,1) -> (N,M) 이동시 높이가 낮은 지점으로만 이동한다
- 경로 개수 구하기 

*** AGAIN
"""

N, M = map(int, input().split())
maps = [ list(map(int, input().split())) for _ in range(N) ]

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)
dp = [ [-1]*M for _ in range(N) ]

def dfs(x, y):
    # 도착
    if x == N-1 and y == M-1 :
        return 1
    
    # 탐색
    if dp[x][y] == -1:
        dp[x][y] = 0

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] < maps[x][y]:
                dp[x][y] += dfs(nx, ny) # (x, y) -> (nx, ny) 경로 경우의 수

    return dp[x][y]

print(dfs(0,0))

""" 시간초과
from collections import deque

q = deque([(0, 0)])
answer = 0
while q:
    x, y = q.popleft()
    
    if x == N-1 and y == M-1:
        answer += 1
        continue
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]

        if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] < maps[x][y]:
            q.append((nx, ny))
            
print(answer)
"""