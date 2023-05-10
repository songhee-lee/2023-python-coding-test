""" 
- (1,1) -> (N,M) 으로 이동할 때 가져올 수 있는 사탕의 최댓값
"""
from collections import deque

N,M = map(int, input().split())
maps = [ list(map(int, input().split())) for _ in range(N) ]

dx = (1, 0, 1)
dy = (0, 1, 1)

# dp[n][m] : (n,m) 에서 가져갈 수 있는 최대 사탕 수
dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = maps[i-1][j-1] + max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

print(dp[N][M])
