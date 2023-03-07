'''
- 모든 방문하지 않는 섬의 위치에 대해서 BFS를 수행한다.
- 문제의 이동 규칙에 맞게 다음 섬의 위치를 설정한다.
- 방문하지 않았고 범위를 벗어나지 않는다면, 방문 표시를 하고 큐에 추가한다.
- BFS가 끝나면, (섬의 개수 + 1)
'''
from collections import deque

dx = [-1, 1, 0, 0, -1, 1, -1, 1] 
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w: continue
            if visited[nx][ny] or graph[nx][ny] == 0: continue
            
            visited[nx][ny] = 1
            queue.append((nx, ny))
            
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break # 종료 조건
    
    graph = [[] * w for _ in range(h)] 
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        graph[i] = list(map(int, input().split()))
    
    connected_island_count = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == 1:
                bfs(i, j)
                connected_island_count += 1
                
    print(connected_island_count)