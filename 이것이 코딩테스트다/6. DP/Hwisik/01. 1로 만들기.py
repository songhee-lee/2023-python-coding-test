'''
[설명]
- 정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 4가지.
    - X가 5로 나누어떨어지면, 5로 나눈다.
    - X가 3으로 나누어떨어지면, 3으로 나눈다.
    - X가 2로 나누어떨어지면, 2로 나눈다.
    - X에서 1을 뺀다.
- 정수 X를 1로 만드려고 할 때, 연산을 사용하는 횟수의 최솟값 출력하기

[아이디어]
- 무작정 큰 수로 나누면 안된다. -> 26 -> 25 -> 5 -> 1 처럼 1을 먼저 뺐을 때 최소 연산횟수가 가능함.
- 따라서, 먼저 1을 뺀 후 5, 3, 2 순서로 나눠본다.

[점화식]
- dp[i] = min(dp[i - 1], dp[i // 2], dp[i // 3], dp[i // 5]) + 1
    -> i를 1로 만들기 위해 4가지 연산을 사용했을 때 필요한 최소 연산 횟수
'''

import sys

x = int(input())

# dp[i] = i를 1로 만들기 위해 필요한 최소 연산 횟수
dp = [0] * (x + 1)

for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1 # 먼저 1을 뺀다.
    
    # 5로 나누어 떨어지면
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1) 
    
    # 3으로 나누어 떨어지면
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    
    # 2로 나누어 떨어지면
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

# 출력
print(dp[x])