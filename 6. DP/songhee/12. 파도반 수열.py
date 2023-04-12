
dp = [0] * (101)
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2

now = 6
for _ in range(int(input())):
    N = int(input())

    if dp[N] != 0:
        print(dp[N])
        continue

    for i in range(now, N+1):
        dp[i] = dp[i-5]+dp[i-1]
    
    now = N+1
    print(dp[N])