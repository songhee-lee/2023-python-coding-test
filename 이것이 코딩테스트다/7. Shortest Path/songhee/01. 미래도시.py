""" 
- 1번 -> K번 -> X번 까지의 최소 시간 계산하기
- X에 도달할 수 없으면 -1 리턴
"""
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())    # 노드 / 간선 개수
graph = [[] for _ in range(N+1)]    # 그래프
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
distance = [INF] * (N+1)            # 최단 거리 테이블
X, K = map(int, input().split())    # 도착지, 중간지점

q = []
start = 1
distance[start] = 0
heapq.heappush(q, (0, start, set([1])))
while q:
    dist, now, nodes = heapq.heappop(q)

    if distance[now] < dist :
        continue

    for i in graph[now]:
        cost = dist + 1

        if i == X and K not in nodes:
            continue

        if cost < distance[i]:
            distance[i] = cost
            nodes.add(i)
            heapq.heappush(q, (cost, i, nodes))

print(-1) if distance[X] == INF else print(distance[X])
