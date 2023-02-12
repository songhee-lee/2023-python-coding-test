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