""" 
- N개의 정수 중 연속된 수의 합이 가장 큰 합 구하기
"""

N = int(input())
numbers = list(map(int, input().split()))

# dp[x][0] : ~X-1 번째까지 수 중 연속합의 최댓값
# dp[x][1] : ~X번째까지 연속합

dp = [[0]*2 for _ in range(N)]
dp[0][0] = dp[0][1] = numbers[0]

for i in range(1, N):
    # ~i번째까지 최대 VS ~i-1번째까지 최대 VS i번째서 새로 시작
    dp[i][0] = max(dp[i-1][0], dp[i-1][1])
    dp[i][1] = max(dp[i-1][1]+numbers[i], numbers[i])

print(max(dp[N-1]))