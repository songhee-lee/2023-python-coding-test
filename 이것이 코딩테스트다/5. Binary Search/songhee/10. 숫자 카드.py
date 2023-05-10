""" 
- N개 카드 중 M개 숫자 카드를 가지고 있는지 아닌지 구하기
"""

N = int(input())
cards = set(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

print(*[ 1 if x in cards else 0 for x in numbers])
