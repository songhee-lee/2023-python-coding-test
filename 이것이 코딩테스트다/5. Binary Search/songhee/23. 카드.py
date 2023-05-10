""" 
- 가장 많이 가지고 있는 정수 구하기
"""
from collections import Counter

N = int(input())
numbers = [ int(input()) for _ in range(N) ]

numbers_cnt = sorted(Counter(numbers).most_common(), key=lambda x: (-x[1], x[0]))
print(numbers_cnt[0][0])
