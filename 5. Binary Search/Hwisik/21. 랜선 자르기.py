'''
- 최대 랜선의 길이 구하기 -> 랜선을 최대한 짧게 자른다.
- 랜선의 가능 길이 => 1 ~ 입력으로 주어진 랜선 길이의 최대값
'''

import sys

def binary_search():
    l, r = 0, lans[-1]
    while l <= r:
        cutted_count = 0
        mid = l + (r - l) // 2
        
        for lan in lans:
            cutted_count += lan // mid
        
        if cutted_count >= n: l = mid + 1
        else: r = mid - 1
            
    return r

k, n = map(int, sys.stdin.readline().split())
lans = sorted(list(int(sys.stdin.readline()) for _ in range(k)))

ret = binary_search()

print(ret)