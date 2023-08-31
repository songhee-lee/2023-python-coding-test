# 얻을 수 있는 최대 기쁨구하기
# 다시 풀기
# 현재 얻을 수 있는 기쁨은, 이전 사람에게 인사를 했을 때 또는 인사를 하지 않았을 때가 영향을 준다.
n = int(input())
L = [0] + list(map(int, input().split()))
J = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(101)] for _ in range(n + 1)]

# 현재 체력보다 읽는 체력이 같거나 많다. -> 현재 기쁨은 이전 기쁨
# 현재 체력이 더 많다 -> 현재 기쁨은 '체력을 깎지 않은 이전 기쁨' / '체력을 깎은 이전 기쁨 + 현재 기쁨' 중 큰 값
for i in range(1, n + 1):
    for j in range(1, 101): # 체력(1~100)
        if L[i] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - L[i]] + J[i])
        else:
            dp[i][j] = dp[i - 1][j]
            
print(dp[n][99])