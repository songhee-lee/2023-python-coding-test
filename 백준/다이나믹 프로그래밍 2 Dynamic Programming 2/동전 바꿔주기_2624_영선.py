#입력1 : 지폐의 금액 T
#입력2 : 동전의 가지수 k
#입력3 : 동전의 금액 pi 와 개수 ni

#출력 : 동전 교환 방법의 가지수 출력, 없으면 0
import sys

t = int(input())
k = int(input())
coins = [[0,0]]
for _ in range(k):
    coins.append(list(map(int, sys.stdin.readline().split())))


#dp
dp = [[0 for _ in range(t+1)] for _ in range(k+1)]

dp[0][0] = 1
for i in range(1, k+1):
    pi, ni = coins[i]
    for j in range(t+1):
        dp[i][j] = dp[i-1][j]
        for l in range(1, ni+1):
            if j-(l*pi) >= 0:
                dp[i][j] += dp[i-1][j-l*pi]
            else:
                break

print(dp[k][t])
        

