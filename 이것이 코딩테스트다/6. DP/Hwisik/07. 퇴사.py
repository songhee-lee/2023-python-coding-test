'''
[설명]
- 오늘부터 N + 1일째 되는 날에 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.
- 하루에 하나씩 서로 다른 사람의 상담이 있다.
- 상담을 완료하는데 걸리는 기간 : Ti, 받을 수 있는 금액 : Pi

[아이디어]
- Bottom-Up
- i번째 일의 상담을 기준으로, (i + time[i])번째 일부터 일을 했을 때 수익이 i번째 일의 상담의 수익보다 작다면, 갱신하는 방식으로...

[점화식]
- dp[j] = max(dp[j], dp[i] + price[i]) => 단, j의 범위는 [i + time[i], n + 1]
    -> j번째 일을 했을 때 얻을 수 있는 최대 수익은, i번째 일을 했을 때 수익과 j번째 일을 했을 때 수익 중 최댓값

-> ✅ 다시풀기
'''

import sys

# sol-1
# 1일부터 n일까지(Bottom-Up)
def dp_helper():
    dp = [0] * (n + 1)
    
    for i in range(n): # i일의 상담
        for j in range(i + time[i], n + 1): # i번째 일의 상담이 끝나는 날부터
            if dp[j] < dp[i] + price[i]: # 현재 상담이 i번째 일을 했을 때 수익보다 작다면
                dp[j] = dp[i] + price[i] # 갱신
    
    # 최종적으로 리스트의 마지막에 최댓값이 있다.
    return dp[-1]
# sol-2
# n일부터 1일까지 (Top-Down)
def dp_helper2():
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        # i번째 일에 상담을 하는데, 퇴사일을 넘긴다면
        if i + time[i] > n:
            dp[i] = dp[i + 1] # 상담 안함
        else:
            # i번째 일에 상담 하지 않기 or i번째 일에 상담을 하기 중 이익이 큰 것을 선택
            dp[i] = max(dp[i + 1], price[i] + dp[i + time[i]])
            
    return dp[0]

n = int(input())
time = []
price = []
dp = [0] * (n + 1)

for i in range(n):
    t, p = map(int, input().split())
    time.append(t)
    price.append(p)

print(dp_helper())