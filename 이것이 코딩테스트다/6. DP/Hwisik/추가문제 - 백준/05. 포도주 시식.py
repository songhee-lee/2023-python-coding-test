'''
[설명]
- 포도주 시식에는 규칙이 있다.
    1. 포도주 잔을 선택하면, 그 잔을 포함한 왼쪽의 잔은 마실 수 없다.
    2. 연속으로 놓여 있는 3잔을 모두 마실 수 없다.
- 포도주 잔이 n개가 있을 때, 최대로 마실 수 있는 포도주의 양을 구하라.

[점화식]
- dp[i] : i번째 포도주까지 최대로 마실 수 있는 포도주의 양
    - i번째 포도주를 마시지 않는 경우 : dp[i - 1]
    - i번째 포도주를 마시는 경우
        - dp[i - 2] + wines[i] : i - 2번째 까지 마시고 i번째 포도주 마시기
        - dp[i - 3] + wines[i - 1] + wines[i] : i - 3번째 까지 마시고 i - 1, i번째 포도주 마시기
        
'''

import sys

n = int(input())
wines = [int(input()) for _ in range(n)]

dp = [0] * n
dp[0] = wines[0]
if n >= 2:
    dp[1] = wines[0] + wines[1]
if n >= 3:
    dp[2] = max(dp[1], wines[0] + wines[2], wines[1] + wines[2])

for i in range(3, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + wines[i], dp[i - 3] + wines[i - 1] + wines[i])

print(max(dp))