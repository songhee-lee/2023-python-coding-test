'''
[문제]
- n가지 종류의 동전이 주어졌을 때, 그 가치의 합이 K원이 되도록 하기 위해 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
- 각각의 동전은 몇 개라도 사용할 수 있다.
- 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

[점화식]
- dp[i] = min(dp[i], dp[i - coin] + 1)
    -> 사용한 동전의 최소 개수이므로 +1을 해준다.

'''

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [float('inf')] * (k + 1)

# sol - 1
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        # 이때는 i - coin이 0이 될 수 있다. 그러므로 위에서 dp[0] = 0을 해줘야 한다.
        dp[i] = min(dp[i], dp[i - coin] + 1) # 단, 사용한 동전의 개수는 최소기 때문에 min을 사용한다.

print(dp[k] if dp[k] != float('inf') else -1)

# sol - 2
for coin in coins:
    # 동전의 가치가 k원보다 작거나 같을 때
    if coin <= k:
        dp[coin] = 1
    
    # 점화식
    # i원을 만들 수 있는 경우의 수는 i - coin원을 만들 수 있는 경우의 수에 coin원을 더해야 하므로 +1을 해준다.
    for i in range(coin + 1, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1) # 단, 사용한 동전의 개수는 최소기 때문에 min을 사용한다.

print(dp[k] if dp[k] != float('inf') else -1)