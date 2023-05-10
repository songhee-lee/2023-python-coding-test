"""
- 초콜릿을 NxM 조각으로 쪼개기
- 1x1 크기의 초콜릿으로 쪼개기 위한 최소 쪼개기 횟수 구하기 
"""

N, M = map(int, input().split())

# dp[n][m] : nxm 초콜릿을 1X1로 자르기 위한 최소 횟수
dp = [[90000]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    dp[i][1] = i-1
for j in range(1, M+1):
    dp[1][j] = j-1

for i in range(2, N+1):
    for j in range(2, M+1):
        dp[i][j] = min([dp[i][j-k]+dp[i][k] for k in range(1, j//2+1)]) + 1
        dp[i][j] = min(dp[i][j], min([dp[i-k][j]+dp[k][j] for k in range(1, i//2+1)])+1)

print(dp[N][M])