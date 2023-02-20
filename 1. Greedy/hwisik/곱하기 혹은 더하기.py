"""
일반적으로 곱셈이 덧셈보다 더 큰 수를 만들 수 있다.
하지만 만약 어떤 수가 0일 때는 결과를 0으로 만드므로 덧셈을 수행해야 한다.
또는 어떤 수가 1일 때는 곱셈일 경우 결과 그대로가 되지만, 덧셈일 경우 결과 = 결과 + 1 이 된다.

따라서, 어떤 수가 0이나 1이 아닐 경우, 즉 1보다 작거나 같을 경우에는 덧셈을 수행하고 아니라면 곱셈을 수행하면 항상 최적의 해를 찾을 수 있다.

위 코드에서 total은 모든 연산의 결과를 저장하는 변수이다.
배열의 첫번째 값으로 초기화를 한 이유는 배열의 첫번째 값이 1보다 작거나 같을 경우가 있을 수 있기 때문이다.
"""

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
