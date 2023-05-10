'''
- 일반적인 이진탐색 알고리즘 사용
- 찾고자 하는 수 == cards[mid]랄면 return 1
- 찾고자 하는 수가 cards[mid]보다 작다면, mid를 줄여야하므로 r = mid - 1
- 찾고자 하는 수가 cards[mid]보다 크다면, mid를 늘려야하므로 l = mid + 1
'''

import sys

# 이진 탐색
def binary_search(target):
    l, r = 0, n - 1
    
    while l <= r:
        mid = l + (r - l) // 2
        if cards[mid] == target: # 찾고자 하는 수가 있으면
            return 1
        elif cards[mid] > target: # 찾고자 하는 수보다 크다면, 오른쪽 부분탐색
            r = mid - 1
        else: # 찾고자 하는 수보다 작다면, 왼쪽 부분탐색
            l = mid + 1
            
    return 0 # 찾고자 하는 수가 없으면

n = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
to_check = list(map(int, sys.stdin.readline().split()))

# 이진 탐색 수행 & 출력
for target in to_check:
    print(binary_search(target), end=' ')