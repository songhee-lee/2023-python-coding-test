'''
[설명]
- 2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하는 문제

[점화식]
- dp[n] = dp[n - 1] + dp[n - 2]
    -> n번째 타일을 1x2로 채우는 경우 : dp[n - 1]
    -> n번째 타일을 2x1로 채우는 경우 : dp[n - 2]
    
'''

import sys

n = int(input())

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n])