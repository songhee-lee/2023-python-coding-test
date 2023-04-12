""" 
- N가지 동전으로 K원 만들 수 있는 경우의 수
"""
 
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

dp = [0 for _ in range(K+1)]
dp[0] = 1

for coin in coins:
    for k in range(1, K+1):
        if k - coin >= 0:
            dp[k] += dp[k-coin]
print(dp[K])

""" 시간 초과
# dp[n][k] : n가지 동전으로 k원 만드는 경우의 수
dp = [ [0]*(K+1) for _ in range(N) ]

# 코인 X로 만들 수 있는 X 배수들
for i, coin in enumerate(coins):
    for j in range(coin, K+1, coin):
        dp[i][j] = 1

# Bottom-up
for i, coin in enumerate(coins[1:]):
    dp[i+1][coin] += dp[i][coin]
    for k in range(coin+1, K+1):
        for idx in range(k//coin+1): 
            dp[i+1][k] += dp[i][k-coin*idx]

print(dp[N-1][K])
"""