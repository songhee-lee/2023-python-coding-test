""" 
 - 두 나무 중 열매가 떨어지는데 그 아래 있으면 열매를 먹을 수 있다.
 - T초 동안 W번 움직일 때 받을 수 있는 최대 자두 개수는?
"""

T, W = map(int, input().split())
moves = [0] + [ int(input()) for _ in range(T) ]

# dp1[i][w] : i초에 1번에 있고 w번째 움직임, 최대 자두 개수
# dp2[i][w] : i초에 2번에 있고 W번째 움직임, 최대 자두 개수
dp1 = [[0]*(W+1) for _ in range(T+1)]
dp2 = [[0]*(W+1) for _ in range(T+1)]

# 자두는 1번 나무에서 시작한다. (초깃값 설정)
for i in range(1, T+1):
    if moves[i] == 1:
        dp1[i][0] = dp1[i-1][0]+1
        dp2[i][1] = dp2[i-1][1]
    else:
        dp2[i][1] = dp2[i-1][1]+1
        dp1[i][0] = dp1[i-1][0]

# Bottom-up
for i in range(1, T+1):
    now = moves[i]
    for w in range(1, min(i, W+1)):
        if now == 1:
            dp1[i][w] = max(dp1[i-1][w], dp2[i-1][w-1]) + 1
            dp2[i][w] = max(dp1[i-1][w-1], dp2[i-1][w])
        else:
            dp2[i][w] = max(dp1[i-1][w-1], dp2[i-1][w]) + 1
            dp1[i][w] = max(dp1[i-1][w], dp2[i-1][w-1])

print( max(max(dp1[T]), max(dp2[T])))