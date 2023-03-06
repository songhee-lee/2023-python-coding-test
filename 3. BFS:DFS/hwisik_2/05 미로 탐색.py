'''
*** 최소의 칸 수를 구하는 문제이므로 ✅'BFS'를 사용한다.
1. (1, 1)에서 시작해서 (N, M)으로 이동한다.
2. 서로 인접한 칸으로만 이동이 가능하다.
    - '1'은 이동할 수 있는 칸
    - '0'은 이동할 수 없는 칸
'''

from collections import deque

n, m = map(int, input().split())

graph = []
visited = [[0] * m for _ in range(m)]
dist = [[-1] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    input_data = list(input())
    graph.append(input_data)
    
def bfs():
    queue = deque([(0, 0)]) # (1, 1)에서 시작 - 문제의 조건
    dist[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if dist[nx][ny] != -1: continue
            if graph[nx][ny] == '0': continue
            
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))
            
    return dist[n - 1][m - 1]

out = bfs()

print(out)