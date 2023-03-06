from collections import deque

def bfs(x, y):
    visited = [[0] * m for _ in range(n)]
    queue = deque([(x, y)])
    
    dist[x][y] = 0
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if graph[nx][ny] == 1 or visited[nx][ny]: continue
            
            dist[nx][ny] = min(dist[nx][ny], dist[x][y] + 1)
            visited[nx][ny] = 1
            queue.append((nx, ny))
    
n, m = map(int, input().split())

graph = []

# 방향 정보(왼쪽 위 대각선 ~)
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]

for _ in range(n):
    input_data = list(map(int, input().split()))
    graph.append(input_data)

INF = float('inf')
dist = [[INF] * m for _ in range(n)] # 각 칸의 안전 거리의 최솟값 

safe_dist = 0 # 안전 거리

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)
            
# 안전거리의 최댓값 구하기
for i in range(n):
    safe_dist = max(safe_dist, max(dist[i]))
    
# 출력
print(safe_dist)