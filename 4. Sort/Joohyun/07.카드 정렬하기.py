import heapq
from sys import stdin

input = stdin.readline
cards = []
result = 0

for i in range(int(input())):
    heapq.heappush(cards, int(input()))

if len(cards) == 1:
    print(0)
else:
    while len(cards) > 1:
        plus = heapq.heappop(cards) + heapq.heappop(cards)
        result += plus
        heapq.heappush(cards, plus)

    print(result)