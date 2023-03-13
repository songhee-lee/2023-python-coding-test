'''
- 빈 칸 : '.', 장애물 : '#', 구멍 : '0', 빨간 구슬 : 'R', 파란 구슬 : 'B'
- 구슬 이동 방향 : (상, 하, 좌, 우)

-> ✅'다시풀기'
'''

from collections import deque
from pprint import pprint

# 보드 기울이기 - 구슬의 위치 (x, y), 기울일 방향 (dx, dy)
def tilt_graph(x, y, dx, dy):
    move_time = 0 # 보드 기울였을 때, 총 이동 횟수
    while True:
        if graph[x][y] == 'O': # 구멍이면
            break
        if graph[x][y] == '#': # 벽이라면
            
            # 뒤로 물러난다.
            x -= dx 
            y -= dy
            break
        
        # 위치 갱신
        x += dx
        y += dy
        
        # 이동 횟수 + 1
        move_time += 1
        
    return (x, y, move_time)

# BFS
def bfs(rx, ry, bx, by):
    queue = deque([(rx, ry, bx, by, 1)])
    visited = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
    
    visited[rx][ry][bx][by] = 1
    
    while queue:
        rx, ry, bx, by, move_time = queue.popleft()
        for i in range(4):
            # 기울이기 - 빨간 구슬
            nrx, nry, red_move_time = tilt_graph(rx, ry, dx[i], dy[i])
            
            # 기울이기 - 파란 구슬
            nbx, nby, blue_move_time = tilt_graph(bx, by, dx[i], dy[i])
            
            # 파란 구슬이 구멍에 빠지면, 실패
            if graph[nbx][nby] == 'O':
                continue
            
            # 빨간 구슬이 구멍에 빠지면, 성공
            if graph[nrx][nry] == 'O':
                return move_time
            
            # 두 구슬의 위치가 같다면,
            # 문제의 조건에 따라, 두 구슬은 동시에 같은 칸에 있을 수 없다.
            if nrx == nbx and nry == nby:
                # 파란 구슬이 빨간 구슬보다 더 뒤에있었음
                if red_move_time < blue_move_time: 
                    nbx, nby = nbx - dx[i], nby - dy[i] # 뒤로 물러난다.
                # 빨간 구슬이 파란 구슬보다 더 뒤에있었음   
                else:
                    nrx, nry = nrx - dx[i], nry - dy[i] # 뒤로 물러난다.
            
            # 방문한적 없으면
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = 1
                queue.append((nrx, nry, nbx, nby, move_time + 1))
                
    return -1 # 어떻게 움직여도 빨간 구슬을 구멍으로 빼낼 수 없다.

n, m = map(int, input().split())

graph = []

# 방향 정보(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 빨간 구슬의 (x, y), 파란 구슬의 (x, y)
rx, ry, bx, by = 0, 0, 0, 0 

for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
            graph[i][j] = '.'
        elif graph[i][j] == 'B':
            bx, by = i, j
            graph[i][j] = '.'

# 빨간 구슬과 파란 구슬의 위치를 인자로 BFS 수행
ret = bfs(rx, ry, bx, by)

print(ret)