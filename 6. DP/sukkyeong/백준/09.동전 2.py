'''
dp[i]는 i원을 만들기 위해 필요한 최소 동전 개수를 저장합니다.
dp 테이블을 무한대로 초기화합니다.
dp[0] = 0으로 초기화합니다.
각 동전의 가치를 하나씩 확인하면서, dp[i-coin] + 1이 dp[i]보다 작으면 dp[i]를 갱신합니다.
이때, dp[i-coin] + 1은 이전에 구한 동전의 가치를 이용하여 만들 수 있는 금액에 현재 동전을 추가한 것을 의미합니다.
dp[i-coin] + 1이 dp[i]보다 작은 경우, dp[i]는 dp[i-coin] + 1로 갱신됩니다.
'''

import sys

# 입력 받기
n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

# dp[i]는 i원을 만들기 위해 필요한 최소 동전 개수를 저장합니다.
dp = [float('inf')] * (k+1)
dp[0] = 0

# 동전의 가치를 하나씩 확인하면서 dp 테이블을 갱신합니다.
for coin in coins:
    for i in range(coin, k+1):
        if dp[i-coin] != float('inf'):
            dp[i] = min(dp[i], dp[i-coin] + 1)

# dp[k]가 무한대인 경우, k원을 만들 수 없는 경우이므로 -1 출력
if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])
