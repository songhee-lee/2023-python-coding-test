# 음수를 모르고 20을 넘는 수는 모른다.

n = int(input())
nums = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n)]
dp[0][nums[0]] = 1

for i in range(1, n - 1):
  for num in range(21):
    if dp[i - 1][num] != 0:
      _sum = num + nums[i]
      _sub = num - nums[i]
      
      if _sum <= 20:
        dp[i][_sum] += dp[i - 1][num]
      if _sub >= 0:
        dp[i][_sub] += dp[i - 1][num]

print(dp[n - 2][nums[-1]])