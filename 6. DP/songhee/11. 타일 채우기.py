""" 
- 3xN 의 벽을 2x1(a) 과 1x2(b) 타일로 채우는 경우의 수

- 3x1 : X
- 3x2 : a 3개 / a2개+b1개 * 2
- 3x3 : X
- 3x4 : (3x2)*2 + 2
"""

N = int(input())
dp = [0] * (N+1)

if N > 1:
    dp[2] = 3

for i in range(4, N+1, 2):
    dp[i] = dp[i-2] * 3 + sum(dp[:i-2])*2 + 2

print(dp[N])