'''
- 일반적인 이진 탐색 알고리즘 문제
'''

import sys

# 이진 탐색
def binary_search():
    l, r = 0, n - 1 # 시작점, 끝점 설정
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == mid:
            return arr[mid]
        elif arr[mid] > mid:
            r = mid - 1
        else:
            l = mid + 1
    return -1

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 이진 탐색 결과 출력
print(binary_search())