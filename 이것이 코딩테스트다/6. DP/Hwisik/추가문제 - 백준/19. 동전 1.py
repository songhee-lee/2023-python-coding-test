'''
[문제]
- n가지 종류의 동전이 있다. 이 동전들의 개수는 무한하다.
- 동전을 적당히 사용해서, 가치의 합이 k원이 되도록 한다.
- 사용한 동전의 구성은 같지만, 순서만 다른 것은 같은 경우이다.
- k원을 만들 수 있는 경우의 수를 구하시오.

[점화식]
- dp[i] += dp[i - coin]
    -> i원을 만들 수 있는 경우의 수는, i - coin원을 만들 수 있는 경우의 수에 coin원을 더한 경우의 수이다.

'''

n, k = map(int, input().split())


coins = [int(input()) for _ in range(n)]

# dp[i] : i원을 만들 수 있는 경우의 수
dp = [0] * (k + 1)
dp[0] = 1

# 입력으로 주어진 동전의 가치에 대해서
for coin in coins:
    # 동전의 가치가 k원보다 크면, dp에 더할 필요가 없다.(dp의 크기는 k + 1이기 때문)
    if coin <= k: 
        dp[coin] += 1 # 자기 자신은 1가지 경우의 수가 있다.
        
    # 점화식
    # i원을 만들 수 있는 경우의 수는, 
    # i - coin원을 만들 수 있는 경우의 수에 coin원을 더한 경우의 수이다.
    for i in range(coin + 1, k + 1):
        dp[i] += dp[i - coin]
    
print(dp[k])