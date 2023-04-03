"""
- 3으로 ...
- 2로...
- 1 빼기

- 최소한의 연산으로 1을 만드는 방법
"""

X = int(input())

# dp[x] : x를 1로 만드는데 필요한 최소 연산 횟수
dp = [ 0 ] * (X+1)

# bottom-up
for i in range(2, X+1):
    dp[i] = dp[i-1] + 1     # 1빼기
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])

print(dp[X])