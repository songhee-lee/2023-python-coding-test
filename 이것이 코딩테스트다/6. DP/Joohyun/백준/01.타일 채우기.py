n = int(input())

dp = [0]*(n+1)

# 가로 길이가 짝수일 때만 채울 수 있다
if n % 2 != 0:
    print(0)
else:
    dp[2] = 3
    for i in range(4, n+1, 2):      
        dp[i] = dp[i-2] * 3 + 2     # 끝이 2개 짜리로 끝나는 경우 + 한 덩어리로 채우는 경우
        for j in range(2, i-2, 2):  
            dp[i] += dp[j] * 2      # 끝이 4개 짜리로 끝나는 경우

    print(dp[n])