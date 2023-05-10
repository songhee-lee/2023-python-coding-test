'''
[설명]
- 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

[점화식]
- dp[i] = a[i]를 마지막 원소로 가지는 부분 수열의 최대 길이

'''

import sys

# in Dynamic Programming
def __dp_helper():
    # dp 테이블 초기화
    dp = [1] * n 
    
    # 점화식에 따라 dp 테이블 채우기
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    print(max(dp))

# in Binary Search
def __binary_search_helper():
    LIS = [a[0]] # LIS: Longest Increasing Subsequence
    
    # 이진 탐색을 위한 함수
    def binary_search(el):
        l, r = 0, len(LIS) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if LIS[mid] == el:
                return mid
            elif LIS[mid] < el:
                l = mid + 1
            else:
                r = mid - 1
                
        return l

    # LIS 생성
    for el in a:
        # LIS의 마지막 원소보다 el이 크면 LIS에 추가
        if LIS[-1] < a:
            LIS.append(a)
        # LIS의 마지막 원소보다 el이 작으면 LIS의 적절한 위치에 el 삽입
        else:
            idx = binary_search(el=el)
            LIS[idx] = el
            
    print(len(LIS))
    
n = int(input())
a = list(map(int, input().split()))

# dp
__dp_helper()

# binary_search
__binary_search_helper()
