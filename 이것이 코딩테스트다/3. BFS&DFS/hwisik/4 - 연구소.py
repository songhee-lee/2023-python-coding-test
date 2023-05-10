'''
1. 먼저, 벽을 3개 세운다.(완전 탐색)
2. 현재 바이러스가 있는 위치를 큐에 모두 저장한다.
3. 바이러스의 위치를 하나씩 꺼내서, (상, 하, 좌, 우)를 살피면서 전파시킨다.
4. 모두 전파시킨 뒤, 안전영역의 크기를 계산한다.
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
    copy_graph = deepcopy(graph) # 바이러스 퍼트리기 위해 deepcopy
    
    # 큐에 바이러스 위치 저장
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        
        # 상, 하, 좌, 우 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if not is_range(nx, ny): continue
            if copy_graph[nx][ny] != 0: continue
            
            copy_graph[nx][ny] = 2 # 바이러스 퍼트린다.
            queue.append((nx, ny))
        
    global ret    
    
    safe_zone_cnt = 0
    for i in range(n): # 안전 영역의 크기 구한다.
        safe_zone_cnt += copy_graph[i].count(0)
        
    ret = max(ret, safe_zone_cnt) # 최대 안전 영역의 크기 구한다.
# 벽 세우기
def set_wall(wall_cnt):
    if wall_cnt == 3: # 벽을 다 세웠다면
        bfs() # BFS 수행
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0: # 빈 칸이라면
                graph[i][j] = 1 # 벽을 세운다.
                set_wall(wall_cnt + 1) # 다음 위치 선정을 위해 재귀 호출
                graph[i][j] = 0 # 벽을 허문다.
                
n, m = map(int, input().split())


# 방향 정보(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []

# 연구소 정보 입력
for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

ret = 0 # 최대 안전 영역 크기
set_wall(0) # 벽 세우는 시뮬레이션 시작

print(ret) # 출력