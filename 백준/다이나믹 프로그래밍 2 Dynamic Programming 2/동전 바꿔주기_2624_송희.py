import sys
input = sys.stdin.readline

T = int(input())
k = int(input())
coins = []
for _ in range(k) :
    p, n = map(int, input().split())
    coins.append((p, n))

dp = [0] * (T+1)
dp[0] = 1

for coin, cnt in coins :
    for sum in range(T, 0, -1) :        # T원에서 0원이 될 때까지 동전 하나씩 교환
        for i in range(1, cnt+1) :      # 현재 동전 개수만큼 교환
            if sum - coin * i >= 0 :
                dp[sum] += dp[sum - coin * i]
    print(dp)

print(dp[T])