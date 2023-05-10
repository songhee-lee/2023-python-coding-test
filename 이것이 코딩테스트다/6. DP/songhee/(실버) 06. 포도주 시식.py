""" 
- 연속으로 포도주 3잔을 마실 수는 없다
- 될 수 있는 대로 많은 양의 포도주를 맛보는 방법은?

"""

N = int(input())
wine = [ int(input()) for _ in range(N) ]

# dp[x] : x번째 포도주까지의 최대 양
dp = [0] * N

dp[0] = wine[0]
if N > 1:
    dp[1] = wine[0]+wine[1]

if N > 2:
    dp[2] = max(wine[0]+wine[1], wine[1]+wine[2], wine[0]+wine[2])

for i in range(3, N):
    # i-1번째 + 안마심 VS i-1번째(1회)+마심 VS i-2번째 + 마심 
    dp[i] = max(dp[i-1], dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i])

print(dp[N-1])