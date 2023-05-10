""" 
- N까지의 정수 K개를 더해서 합이 N이 되는 경우의 수 구하기
- 1e9로 나눈 나머지 출력하기

- 점화식 세우기...
"""

N, K = map(int, input().split())
mod = 1000000000

if K == 1:
    print(1)
    exit()
elif K == 2:
    print(N+1)
    exit()

# dp[k][n]
dp = [[0]*(N+1) for i in range(K+1)]

for i in range(N+1):
    dp[1][i] = 1    # K=1 이면 항상 1개 
    dp[2][i] = i+1  # K=2 이면 항상 i+1개 

for k in range(2, K+1):
    dp[k][1] = k    # (0, 0, .., 1) 경우의수
    for n in range(2, N+1):
        dp[k][n] = (dp[k][n-1] + dp[k-1][n]) % mod

print(dp[K][N])