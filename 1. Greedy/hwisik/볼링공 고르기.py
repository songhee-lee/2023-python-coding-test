"""
combinations(…)을 사용하여 모든 조합을 구한 뒤, 안의 데이터를 순회하면서 두 볼링공의 무게가 같지 않을 때 ret 값을 1 증가시키는 방식으로도 가능하다.
"""

import sys
from collections import deque
from pprint import pprint
import heapq
import copy
from itertools import combinations

# 프로그램 소스코드
n, m = map(int, sys.stdin.readline().split())
w = list(map(int, sys.stdin.readline().rstrip().split()))


ret = 0
c = combinations(w, 2) # 가능한 모든 조합을 구한다.
for data in c:
    if data[0] != data[1]: # 만약 선택한 두 볼링공의 무게가 같지 않다면
        ret += 1 # 조합 개수 1 증가시킨다.
print(ret)
