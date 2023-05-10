'''
[설명]
- 인접한 모든 자리의 차이가 1인 수 -> 계단 수
- 길이가 N인 계단 수의 개수를 구하는 프로그램 작성
- 0으로 시작하는 수는 계단수가 아니다.

[점화식]
- dp[i][j] = 자리수가 i이고 첫번째 수가 j인 계단 수의 개수
    -> j == 0 : dp[i][j] = dp[i - 1][1]
    -> 1 <= j <= 8 : dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
    -> j == 9 : dp[i][j] = dp[i - 1][8]
'''

import sys

MOD = 1_000_000_000

n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif 1 <= j <= 8:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
        else:
            dp[i][j] = dp[i - 1][8]

print(sum(dp[n]) % MOD)