'''
동전의 가치를 입력받습니다.
dp[i]는 i원을 만드는 경우의 수를 저장합니다.
dp[0] = 1로 초기화합니다.
동전의 가치를 하나씩 확인하면서, dp[i]를 갱신합니다.
만약 j원을 만드는 경우의 수를 알고 있다면, j원 + 현재 동전의 가치가 i원이 되는 경우에 대해 dp[i]를 갱신합니다.
이때, 갱신되는 dp[i]의 값은 dp[i] += dp[i-coin] 입니다.
위와 같은 과정을 통해 dp 테이블을 구하면, dp[k]는 k원을 만드는 경우의 수가 됩니다.

'''

import sys

# 입력 받기
n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

# dp[i]는 i원을 만드는 경우의 수를 저장합니다.
dp = [0] * (k+1)
dp[0] = 1

# 동전의 가치를 하나씩 확인하면서 dp 테이블을 갱신합니다.
for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]

# k원을 만드는 경우의 수 출력
print(dp[k])
