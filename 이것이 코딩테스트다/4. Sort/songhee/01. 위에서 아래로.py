"""
- 큰 수부터 작은 수의 순서로 정렬하기
"""

N = int(input())
q = []
for _ in range(N):
    q.append(int(input()))

print(*sorted(q, reverse=True))