'''
- 수열 A의 크기 : N (1 <= N <= 1,000,000)
- 가장 긴 증가하는 부분 수열을 저장할 리스트 선언
    - 이 리스트에 이진탐색을 수행한다.(배열 A에 수행 X)
- A를 순회하면서, 
    - 현재 원소가 LIS의 마지막 원소보다 작거나 같다면 
        이진탐색으로 LIS의 어디 위치에 들어갈지 판단
    - 현재 원소가 LIS의 마지막 원소보다 크다면
        현재 원소를 LIS 끝에 붙인다.(이진탐색 X)

-> ✅다시풀기
'''

import sys

# 이진 탐색
def binary_search(el):
    l, r = 0, len(LIS) - 1
    
    # el이 어디에 들어갈지, 인덱스 판단
    while l <= r:
        mid = l + (r - l) // 2
        if LIS[mid] == el:
            return mid
        elif LIS[mid] < el:
            l = mid + 1
        else:
            r = mid - 1
            
    return l

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

LIS = [a[0]] # 최장 증가 부분 수열 리슷트

# 리스트 a 순회
for el in a:
    if LIS[-1] < el: # LIS의 마지막 원소보다 크다
        LIS.append(el)
    
    # LIS의 마지막 원소보다 작거나 같다.
    # 적절한 인덱스 찾는다.(이진탐색 수행)
    else:
        idx = binary_search(el)
        LIS[idx] = el
    print(LIS)
    
print(len(LIS))
