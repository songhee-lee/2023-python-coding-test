"""
- N x 2 바닥을 1x2 덮개와 2x1 덮개, 2x2 덮개로 채울 때
- 바닥을 채우는 모든 경우의 수

- 경우의 수
    - 1x2 2개 / 2x1 2개 / 2x2 1개
    - 2x1 1개

- 796,796 으로 나눈 나머지 출력하기
"""

N = int(input())

# dp[n] : nx2 바닥 채우는 경우의 수
dp = [0] * (N+1)

# 초깃값 설정
dp[1] = 1
dp[2] = 3

# Bottom-up
for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2] * 2 ) % 796796

print(dp[N])

