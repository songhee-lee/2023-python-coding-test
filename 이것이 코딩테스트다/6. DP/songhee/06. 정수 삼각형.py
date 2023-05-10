""" 
- 삼각형 위에서 아래로 내려오면서 이제까지의 합이 최대가 되는 경로 구하기
"""

N = int(input())
triangle = [ list(map(int, input().split())) for _ in range(N) ]
triangle.insert(0, [])

# dp[x][i] : x번째 줄에서 i 위치까지 합이 최대가 되는 경로
dp = [ [0] * (i+1) for i in range(N+1)]
dp[1] = [triangle[1][0]]

# Bottom-up
for i in range(2, N+1):
    dp[i][0] = dp[i-1][0] + triangle[i][0]
    for j in range(1, i-1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    dp[i][i-1] = dp[i-1][i-2] + triangle[i][i-1]

print( max(dp[N]))
