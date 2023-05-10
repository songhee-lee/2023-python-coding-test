'''
- 집이 있는 곳 : 1, 집이 없는 곳 : 0
- 무작위의 집이 있는 곳의 위치를 시작점으로 설정하여 BFS를 수행
- 현재 노드에 연결된 모든 노드에 대해 검사하면서, 
    - 집이라면 방문 표시 / 큐에 추가 / 현재 단지에 포함된 집의 개수 + 1
'''

import sys
from collections import deque

n = int(input())

graph = []
visited = [[0] * n for _ in range(n)] 
ret = []

# 방향 정보(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for _ in range(n):
    input_data = list(input())
    graph.append(input_data)

# BFS
def bfs(i, j):
    queue = deque([(i, j)])
    visited[i][j] = 1
    cnt = 1 # 현재 단지에 포함된 집의 개수
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if visited[nx][ny] == 1 or graph[nx][ny] == '0': continue
            
            visited[nx][ny] = 1 
            queue.append((nx, ny))
            cnt += 1 # 집의 개수 + 1
    return cnt

total_home_count = 0 # 단지의 개수

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == '1':
            out = bfs(i, j)
            ret.append(out)
            total_home_count += 1 # 단지의 개수 + 1

# 출력
print(total_home_count)

# 정렬 후 출력
ret.sort()
for x in ret:
    print(x)