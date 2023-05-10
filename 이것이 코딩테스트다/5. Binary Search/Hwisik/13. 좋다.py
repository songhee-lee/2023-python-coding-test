'''
- 리스트 A를 정렬.
- 리스트 A를 순회하면서, 특정 원소 선택.
- 선택한 원소를 제외한 리스트 생성.
- 새로운 리스트에서 투 포인터 이용.
    - 투 포인터를 이용한 두 원소의 합이 제외한 원소와 같다면, '좋은 수 += 1'
    - ... 작다면, l += 1
    - ... 크다면, r -= 1

'''

import sys
from collections import Counter

def binary_search():
    count = 0
    for i in range(n):
        except_i_a = a[:i] + a[i + 1:]
        l, r = 0, len(except_i_a) - 1
        
        while l < r:
            sums = except_i_a[l] + except_i_a[r]
            if sums == a[i]:
                count += 1
                break
            
            if sums < a[i]: l += 1
            else: r -= 1
            
    return count

n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))

ret = binary_search()

print(ret)