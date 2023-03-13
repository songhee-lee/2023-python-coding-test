
""" 
- A와 B 한 묶음 만들기 : len(A) + len(B)
"""
import heapq

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

heapq.heapify(numbers)
answer = 0
while len(numbers) != 1 :
    # 수가 작은 카드 묶음부터 차례로 합치기
    summation = heapq.heappop(numbers)+heapq.heappop(numbers)
    answer += summation
    heapq.heappush(numbers, summation)

print(answer)

