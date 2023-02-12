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