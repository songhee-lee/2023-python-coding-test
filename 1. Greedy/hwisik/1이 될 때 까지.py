"""
‘n을 k로 최대한 많이 나누는 것’에 초점을 맞췄다.
"""

import sys
from collections import deque
import time

sys.setrecursionlimit(10000)

start_time = time.time() # 측정 시작
# 프로그램 소스코드

n, k = map(int, sys.stdin.readline().split()) # n, m을 공백으로 구분하여 입력받기
ret = 0

# n이 1이 아닐 때 까지 계속 연산하기
while n != 1:
    if n % k == 0: # n이 k로 나누어 떨어진다면
        n //= k # k로 나누기
    else: # 나누어 떨어지지 않는다면
        n -= 1 # n에서 1씩 빼기
    ret += 1
    
print(ret)

end_time = time.time() # 측정 종료
print("Time: ", end_time - start_time) # 수행 시간 출력
