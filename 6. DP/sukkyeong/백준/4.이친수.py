'''
0,1로 이루어진 수 중에서


'''

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]
print(dp[n])
