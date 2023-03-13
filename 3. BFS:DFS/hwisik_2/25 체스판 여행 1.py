'''
-> 주어진 대로 방문하는데 필요한 시간의 최솟값 -> ✅'BFS'

- 1 ~ N^2 까지의 수들의 위치를 모두 찾아 저장한다.
- 처음에는 (1, 1) 위치에 나이트, 비숍, 룩 모두를 큐에 놓는다. => 경우의 수 3가지
- 큐를 순회하면서, 체스말을 바꾸는 경우와 체스를 이동하는 경우를 수행한다.
    - 현재 체스 말이 이전 체스말과 다르다면, 체스말을 바꿔서 큐에 추가.
    - 체스말의 종류에 따라 이동을 수행한다.
        - 만약, 다음 칸에 도착했다면, Step을 늘려서 큐에 추가한다.
        - 다음 칸이 아니라면, Step을 그대로 두고 큐에 추가한다.

-> ✅다시풀기
'''
from collections import deque

# 범위 확인
def is_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n: return False
    return True

# BFS
def bfs():
    ROOK = 0
    BISHOP = 1
    KNIGHT = 2
    
    queue = deque()
    
    # visited = [행][열][칸의 값(1, 2, ..., N^2)][체스 말 종류]
    visited = [[[[0 for _ in range(3)] for _ in range(n ** 2 + 1)] for _ in range(n)] for _ in range(n)]
    
    step_pos = []

    # 1, 2, ..., N^2 가 적힌 칸들의 위치 저장
    for num in range(n ** 2):
        for i in range(n):
            for j in range(n):
                if graph[i][j] == (num + 1):
                    step_pos.append((i, j))
    
    # 처음 방문해야 하는 칸(2가 적힌 칸)의 위치
    x, y = step_pos[0]

    # 룩, 비숍, 나이트 추가
    queue.append((x, y, 0, 2, ROOK))
    queue.append((x, y, 0, 2, BISHOP))
    queue.append((x, y, 0, 2, KNIGHT))
            
    # 룩, 비숍, 나이트 방문 표시
    visited[x][y][2][ROOK] = 1
    visited[x][y][2][BISHOP] = 1
    visited[x][y][2][KNIGHT] = 1

    while queue:
        # 행 / 열 / 이동 횟수 / 현재 도착한 칸에 적힌 수 / 체스 말 종류
        x, y, count, step, chess_type = queue.popleft()

        # N^2가 적힌 칸에 도착
        if step == n ** 2 + 1:
            return count

        # 다음으로 가야하는 수가 적힌 칸의 위치
        nxt_step_x, nxt_step_y = step_pos[step - 1]

        # 말 종류 변경
        for i in range(3):
            if i == chess_type: continue
            if visited[x][y][step][i]: continue
            
            visited[x][y][step][i] = 1
            queue.append((x, y, count + 1, step, i))
        
        # 룩인 경우
        if chess_type == ROOK:
            for i in range(4):
                nx, ny = x, y
                
                # 범위 안에서 가로, 세로로 무한정 이동 가능
                while 0 <= nx < n and 0 <= ny < n:
                    nx += rook_x[i]
                    ny += rook_y[i]
                    
                    if not is_range(nx, ny): break
                    if visited[nx][ny][step][ROOK]: continue
                    
                    visited[nx][ny][step][ROOK] = 1
                    
                    # 다음으로 가야하는 수가 적힌 칸에 도착
                    if nx == nxt_step_x and ny == nxt_step_y:
                        queue.append((nx, ny, count + 1, step + 1, ROOK))
                    # 다음 수가 아닌, 다른 칸에 도착(= 경유하는 느낌)
                    else:
                        queue.append((nx, ny, count + 1, step, ROOK))
        # 비숍인 경우
        elif chess_type == BISHOP:
            for i in range(4):
                nx, ny = x, y
                
                # 범위 안에서 대각선으로 무한정 이동 가능
                while 0 <= nx < n and 0 <= ny < n:
                    nx += bishop_x[i]
                    ny += bishop_y[i]
                    
                    if not is_range(nx, ny): break
                    if visited[nx][ny][step][BISHOP]: continue
                    
                    visited[nx][ny][step][BISHOP] = 1
                    
                    # 다음으로 가야하는 수가 적힌 칸에 도착
                    if nx == nxt_step_x and ny == nxt_step_y:
                        queue.append((nx, ny, count + 1, step + 1, BISHOP))
                    # 다음 수가 아닌, 다른 칸에 도착(= 경유하는 느낌)
                    else:
                        queue.append((nx, ny, count + 1, step, BISHOP))
        # 나이트인 경우
        elif chess_type == KNIGHT:
            for i in range(8):
                nx, ny = x + knight_x[i], y + knight_y[i]
                
                if not is_range(nx, ny): continue
                if visited[nx][ny][step][KNIGHT]: continue
                
                visited[nx][ny][step][KNIGHT] = 1
                
                # 다음으로 가야하는 수가 적힌 칸에 도착
                if nx == nxt_step_x and ny == nxt_step_y:
                    queue.append((nx, ny, count + 1, step + 1, KNIGHT))
                # 다음 수가 아닌, 다른 칸에 도착(= 경유하는 느낌)
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

# BFS 수행
ret = bfs()

# 출력
print(ret)