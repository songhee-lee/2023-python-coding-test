""" 
- 0과 1로만 이루어진 수
- 0으로 시작하지 않고 1이 연속하지 않음
- N자리 이친수 개수 구하기
"""

N = int(input())

# dp[x][i] : x자리이고 i로 끝나는 이친수 개수
dp = [[0]*2 for _ in range(N+1)]
dp[1][1] = 1

for i in range(2, N+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(sum(dp[N]))