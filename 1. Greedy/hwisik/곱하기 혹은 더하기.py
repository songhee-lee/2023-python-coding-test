import sys
from collections import deque
from pprint import pprint
import heapq
import copy

# 프로그램 소스코드
nums = list(sys.stdin.readline().rstrip())

total = int(nums[0]) # 첫 번째 문자를 숫자로 변경해서 대입
for i in range(1, len(nums)):
    cur = int(nums[i])
    if cur <= 1 or total <= 1: # 두 수 중에서 하나라도 0 혹은 1인 경우, 덧셈 수행
        total += cur
    else:
        total *= cur
print(total)