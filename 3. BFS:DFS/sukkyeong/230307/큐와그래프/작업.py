
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
for i in range(1, n+1):
    tmp_lst = list(map(int, input().split()))
    for num in tmp_lst[1:]:
        dp[i] = max(dp[i], dp[num] + tmp_lst[0])
print(max(dp))
