'''
- 안전거리 : 그 칸과 가장 거리가 가까운 아기 상어와의 거리 -> ✅'BFS'
- 상어는 여러 마리가 존재한다. 따라서, 각 상어의 위치마다 안전거리를 구해서 갱신해야 한다.
- 여기서는 '거리 배열이 방문 표시 배열의 역할을 할 수 없다?'
'''
from collections import deque

# BFS
def bfs(x, y):
    # 각 상어의 위치마다 안전거리를 구해야 하므로 
    # 방문 표시 배열을 BFS안에 선언
    visited = [[0] * m for _ in range(n)]
    queue = deque([(x, y)])
    
    # 현재 상어가 위치한 곳의 안전 거리 = 0, 방문 표시
    dist[x][y] = 0 
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if graph[nx][ny] == 1 or visited[nx][ny]: continue
            
            dist[nx][ny] = min(dist[nx][ny], dist[x][y] + 1) # 안전 거리 갱신
            visited[nx][ny] = 1 # 방문 표시
            queue.append((nx, ny))
    
n, m = map(int, input().split())

graph = []

# 방향 정보(왼쪽 위 대각선, ...)
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]

for _ in range(n):
    input_data = list(map(int, input().split()))
    graph.append(input_data)

# 안전 거리는 최소거리이므로 초기값을 inf로..
INF = float('inf')

dist = [[INF] * m for _ in range(n)] # 각 칸의 안전 거리의 최솟값 

safe_dist = 0 # 안전 거리

# 각 상어마다 BFS 수행
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)
            
# 안전거리의 최댓값 구하기
for i in range(n):
    safe_dist = max(safe_dist, max(dist[i]))
    
# 출력
print(safe_dist)