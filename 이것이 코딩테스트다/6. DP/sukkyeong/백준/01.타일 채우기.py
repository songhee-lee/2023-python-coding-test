'''
dp[0] = 1
dp[2] = 3
dp[4] = 11
dp[6] = 41
dp[8] = 153

dp[i] = dp[i-2] * 3 + (dp[i-4] * 2 + dp[i-6] * 2 + ... + dp[0] * 2)

'''

n = int(input())
if n % 2 == 1:
    print(0)
else:
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 3
    for i in range(4, n + 1, 2):
        dp[i] = dp[i-2] * 3
        for j in range(i-4, -1, -2):
            dp[i] += dp[j] * 2
    print(dp[n])
