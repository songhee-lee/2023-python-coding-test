'''
- 빈 칸 : '.', 장애물 : '#', 구멍 : '0', 빨간 구슬 : 'R', 파란 구슬 : 'B'
- 구슬 이동 방향 : (상, 하, 좌, 우)
'''

from collections import deque

def tilt_graph(x, y, dx, dy):
    dist = 0
    while True:
        if graph[x][y] == 'O':
            break
        if graph[x][y] == '#':
            x -= dx
            y -= dy
            break
        
        x += dx
        y += dy
        dist += 1
    return (x, y, dist)

def bfs(rx, ry, bx, by):
    queue = deque([(rx, ry, bx, by, 1)])
    visited = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visited[rx][ry][bx][by] = 1
    
    while queue:
        rx, ry, bx, by, move_cnt = queue.popleft()
        
        for i in range(4):
            nrx, nry, dist_red = tilt_graph(rx, ry, dx[i], dy[i])
            nbx, nby, dist_blue = tilt_graph(bx, by, dx[i], dy[i])
            
            if graph[nbx][nby] == 'O':
                continue
            
            if graph[nrx][nry] == 'O':
                return move_cnt
            
            if nrx == nbx and nry == nby:
                if dist_red < dist_blue:
                    nbx, nby = nbx - dx[i], nby - dy[i]
                else:
                    nrx, nry = nrx - dx[i], nry - dy[i]
            
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = 1
                queue.append((nrx, nry, nbx, nby, move_cnt + 1))
                
    return -1
            
n, m = map(int, input().split())

graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    input_data = list(input())
    graph.append(input_data)
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
            graph[i][j] = '.'
        elif graph[i][j] == 'B':
            bx, by = i, j
            graph[i][j] = '.'

ret = bfs(rx, ry, bx, by)

print(ret)