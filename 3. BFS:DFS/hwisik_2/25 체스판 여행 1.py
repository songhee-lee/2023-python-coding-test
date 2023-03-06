'''
-> 주어진 대로 방문하는데 필요한 시간의 최솟값 -> ✅'BFS'
- 각 칸에 적힌 수 : 1 ~ N^2
- 지학이가 가지고 있는 말의 종류 : 나이트, 비숍, 룩
- 1인 칸의 위치를 찾는다.
- 처음에는 (1, 1) 위치에 나이트, 비숍, 룩 모두를 놓는다. => 경우의 수 3가지
- BFS를 돌면서,
'''
from collections import deque
from pprint import pprint

def is_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n: return False
    return True

def bfs():
    ROOK = 0
    BISHOP = 1
    KNIGHT = 2
    
    queue = deque()
    visited = [[[[0 for _ in range(3)] for _ in range(n ** 2 + 1)] for _ in range(n)] for _ in range(n)]
    
    step_pos = []

    for num in range(n ** 2):
        for i in range(n):
            for j in range(n):
                if graph[i][j] == (num + 1):
                    step_pos.append((i, j))
                
    x, y = step_pos[0]

    queue.append((x, y, 0, 2, ROOK))
    queue.append((x, y, 0, 2, BISHOP))
    queue.append((x, y, 0, 2, KNIGHT))
            
    visited[x][y][2][ROOK] = 1
    visited[x][y][2][BISHOP] = 1
    visited[x][y][2][KNIGHT] = 1
    
    while queue:
        x, y, count, step, chess_type = queue.popleft()

        if step == n ** 2 + 1:
            return count

        nxt_step_x, nxt_step_y = step_pos[step - 1]

        for i in range(3):
            if i == chess_type: continue
            if visited[x][y][step][i]: continue
            
            visited[x][y][step][i] = 1
            queue.append((x, y, count + 1, step, i))
        
        if chess_type == ROOK:
            for i in range(4):
                nx, ny = x, y
                while 0 <= nx < n and 0 <= ny < n:
                    nx += rook_x[i]
                    ny += rook_y[i]
                    if not is_range(nx, ny): break
                    if visited[nx][ny][step][ROOK]: continue
                    
                    visited[nx][ny][step][ROOK] = 1
                    if nx == nxt_step_x and ny == nxt_step_y:
                        queue.append((nx, ny, count + 1, step + 1, ROOK))
                    else:
                        queue.append((nx, ny, count + 1, step, ROOK))
        elif chess_type == BISHOP:
            for i in range(4):
                nx, ny = x, y
                while 0 <= nx < n and 0 <= ny < n:
                    nx += bishop_x[i]
                    ny += bishop_y[i]
                    
                    if not is_range(nx, ny): break
                    if visited[nx][ny][step][BISHOP]: continue
                    
                    visited[nx][ny][step][BISHOP] = 1
                    if nx == nxt_step_x and ny == nxt_step_y:
                        queue.append((nx, ny, count + 1, step + 1, BISHOP))
                    else:
                        queue.append((nx, ny, count + 1, step, BISHOP))
        elif chess_type == KNIGHT:
            for i in range(8): # 나이트
                nx, ny = x + knight_x[i], y + knight_y[i]
                
                if not is_range(nx, ny): continue
                if visited[nx][ny][step][KNIGHT]: continue
                
                visited[nx][ny][step][KNIGHT] = 1
                if nx == nxt_step_x and ny == nxt_step_y:
                    queue.append((nx, ny, count + 1, step + 1, KNIGHT))
                else:
                    queue.append((nx, ny, count + 1, step, KNIGHT))

graph = []

# 룩, 비숍, 나이트의 방향 정보
rook_x, rook_y = [-1, 1, 0, 0], [0, 0, -1, 1]
bishop_x, bishop_y = [-1, 1, 1, -1], [-1, -1, 1, 1]
knight_x, knight_y = [-2, -1, 1, 2, 2, 1, -1, -2], [-1, -2, -2, -1, 1, 2, 2, 1]

n = int(input())

for _ in range(n):
    input_data = list(map(int, input().split()))
    graph.append(input_data)

ret = bfs()

print(ret)