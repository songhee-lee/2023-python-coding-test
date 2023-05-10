""" 
- N은 그보다 작거나 같은 제곱수들의 합으로 나타낼 수 있다.
- 최소 항의 개수 구하기
"""

N = int(input())

# dp[x] : x를 나타낼 때 최소 항 개수
dp = [ i for i in range(N+1) ]

# 자신보다 작은 제곱수까지로 나타낼 수 있는 경우의 수 모두 확인
for i in range(4, N+1):
    for j in range(1, int(i**0.5)+1):
        dp[i] = min(dp[i], dp[i-j*j]+1)

print(dp[N])