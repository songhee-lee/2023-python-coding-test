"""
- 소형 기관차가 끌 수 있는 최대 객차 수
- 최대한 많은 손님을 목적지로 운송
- 번호가 연속적인 객차를 끌게 함

- 최대로 운송할 수 있는 손님 수
"""
N = int(input())    # 객차 수
nums = [0] + list(map(int, input().split()))  # 손님수
M = int(input())    # 최대 객차 수

# 구간합 
s = [0]*(N+1)
for i in range(1, N+1):
    s[i] = s[i-1] + nums[i]

# dp[x][i] : 소형 기관차 x대로 i번째 객차까지의 최대 손님 수
dp = [[0]*(N+1) for _ in range(4)]
for x in range(1, 4):
    for i in range(x*M, N+1):
        if x == 1:
            # 차가 1대인 경우 현재 구간합이 최대인지 확인
            dp[x][i] = max(dp[x][i-1], s[i]-s[i-M])
        else:
            # 현재 객차 포함 X vs 현재 객차 포함o
            dp[x][i] = max(dp[x][i-1], dp[x-1][i-M]+s[i]-s[i-M])

print(dp[3][N])