""" 
- 1x2 와 2x1 타일이 있다
- 2xN 크기의 직사각형 채우는 방법의 수 % 10,007 출력
"""

N = int(input())

# dp[n] : 2xn 크기의 직사각형 채우는 방법 수
dp = [0]*(N+1)
# 초기화
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])