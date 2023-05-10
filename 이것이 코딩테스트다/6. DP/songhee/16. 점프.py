"""
- (1,1)에서 (N,M으로 이동
- 각 칸에서 숫자만큼 오른쪽이나 아래쪽으로 이동 
- 경로의 개수 구하기
"""

N = int(input())
maps = [ list(map(int, input().split())) for _ in range(N) ]

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        x = maps[i][j]
        if i == N-1 and j == N-1 :   # 끝
            print(dp[i][j])
            exit(0)
        
        # 오른쪽
        if j + x < N:
            dp[i][j+x] += dp[i][j]
        # 아래
        if i + x < N:
            dp[i+x][j] += dp[i][j]

print(0)

"""메모리 초과
from collections import deque
N = int(input())
maps = [ list(map(int, input().split())) for _ in range(N) ]

answer = 0
q = deque([(0, 0)])
while q:
    i, j = q.popleft()
    x = maps[i][j]

    if i+x < N :   # 아래로 이동
        if maps[i+x][j] != 0:
            q.appendleft((i+x, j))
        else:
            answer += 1
    if j+x < N :   # 오른쪽으로 이동
        if maps[i][j+x] != 0:
            q.append((i, j+x))
        else:
            answer += 1

print(answer)
""" 
