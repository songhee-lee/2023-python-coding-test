import sys
from collections import deque
from pprint import pprint
import heapq
import copy

# 프로그램 소스코드
n = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().rstrip().split()))

coins.sort()

target = 1 # 만들 수 있는 금액

for coin in coins:
    if target < coin: # 만들 수 없는 금액을 찾았을 때 반복 종료
        break
    target += coin
print(target) # 만들 수 없는 금액 출력