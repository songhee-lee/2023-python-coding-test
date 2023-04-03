""" 
- 수열의 증가하는 부분 수열 중 합이 가장 큰 것
"""

N = int(input())
arr = list(map(int, input().split()))

# dp[x] : x번째까지 수열의 증가 부분 수열 합
dp = [ x for x in arr ] 

# Bottom-up
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i] and dp[j]+arr[i] > arr[i]:
            dp[i] = dp[j]+arr[i]

print(max(dp))