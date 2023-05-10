'''
- 리스트의 in 함수 -> O(n)
- 문제의 조건에서, "1 <= n <= 100,000", "1 <= m <= 100,000"
    - 최악의 경우 시간복잡도 : O(nm) => O(10,000,000,000) => 100억 ❌
- 따라서, 이진 탐색을 사용한다.

'''

import sys

# 이진 탐색
def binary_search(x):
    l, r = 0, n - 1
    while l <= r:
        mid = l + (r - l) // 2
        if a[mid] == x:
            return 1
        
        if a[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return 0

n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

# X라는 정수가 존재하는지 확인
for x in b:
    ret = binary_search(x)
    print(ret)