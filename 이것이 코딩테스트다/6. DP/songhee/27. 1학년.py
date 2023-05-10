""" 
 - 중간의 모든 수는 0~20 사이의 수
 - 올바른 등식의 수 구하기
"""

N = int(input())
num = list(map(int, input().split()))

# dp[i][k] : i 번째에서 K를 만들 수 있는 등식의 수 
dp = [[0]*(21) for _ in range(N+1)]
dp[1][num[0]] = 1

for i in range(1, N):
    for k in range(21):
        if dp[i][k] > 0 :   # i번째에서 k 만들 수 있고,
            plus = k + num[i]
            minus = k - num[i]

            if plus <= 20 : # 덧셈 가능
                dp[i+1][plus] += dp[i][k]
            if minus >= 0 : # 뺄셈 가능
                dp[i+1][minus] += dp[i][k]

print(dp[N-1][num[N-1]])            
