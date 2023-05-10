'''
- 최소 힙을 사용한다.
    - 두 묶음을 더한 것을 다시 덧셈에 활용하므로...
- 최소한의 비교를 하려면, 카드의 수가 작은 것 부터 빼서 합쳐야 한다.
- 두 묶음을 뺴서 합을 구해서 sums에 저장한다.
- 두 묶음의 합을 최소 힙에 다시 넣는다.
'''
import sys
import heapq

n = int(sys.stdin.readline())

cards = []
for _ in range(n):
    cards.append(int(sys.stdin.readline()))

# cards 리스트를 최소 힙으로 만든다.    
heapq.heapify(cards)

sums = 0 # 최소 비교 횟수

while len(cards) >= 2:
    cur = heapq.heappop(cards) + heapq.heappop(cards) # 두 묶음을 합친다.
    sums += cur # 비교 횟수 갱신
    heapq.heappush(cards, cur) # 다음 비교를 위해서, 합친 두 묶음을 힙에 넣는다.

# 출력
print(sums)