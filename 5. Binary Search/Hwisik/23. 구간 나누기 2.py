'''
- M개 이하의 구간을 나눈다.
- 구간의 점수 : 최대값 - 최솟값
- 어떤 것을 mid로 설정?

-> ✅ 다시풀기
'''

import sys

# 구간 나누기
def get_divided_count(mid):
    min_val = arr[0] # 구간에서 가장 작은 값
    max_val = arr[0] # 구간에서 가장 큰 값
    count = 1 # 구간의 개수
    
    for i in range(1, n):
        max_val = max(max_val, arr[i])
        min_val = min(min_val, arr[i])
        
        # 구간의 점수가 기준값(mid)보다 크면
        # 구간을 나눌 수 있다.
        if max_val - min_val > mid: 
            count += 1 # 구간의 개수 + 1
            max_val = arr[i]
            min_val = arr[i]
        
    return count # 구간의 개수 반환

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

l, r = 0, max(arr)
ret = 0

# 이진 탐색
while l <= r:
    mid = l + (r - l) // 2 # 각 구간의 점수의 최댓값 중 최솟값
    
    # 구간의 개수가 m과 같거나 작다면 => 구간의 점수가 너무 클 때
    if get_divided_count(mid) <= m: 
        ret = mid
        r = mid - 1 # 구간의 점수 줄인다.(=구간의 개수 늘린다), 왼쪽 부분 탐색
        
    # 구간의 개수가 m보다 크다면 => 구간의 점수가 너무 작을 때
    else:
        l = mid + 1 # 구간의 점수 늘린다.(=구간의 개수 줄인다), 오른쪽 부분 탐색
        
print(ret)