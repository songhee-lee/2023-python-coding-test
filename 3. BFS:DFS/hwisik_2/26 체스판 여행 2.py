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
from pprint import pprint

# 범위 확인
def is_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n: return False
    return True

# BFS
def bfs():
    min_time = float('inf')
    min_change = float('inf')
    ROOK = 0
    BISHOP = 1
    KNIGHT = 2
    
    queue = deque()
    change_time = [[[[1e9 for _ in range(3)] for _ in range(n ** 2 + 1)] for _ in range(n)] for _ in range(n)]
    
    step_pos = []

    # 1 ~ N^2까지의 수들의 위치 저장
    for num in range(n ** 2):
        for i in range(n):
            for j in range(n):
                if graph[i][j] == (num + 1):
                    step_pos.append((i, j))
    
    # 값이 1인 칸의 위치 
    x, y = step_pos[0]

    # 룩, 비숍, 나이트 배치
    queue.append((x, y, 0, 0, 2, ROOK))
    queue.append((x, y, 0, 0, 2, BISHOP))
    queue.append((x, y, 0, 0, 2, KNIGHT))
    
    # 룩, 비숍, 나이트 방문 표시
    change_time[x][y][2][ROOK] = 0
    change_time[x][y][2][BISHOP] = 0
    change_time[x][y][2][KNIGHT] = 0
    
    while queue:
        x, y, count, change, step, chess_type = queue.popleft()

        # 값이 N^2 칸에 도착했다면
        if step == n ** 2 + 1:
            if count < min_time:
                min_time = count
                min_change = change
            elif count == min_time:
                if change < min_change:
                    min_change = change
            continue

        # 다음으로 방문해야 하는 칸의 위치
        nxt_step_x, nxt_step_y = step_pos[step - 1]

        # 체스말 종류 바꾸기
        for i in range(3):
            if i == chess_type: continue # 이전과 같은 말이면 pass
            if change + 1 >= change_time[x][y][step][i]: continue
            
            change_time[x][y][step][i] = change + 1
            queue.append((x, y, count + 1, change + 1, step, i))
        
        # '룩'인 경우
        if chess_type == ROOK:
            for i in range(4):
                nx, ny = x, y
                while 0 <= nx < n and 0 <= ny < n:
                    nx += rook_x[i]
                    ny += rook_y[i]
                    if not is_range(nx, ny): break
                    if change >= change_time[nx][ny][step][ROOK]: continue
                    
                    change_time[nx][ny][step][ROOK] = change
                    if nx == nxt_step_x and ny == nxt_step_y: # 다음 칸에 도착했다면
                        queue.append((nx, ny, count + 1, change, step + 1, ROOK))
                    else:
                        queue.append((nx, ny, count + 1, change, step, ROOK))
        # '비숍'인 경우
        elif chess_type == BISHOP:
            # 이동 가능한 경우의 수 확인
            for i in range(4):
                nx, ny = x, y
                while 0 <= nx < n and 0 <= ny < n:
                    nx += bishop_x[i]
                    ny += bishop_y[i]
                    
                    if not is_range(nx, ny): break
                    if change >= change_time[nx][ny][step][BISHOP]: continue
                    
                    change_time[nx][ny][step][BISHOP] = change
                    if nx == nxt_step_x and ny == nxt_step_y: # 다음 칸에 도착했다면
                        queue.append((nx, ny, count + 1, change, step + 1, BISHOP))
                    else: 
                        queue.append((nx, ny, count + 1, change, step, BISHOP))
        # '나이트'인 경우
        elif chess_type == KNIGHT:
            # 이동 가능한 경우의 수 확인
            for i in range(8): # 나이트
                nx, ny = x + knight_x[i], y + knight_y[i]
                
                if not is_range(nx, ny): continue
                if change >= change_time[nx][ny][step][KNIGHT]: continue
                
                change_time[nx][ny][step][KNIGHT] = change
                if nx == nxt_step_x and ny == nxt_step_y: # 다음 칸에 도착했다면
                    queue.append((nx, ny, count + 1, change, step + 1, KNIGHT))
                else:
                    queue.append((nx, ny, count + 1, change, step, KNIGHT))
                    
    print(min_time, min_change)
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
bfs()