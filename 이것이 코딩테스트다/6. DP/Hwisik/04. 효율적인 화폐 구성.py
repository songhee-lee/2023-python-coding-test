'''
[설명]
- N가지 종류의 화폐가 있고, 화폐의 개수를 최소한으로 사용해서 가치의 합이 M원이 되도록 만드려고 한다.
- 화폐는 몇 개라도 사용할 수 있고, 사용한 화폐의 구성은 같지만 순서가 다른 경우는 같은 경우로 간주한다.

[아이디어]
- 화폐들 중 하나를 선택해서,
- 선택한 화폐의 금액부터 M원까지, 선택한 화폐로 i원을 만들기 위해 사용해야 하는 화폐 개수의 최솟값을 갱신한다.

[점화식]
- dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    -> 가지고 있는 화폐로 i원을 만들기 위해 사용해야 하는 화폐 개수의 최솟값
'''

import sys

n, m = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [1e9] * (m + 1)


# Bottom-Up
dp[0] = 0
for coin in coins: # 가지고 있는 coin으로
    for i in range(coin, m + 1): # m + 1원까지 만들 수 있는지 확인한다.
        dp[i] = min(dp[i], dp[i - coin] + 1)

# 만들 수 없는 금액이면
if dp[m] == 1e9:
    print(-1)
# 만들 수 있는 금액이면
else:
    print(dp[m])