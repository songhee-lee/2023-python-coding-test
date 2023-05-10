'''
1. 현재 노드에 연결된 다음 노드를 탐색한다.
2. 다음 노드가 있다면
    2-1. 다음 노드를 방문하지 않았다면, 다음 노드를 큐에 추가하고, 최단거리를 갱신한다.
3. 다음 노드가 없다면, 큐에서 가장 왼쪽의 노드를 현재 노드로 갱신하고 큐가 비지 않을 때 까지 (1)부터 반복한다. 
'''

from collections import deque
import sys

# SOL - 1
# BFS
def bfs(x):
    queue = deque([x]) 
    
    while queue:
        cur = queue.popleft() # 현재 노드
        
        # 현재 노드에 연결되어 있는 모든 노드 탐색
        for nxt in graph[cur]:
            if dist[nxt] == INF: # 방문하지 않은 노드라면
                dist[nxt] = dist[cur] + 1 # 최단거리 갱신
                queue.append(nxt) 
                
# 입력
n, m, k, x = map(int, sys.stdin.readline().split())

INF = float('inf') # 방문하지 않았음을 표시하는 변수
dist = [INF] * (n + 1) # 모든 노드의 최단거리 초기화
graph = [[] for _ in range(n + 1)]

# 출발 도시의 최단 거리는 0
dist[x] = 0

# 도시 간선 정보 입력
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

# bfs 수행
bfs(x)

# 최단 거리가 K인 노드의 리스트
ret = []

# 최단 거리가 K인 노드 찾기
for i in range(1, n + 1):
    if dist[i] == k:
        ret.append(i)


if ret: # 최단 거리가 K인 노드가 있다면
    for node in ret:
        print(node)
else: # 없다면
    print(-1)
    
########################################################################################
# SOL - 2
def bfs(x):
    queue = deque([x])
    visited[x] = 1
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = 1
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)
    

n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

visited = [0] * (n + 1)
dist = [0] * (n + 1)

bfs(x)

ret = []
for i, d in enumerate(dist):
    if d == k:
        ret.append(i)
        
if not ret:
    print(-1)
else:
    for d in ret: print(d)