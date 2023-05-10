""" 
- N 종류 동전으로 K원 만들 때, 동전 개수 최소로 사용하기
- 불가능하면 -1 출력
"""

N, K = map(int, input().split())
coins = set([ int(input()) for _ in range(N) ])

# dp[k] : k원 만드는데 필요한 최소 동전 개수
dp = [1e9]*(K+1)

for coin in coins :
    if coin <= K:
        dp[coin] = 1
    for k in range(1, K+1):
        if k >= coin :
            dp[k] = min(dp[k], dp[k-coin]+1)

print(-1) if dp[K] == 1e9 else print(dp[K])