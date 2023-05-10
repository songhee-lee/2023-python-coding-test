'''
[설명]
- 예를 들어 수열 A = {10, 30, 10, 20, 20, 10}인 경우에
    가장 긴 감소하는 부분 수열은 {30, 20, 10}이고, 길이는 3이다.
    
[점화식]
- dp[i] = max(dp[i], dp[j] + 1)
    -> i번째 원소를 마지막으로 하는 가장 긴 감소하는 부분 수열의 길이
'''

n = int(input())
a = list(map(int, input().split()))

# dp[i] : i번째 원소를 마지막으로 하는 가장 긴 감소하는 부분 수열의 길이
dp = [1] * n # 초기화

for i in range(1, n):
    for j in range(i):
        if a[i] < a[j]: # LIS와 다른 부분(부등호 방향)
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))