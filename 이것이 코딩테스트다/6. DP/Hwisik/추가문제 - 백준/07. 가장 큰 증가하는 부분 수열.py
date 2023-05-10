'''
[설명]
- 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
- 예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8}인 경우에
    합이 가장 큰 증가하는 부분 수열은 {1, 2, 50, 60}이고, 합은 113이다.

[점화식]
- dp[i] = max(dp[i], dp[j] + 1)
- _sum[i] = max(_sum[i], _sum[j] + a[i])
'''

n = int(input())

a = list(map(int, input().split()))

dp = [1] * n  # dp[i]: a[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
_sum = [el for el in a]  # _sum[i]: a[i]를 마지막 원소로 가지는 부분 수열의 최대 합


for i in range(1, n):
    for j in range(i):
        # 현재 원소 : a[i], 비교하려는 이전 원소 : a[j]
        if a[i] > a[j]:
            
            # 길이가 가장 긴 증가하는 부분 수열을 구하는 것이므로
            dp[i] = max(dp[i], dp[j] + 1)
            
            # 합이 가장 큰 증가하는 부분 수열을 구하는 것이므로
            _sum[i] = max(_sum[i], _sum[j] + a[i])

print(max(_sum))
