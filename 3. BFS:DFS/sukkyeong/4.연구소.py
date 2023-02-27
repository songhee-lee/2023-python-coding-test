from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# DFS를 이용해 울타리를 설치하고, 안전 영역 크기를 계산하는 함수


def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        # 복사된 지도에서 바이러스를 확산시킵니다.
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    bfs()
        # 안전 영역의 크기를 계산합니다.
        count = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    count += 1
        result = max(result, count)
        return

    # 울타리를 설치하는 경우
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                # 되돌리기
                graph[i][j] = 0
                count -= 1

# BFS를 이용해 바이러스를 확산시키는 함수


def bfs():
    queue = deque()
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                queue.append((nx, ny))


temp = [[0]*m for _ in range(n)]
dfs(0)
print(result)
