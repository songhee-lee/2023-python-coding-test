"""
target은 만들 수 있는 금액을 저장하는 변수이다. 초기값은 1이다.(만들 수 없는 양의 정수 금액 중 최솟값을 찾아야 하므로)
아이디어는 다음과 같다. 일단 동전에 대한 정보를 화폐 단위를 기준으로 오름차순으로 정렬한다.
이후에 1부터 차례대로 특정한 금액을 만들 수 있는지를 확인한다.

1부터 target - 1까지의 모든 금액을 만들 수 있다고 가정해보자. 화폐 단위가 작은 순서대로 동전을 확인하며, 현재 확인하는 동전을 이용해 target 금액 또한 만들 수 있는지 확인한다. 만약 target 금액을 만들 수 있다면, target 값을 업데이트하는(증가시키는) 방식을 이용한다.

자세한 과정은 다음과 같다.
0. 처음에는 금액 1을 만들 수 있는지 확인하기 위해, target = 1로 설정한다.
1. target = 1을 만족할 수 있는지 확인한다. 화폐 단위가 x인 동전이 있다고 가정하고 1을 만들 수 있다면 target = 1 + x로 업데이트 한다.(x까지의 모든 금액을 만들 수 있다는 말과 같다.)
2. target = 1 + x를 만족할 수 있는지 확인한다. 현재 화폐 단위가 y인 동전이 1 + x 보다 크다면 1 + x를 만들 수 있는 방법은 없다. 따라서 정답은 1 + x가 된다.
"""


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
