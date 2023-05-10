"""
- 2xN을 1x2(또는 2x1)타일과 2x2 타일로 채우기
- 좌우 대칭을 이루는 것은 중복 표현으로 처리
- 전체 타일 코드 개수 구하기
"""

N = int(input())

# dp[n] : 2xn 타일의 코드 개수
dp = [0]*(N+1)

dp[1] = 1
if N > 1:
    dp[2] = 3

# 좌우 대칭 고려하지 않을 때
for i in range(3, N+1):
    dp[i] = dp[i-1] + 2 * dp[i-2]

# 좌우 대칭인 경우를 제외하고 //2 하기
if N >= 3:
    if N % 2 == 0:
        symm = dp[N//2] + 2 * dp[(N-2)//2] 
    else:
        symm = dp[(N-1)//2]

    dp[N] = (dp[N]-symm)//2 + symm

print(dp[N])