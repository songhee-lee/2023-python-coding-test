# .ref

t = int(input())
k = int(input())
coins = [list(map(int, input().split())) for _ in range(k)]

dp = [0] * (t + 1)
dp[0] = 1


def fail_logic():
  for coin, cnt in coins:
    for j in range(coin, t + 1): # 왜 coin부터 t원까지로 설정하면 안되는가?
      for i in range(1, cnt + 1):
        if j <= coin * i:
          dp[j] += dp[coin * i - j]
          
def success_logic():
  for coin, cnt in coins:
    for j in range(t, 0, -1): # 왜 t원부터 돌려야 하는가?
      for i in range(1, cnt + 1):
        if j >= coin * i:
          dp[j] += dp[j - coin * i]
          
success_logic()
# fail_logic()

print(dp[t])
