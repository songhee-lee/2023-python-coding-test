""" 
- 길이가 N인 계단 수가 몇 개 있는지 구하기
dp[1] = 9
dp[2] : 8*2 (98) => 17
dp[3] : (101, 898) 15*2  => 32 
"""

N = int(input())

# dp[x][i] : 길이가 x고 i 로 끝나는 계단 수 개수
dp = [[0] * 10 for _ in range(N+1)]
for i in range(1, 10):
    dp[1][i] = 1

# bottom-up
mod = 1000000000
for i in range(2, N+1):
    dp[i][0] = dp[i-1][1] % mod
    dp[i][9] = dp[i-1][8] % mod
    for j in range(1, 9):
        dp[i][j] += dp[i-1][j-1] + dp[i-1][j+1]
        dp[i][j] %= mod

print(sum(dp[N])%mod)