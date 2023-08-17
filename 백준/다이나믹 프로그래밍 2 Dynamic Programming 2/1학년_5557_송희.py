from collections import defaultdict

# 입력 받기
N = int(input())
numbers = list(map(int, input().split()))

# dp[i][j] : ~i번째 까지 만들 수 있는 0~20까지 숫자의 개수
dp = [[0] * 21 for _ in range(N)]
dp[0][numbers[0]] = 1       # 0번째 숫자에서 만들 수 있는 숫자

for i in range(1, N-1) :    # 1 ~ N-1 번까지 차례로 수식 만들기
    for j in range(21) :
        # 이전에 만들 수 있는 숫자에 +, - 하기
        if dp[i-1][j] : 
        	plus, minus = j + numbers[i], j - numbers[i]
            if plus <= 20 : 
                dp[i][plus] += dp[i-1][j]
            if minus >= 0 :
                dp[i][minus] += dp[i-1][j]

print(dp[N-2][numbers[N-1]])