'''

'''
from copy import deepcopy
from collections import deque

# 현재 위치의 범위 확인
def is_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return True

# 바이러스 퍼트리기
def bfs():
    queue = deque()
    copy_graph = deepcopy(graph)
    
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if not is_range(nx, ny): continue
            if copy_graph[nx][ny] != 0: continue
            
            copy_graph[nx][ny] = 2
            queue.append((nx, ny))
        
    global ret    
    safe_zone_cnt = 0
    for i in range(n):
        safe_zone_cnt += copy_graph[i].count(0)
        
    ret = max(ret, safe_zone_cnt)
# 벽 세우기
def set_wall(wall_cnt):
    if wall_cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                set_wall(wall_cnt + 1)
                graph[i][j] = 0
                
n, m = map(int, input().split())


# 방향 정보(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []

# 연구소 정보 입력
for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

ret = 0 
set_wall(0)
print(ret)