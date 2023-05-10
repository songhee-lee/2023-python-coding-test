"""
- N가지 화폐로 M원을 만들기
- 최소한의 화폐 개수
- 불가능하면 -1 출력하기
""" 

N, M = map(int, input().split())
coins = [ int(input()) for _ in range(N) ]

# dp[x] : x원 만드는데 필요한 최소 화폐 개수
dp = [1e9] * (M+1)   
dp[0] = 0

for coin in coins:  # 각 코인에 대해서
    for k in range(coin, M+1):    # x원 만드는 화폐 개수 구하기
        dp[k] = min(dp[k], dp[k-coin]+1)

print(dp[M]) if dp[M] != 1e9 else print(-1) 

