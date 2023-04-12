""" 
- N개의 섬에 다리가 설치되어 차가 다닐 수 있다.
- 각 다리별 중량 제한이 있을 때, 한 번의 이동에서 옮길 수 있는 물품들의 중량 최댓값 구하기
"""
from collections import deque
import sys
input = sys.stdin.readline

def bfs(limit):
    visited = [False] * (N+1)
    visited[start] = True
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        if now == end:
            return True
        for next, weight in graph[now]:
            if not visited[next] and limit <= weight:
                q.append(next)
                visited[next] = True
    return False

N, M = map(int, input().split())
graph = [ [] for _ in range(N+1) ]
s, e = 1, 0
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    if e < c:
        e = c 
start, end = map(int, input().split())

# 그래프 정렬
for i in range(1, N+1):
    graph[i].sort(reverse=True)

# 이진 탐색
while s <= e :
    m = (s+e) // 2

    if bfs(m) :
        s = m+1
    else:
        e = m-1

print(int(e))