""" 
- 술래는 1번에서 출발
- 가장 먼 곳 찾기
"""
import heapq
import sys
from collections import defaultdict
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

start = 1
distance[start] = 0
q = []
heapq.heappush(q, (0, start))

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist :
        continue

    for i in graph[now]:
        cost = dist + 1

        if distance[i] > cost :
            distance[i] = cost
            heapq.heappush(q, (cost, i))

# 갈 수 없는 곳 제외하기
for i in range(2, N+1):
    if distance[i] == INF:
        distance[i] = 0

# 가장 먼 곳 찾기
answer = defaultdict(list)
for i in range(2, N+1):
    answer[distance[i]].append(i)

dist = max(answer.keys())
print( answer[dist][0], dist, len(answer[dist]))
