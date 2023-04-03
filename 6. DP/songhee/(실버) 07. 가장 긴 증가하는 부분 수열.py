""" 
- 수열 A에서 가장 긴 증가하는 부분 수열 구하기
"""

N = int(input())
arr = list(map(int, input().split()))

# dp[x] : x번째까지의 가장 긴 증가하는 부분 수열 길이
dp = [1] * N

for i in range(N):
    for j in range(i):
        # 증가하는 수열일 때, 
        # j번째에 i 추가하는 것과 현재 i번째까지의 수열 중 더 긴 것으로 업데이트
        if arr[j] < arr[i] and dp[j]+1 > dp[i]:
            dp[i] = dp[j]+1

print(max(dp))