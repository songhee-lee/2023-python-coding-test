""" 
- 가장 긴 감소하는 부분 수열 구하기
- O(N logN)
"""
from bisect import bisect_left

# 입력 받기
N = int(input())
arr = list(map(lambda x: int(x) * -1, input().split()))

# dp[i] : i번째 까지 중 감소하는 수열 마지막 원소의 최댓값
dp = [arr[0]]

#
for i in range(N):
    # i번째 원소가 수열의 마지막 원소보다 작은 경우 
    if arr[i] > dp[-1] :
        dp.append(arr[i])   # 수열에 추가
    # 마지막 원소보다 큰 경우
    else:
        # i번째 원소가 들어갈 자리 탐색 후 넣기
        idx = bisect_left(dp, arr[i]) 
        dp[idx] = arr[i]

print(len(dp))


