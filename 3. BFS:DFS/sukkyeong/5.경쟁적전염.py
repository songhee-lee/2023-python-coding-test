from collections import deque

n, k = map(int, input().split())
graph = []
virus = []  # 바이러스 정보를 저장할 리스트
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] != 0:
            virus.append((row[j], 0, i, j))  # 바이러스 종류, 시간, 위치 정보를 저장합니다.
    graph.append(row)

s, x, y = map(int, input().split())

virus.sort()  # 바이러스 종류를 기준으로 정렬합니다.
queue = deque(virus)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS 함수 정의


def bfs():
    while queue:
        v, t, x, y = queue.popleft()
        if t == s:
            break  # 시간이 다 되면 종료
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] != 0:
                continue
            graph[nx][ny] = v  # 바이러스 전파
            queue.append((v, t+1, nx, ny))


# BFS 함수 호출
bfs()

# 결과 출력
print(graph[x-1][y-1])
