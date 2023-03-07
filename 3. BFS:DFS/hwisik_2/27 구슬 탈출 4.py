'''
- 빈 칸 : '.', 장애물 : '#', 구멍 : '0', 빨간 구슬 : 'R', 파란 구슬 : 'B'
- 구슬 이동 방향 : (상, 하, 좌, 우)

-> ✅'다시풀기'
'''

from collections import deque

# 보드 기울이기
def tilt_graph(x, y, dx, dy):
    dist = 0 # 기울였을 때 이동한 거리
    while True:
        if graph[x][y] == 'O': # 구멍에 빠지면
            break
        if graph[x][y] == '#': # 벽이라면
            # 뒤로 이동 후, 종료
            x -= dx 
            y -= dy
            break
        
        x += dx
        y += dy
        dist += 1
    return (x, y, dist)

# BFS - (rx, ry) : 빨간 구슬 위치, (bx, by) : 파란 구슬 위치
def bfs(rx, ry, bx, by):
    queue = deque([(rx, ry, bx, by, 1)])
    
    visited = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visited[rx][ry][bx][by] = 1
    
    
    while queue:
        rx, ry, bx, by, move_cnt = queue.popleft()
        
        for i in range(4):
            nrx, nry, dist_red = tilt_graph(rx, ry, dx[i], dy[i]) # 빨간 구슬 이동
            nbx, nby, dist_blue = tilt_graph(bx, by, dx[i], dy[i]) # 파란 구슬 이동
            
            # 파란 구슬이 구멍에 들어가면, 게임 실패
            if graph[nbx][nby] == 'O':
                continue
            
            # 빨간 구슬이 구멍에 들어가면, 게임 성공
            if graph[nrx][nry] == 'O':
                return move_cnt # 이동 횟수 반환
            
            # 보드를 기울인 후, 
            # 빨간 구슬과 파란 구슬의 위치가 같다면
            if nrx == nbx and nry == nby:
                
                # 파란 구슬이 더 많이 이동 - 파란 구슬이 빨간 구슬보다 더 뒤에 있었다.
                if dist_red < dist_blue: 
                    nbx, nby = nbx - dx[i], nby - dy[i] # 파란 구슬 뒤로 이동
                    
                # 빨간 구슬이 더 많이 이동 - 빨간 구슬이 파란 구슬보다 더 뒤에 있었다.
                else:
                    nrx, nry = nrx - dx[i], nry - dy[i] # 빨간 구슬 뒤로 이동
            
            # 방문한 적 없으면
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = 1
                queue.append((nrx, nry, nbx, nby, move_cnt + 1))
                
    return -1 # 빨간 구슬을 구멍을 통해 빼낼 수 없다.
            
n, m = map(int, input().split())

graph = []

# 보드 이동 방향(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 빨간 구슬과 파란 구슬의 위치를 구한다.
# 해당 위치의 보드 값은 '.'(빈 칸)으로 초기화
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

# BFS 수행
ret = bfs(rx, ry, bx, by)

# 출력
print(ret)