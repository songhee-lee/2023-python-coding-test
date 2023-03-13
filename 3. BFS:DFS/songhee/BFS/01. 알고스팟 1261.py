""" 
- 1초 / 128MB

- 0 빈방, 1 벽
- bfs 로 탐색하면서 부숴야하는 벽 개수 기록하기
    -> 빈 방을 벽 부수는 것보다 먼저 탐색해야 함
"""

from collections import deque

# 1. 입력 받기
M, N = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

# 2. 미로 이동하기
# 상하좌우 이동
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

visited = [ [-1] * M for _ in range(N)]  # 특정 칸까지 부숴야할 벽의 개수


q = deque([(0,0)])
visited[0][0] = 0

while q:
    x, y = q.popleft()

    if visited[N-1][M-1] != -1 :
        break

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        # 미로 밖
        if nx < 0 or nx >= N or ny < 0 or ny >= M :
            continue

        # 방문하기
        if visited[nx][ny] == -1 :
            if graph[nx][ny] == 0 :     # 방
                visited[nx][ny] = visited[x][y]
                q.appendleft((nx, ny))
            elif graph[nx][ny] == 1 :   # 벽
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

print(visited[N-1][M-1])