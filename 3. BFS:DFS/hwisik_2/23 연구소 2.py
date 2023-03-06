'''
- 모든 빈 칸에 바이러스가 있게 되는 최소 시간 -> ✅'BFS'
- 0 : 빈 칸, 1 : 벽, 2 : 바이러스를 놓을 수 있는 칸
- 바이러스를 m개 배치한다. -> 2의 개수와 m이 크지 않으므로, '조합' 사용
- 각 조합마다 BFS를 수행해서, 모든 칸에 바이러스를 퍼트리는데 걸리는 최대 시간을 구한다.
- 모든 조합에서 구한 최대 시간들 중 '최소 시간'을 구한다.

-> ✅다시풀기 (DFS로 바이러스 배치하는 코드는 '시간초과'😿)
'''
from collections import deque
from itertools import combinations
import sys

# BFS
def bfs(virus): # virus : m개 바이러스 배치한 위치
    queue = deque(virus)
    dist = [[-1] * n for _ in range(n)]
    ret = 0 # 모든 칸에 바이러스가 퍼질때 까지 걸리는 최대 시간
    
    # 바이러스기 존재하는 곳의 '거리 = 0'으로 설정
    for x, y in virus:
        dist[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue # 범위 확인
            if graph[nx][ny] == -1 or graph[nx][ny] == 1: continue # 빈 칸 확인
            
            if dist[nx][ny] == -1: # 방문하지 않았고, 빈 칸인 경우
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
                ret = max(ret, dist[nx][ny]) # 최대 시간 갱신
    
    # 모든 빈 칸에 바이러스가 퍼질 수 없는 경우
    for i in range(n):
        for j in range(n):
            if dist[i][j] == -1 and graph[i][j] != 1:
                return float('inf') 
            
    return ret
                
n, m = map(int, input().split())

graph = []

# 방향 정보(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
min_spread_time = float('inf') # 최소 시간을 찾기위해, 최대값으로 설정

for _ in range(n):
    input_data = list(map(int, input().split()))
    graph.append(input_data)

# 바이러스가 존재하는 위치
viruses = set()

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            viruses.add((i, j))

# 바이러스 m개 배치
for virus in combinations(viruses, m):
    # BFS 수행
    min_spread_time = min(min_spread_time, bfs(virus))
    
# 출력
if min_spread_time == float('inf'):
    print(-1)
else:
    print(min_spread_time)