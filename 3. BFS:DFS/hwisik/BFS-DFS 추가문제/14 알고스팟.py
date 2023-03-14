'''
- 0 : 빈 방, 1 : 벽
- M : 가로(열), N : 세로(행)
-> (N, M)에 도착하기 위해 부셔야 하는 최소 벽의 개수를 구하자! -> ✅'BFS'

✅ 벽을 최소로 부시기 위해, 특정 칸이 0일 경우 appendleft, 1일 경우 append를 한다.
    -> '빈 방'을 '우선으로 탐색한다'는 의미?

-> ✅'다시풀기'
'''

from collections import deque
import sys
        
# BFS    
def bfs():
    queue = deque([(0, 0)]) # 초기 위치 추가
    wall[0][0] = 0 # 초기 위치의 부순 벽의 개수
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            
            if wall[nx][ny] == -1: # 방문한 적이 없는 경우
                if graph[nx][ny] == '0': # 빈 방
                    wall[nx][ny] = wall[x][y] # 벽을 부수지 않음
                    
                    queue.appendleft((nx, ny))
                    
                elif graph[nx][ny] == '1': # 벽
                    wall[nx][ny] = wall[x][y] + 1 # 벽을 부셨음
                    
                    queue.append((nx, ny))


m, n = map(int, input().split())

graph = []
wall = [[-1] * m for _ in range(n)] # 특정 칸에 이동하기 위해서 부셔야하는 벽의 수를 저장

# 방향 정보(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    input_data = list(sys.stdin.readline().rstrip())
    graph.append(input_data)

# BFS 수행 
bfs() 

# 출력
print(wall[n - 1][m - 1])