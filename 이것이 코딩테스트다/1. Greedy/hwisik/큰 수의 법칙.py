"""
합이 최대로 되게 하려면 가장 큰 수를 k개만큼 더하고 두번째로 큰 수를 한 번 더하는 방법을 반복한다.
예를 들어 m = 8, k = 3이라면 합이 최대가 되게 하려면
⇒ 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5
"""

import sys
from collections import deque
import time

sys.setrecursionlimit(10000)

start_time = time.time() # 측정 시작
# 프로그램 소스코드

n, m, k = map(int, sys.stdin.readline().split()) # n, m, k를 공백으로 구분하여 입력받기
nums = list(map(int, sys.stdin.readline().split())) # n개의 수를 공백으로 구분하여 입력받기
nums.sort(reverse=True) # 입력받은 수 정렬하기
ret = 0
copy_k = k

while m: # m이 0보다 클 때 까지 -> 0이 되면 더 이상 더할 수 없으므로
    max_num = nums[0] # 가장 큰 수
    while copy_k: # 가장 큰 수를 k(copy_k)번 더하기
       ret += max_num
       copy_k -= 1
       m -= 1 # 더할 때 마다 1씩 빼기
    ret += nums[1] # 두번째로 큰 수 한 번 더하기
    m -= 1 # 더할 때 마다 1씩 뺴기
    copy_k = k # copy_k를 다시 원래 값으로 복구
print(ret)

end_time = time.time() # 측정 종료
print("Time: ", end_time - start_time) # 수행 시간 출력
