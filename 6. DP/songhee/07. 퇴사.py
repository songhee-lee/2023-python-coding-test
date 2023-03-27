""" 
- 
"""

N = int(input())
payment = [ list(map(int, input().split())) for _ in range(N) ]

# dp[i] : i+1 일 동안 상담했을 때 받을 수 있는 최대 금액
dp = [0] * (N+1)

# Bottom-up
answer = 0
for i in range(N-1, -1, -1):
    time = payment[i][0] + i

    if time <= N :
        dp[i] = max(payment[i][1] + dp[time], answer)
        answer = dp[i]
    else:
        dp[i] = answer

print(answer)