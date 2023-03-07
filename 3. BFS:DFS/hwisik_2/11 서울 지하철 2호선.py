'''
1. 순환선(=사이클)에 포함되는 노드들을 먼저 파악한다. (= 사이클을 만든다)
2. 순환선에 포함되지 않는 노드에서 순환선에 포함되는 노드들까지의 거리의 최솟값을 구한다.

✅ 사이클은 DFS, 거리 계산은 최소거리를 구하는 것이므로 BFS
❌ 시간 초과
'''

from collections import deque
import sys

sys.setrecursionlimit(1000000) # - RecursionError 방지

# 사이클 만들기 - DFS
def make_cycle(start, end, cnt):
    if cnt >= 2 and start == end: # 사이클이 있는 경우
        dist[start] = 0
        return
    
    visited[end] = 1 # 방문 표시
    
    for nxt in graph[end]:
        if not visited[nxt]: # 방문한적이 없는 경우
            make_cycle(start, nxt, cnt + 1)
        elif nxt == start and cnt >= 2: # 사이클이 존재한다면
            dist[start] = 0
            return

# 거리 계산 - BFS
def calculate_dist():
    queue = deque()
    
    for i in range(n): # 사이클에 포함되는 노드들은 거리가 0 이다.
        if not dist[i]:
            queue.append(i)
    
    while queue:
        start = queue.popleft()
        for nxt in graph[start]: 
            if dist[nxt] == -1: # 거리 갱신을 하지 않았다면
                dist[nxt] = dist[start] + 1 # 거리 갱신
                queue.append(nxt)

n = int(sys.stdin.readline())

graph = [[] for _ in range(n)] # 노드-간선 정보 배열
dist = [-1] * n # 거리 배열

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    
    # 양방향 간선 의미
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
    

for i in range(n):
    visited = [0] * n # 방문 표시 배열
    
    # 사이클 만들기
    make_cycle(i, i, 0)

calculate_dist() # 거리 계산

# 출력
for d in dist:
    print(d, end=' ')