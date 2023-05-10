'''
- '최소' 키워드가 없으므로 -> 'DFS'
- 적록색약이 아닌 경우는 일반적인 DFS를 수행하고,
    적록색약이라면 'R' -> 'G' or 'G' -> 'R'로 변환해서 DFS를 수행한다.
'''
import sys
sys.setrecursionlimit(10000)

# DFS
def dfs(x, y, color):
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
        if graph[nx][ny] != color or visited[nx][ny]: continue
        
        # 방문하지 않았고, 색깔이 같은 경우
        dfs(nx, ny, color)
    
n = int(input())

graph = []

# 방향 정보(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    input_data = list(input().rstrip())
    graph.append(input_data)

# 적록색약 ❌
visited = [[0] * n for _ in range(n)]
non_weak_count = 0 # 구역 수

# DFS
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            non_weak_count += 1
            
            
# 적록색약 ⭕️
visited = [[0] * n for _ in range(n)]
weak_count = 0 # 구역 수

# 빨간색과 초록색을 같은 색으로 처리
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

# DFS
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            weak_count += 1

# 출력
print(non_weak_count, weak_count)