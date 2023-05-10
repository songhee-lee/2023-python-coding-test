'''
1. 현재 위치에서 다음 위치(상, 하, 좌, 우)를 확인한다.
2. 만약, 다음 위치에 괴물이 없고 처음 방문하는 노드라면 이동한 거리를 저장한다.
3. 출구에 도달하기 전까지 (1)로 돌아가 반복한다.
4. 출구에 도달했다면 출구까지의 최단 거리를 반환한다.
'''

from collections import deque

# 현재 위치의 범위 확인
def is_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= m: return False
    return True

# BFS
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 상, 하, 좌, 우 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 범위를 벗어난 경우
            if not is_range(nx, ny): continue
            
            # 괴물이 있는 경우
            if board[nx][ny] == 0: continue
            
            # 처음 방문하는 경우 and 괴물이 없는 경우
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1 # 거리 저장
                queue.append((nx, ny)) # 
    
    # 미로의 출구까지의 최단 거리 반환
    return board[n - 1][m - 1]

n, m = map(int, input().split())

board = []

# 이동할 방향 (상, 하, 좌, 우) 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 미로 정보 입력받기
for _ in range(n):
    data = list(input().rstrip())
    board.append(data)

# bfs 수행
ret = bfs(1, 1)

# 출구까지의 최단 거리 출력
print(ret)
