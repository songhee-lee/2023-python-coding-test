""" 
N개의 카드 중 특정 숫자가 몇 개인지 구하기
"""
import sys
from collections import Counter

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
M = int(input())
counts = list(map(int, sys.stdin.readline().split()))

# 숫자 카드별 개수 구하기
counting_list = Counter(numbers)

print(*[counting_list[c] if c in counting_list else 0 for c in counts ])