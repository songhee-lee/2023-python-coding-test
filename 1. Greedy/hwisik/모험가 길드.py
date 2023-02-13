"""
처음 작성한 코드에서는 [2, 3, 3, 3, 3, 4]를 순회한다고 가정하면,
[2, 3]이 하나의 그룹이 된다고 생각했다. 하지만 이는 문제의 조건에 위배된다.

문제의 조건에서 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹이어야 한다.
[2, 3]에서 공포도가 3인 모험가는 반드시 3명 이상으로 구성되어야 하므로 옳지 않다.

그래서 새로 작성한 코드의 알고리즘은, 
공포도가 저장된 배열을 순회하면서, cnt 값을 1 증가시킨다.
만약, 현재 모험가의 공포도보다 cnt가 크거나 같다면, 그룹을 만들 수 있으므로 ret 값을 1 증가시킨다.
그리고 다른 그룹을 만들기 위해 cnt를 0으로 초기화한다.
"""

import sys
from collections import deque
from pprint import pprint
import heapq
import copy

# 프로그램 소스코드
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0 # 현재 포함되어 있는 모험가 수
arr.sort()
ret = 0 # 만들 수 있는 최대 그룹 수

for i in arr:
    cnt += 1
    if cnt >= i:
        ret += 1
        cnt = 0
print(ret)
