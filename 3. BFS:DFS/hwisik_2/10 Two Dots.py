'''
- 게임판 크기 : N * M
- 점 k개 d1, d2, ..., dk로 이루어진 사이클의 정의
    - 모든 k개의 점은 서로 다르다. 
    - k는 4보다 크거나 같다.
    - 모든 점의 색은 같다.
    - 모든 1 ≤ i ≤ k-1에 대해서, di와 di+1은 인접하다. 
        - 또, dk와 d1도 인접해야 한다. 
        - 두 점이 인접하다는 것은 각각의 점이 들어있는 칸이 '변을 공유한다'는 의미이다.
        
[아이디어]
- 사이클 찾기 : 특정 알파벳의 사이클을 찾을 떄, 위치를 set에 저장한다. 
                만약, 다음 위치가 이미 set에 있다면 사이클이 존재한다. 
                추가로, 모든 위치에 대하여 DFS, BFS를 수행해야 한다. -> 사이클을 이루는 모든 K개의 점은 서로 다르다는 조건떄문..
'''
from collections import deque

def dfs(dot_type, x, y, cnt, sx, sy):
    global is_cycle
    
    # 사이클이 있다면
    if is_cycle: 
        return
    
    visited[sx][sy] = 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        if cnt >= 4 and nx == sx and ny == sy:
            is_cycle = True
            return
        if graph[nx][ny] == dot_type and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(dot_type, nx, ny, cnt + 1, sx, sy)
            visited[nx][ny] = 0
            
n, m = map(int, input().split())

graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * m for _ in range(n)]

for _ in range(n):
    input_data = list(input())
    graph.append(input_data)

is_cycle = False
for i in range(n):
    for j in range(m):
        sx, sy = i, j
        if not visited[i][j]:
            dfs(graph[i][j], i, j, 1, sx, sy)
        
        if is_cycle:
            break
    if is_cycle:
        break

if is_cycle:
    print('Yes')
else:
    print('No')