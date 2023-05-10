'''
퇴사할 때까지 가장 돈을 많이 벌게 하는 방법

'''
# top down

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    # 퇴사일을 넘기면 상담 안함
    if i + arr[i][0] > n:
        dp[i] = dp[i+1]
    else:
        # max(상담하는 것,안하는 것)
        dp[i] = max(dp[i+1], arr[i][1]+dp[i+arr[i][0]])

print(dp[0])
