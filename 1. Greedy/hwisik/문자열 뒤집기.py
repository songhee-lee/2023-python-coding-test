"""
모든 숫자를 전부 같게 만드는게 문제의 목적이다. 
따라서, 전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에서 더 적은 횟수를 가지는 경우가 답이 된다.
"""

import sys
from collections import deque
from pprint import pprint
import heapq
import copy

# 프로그램 소스코드
data = list(sys.stdin.readline().rstrip())

count0, count1 = 0, 0
if data[0] == '1':
    count1 += 1
else:
    count0 += 1
    
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count1 += 1
        else:
            count0 += 1
            
print(min(count0, count1))  
