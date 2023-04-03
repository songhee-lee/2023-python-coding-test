
dp = [0] * (101)
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2

for _ in range(int(input())):
    N = int(input())

    if dp[N] != 0:
        print(dp[N])
        continue

    for i in range(6, N+1):
        dp[i] = dp[i-5]+dp[i-1]
    
    print(dp[N])