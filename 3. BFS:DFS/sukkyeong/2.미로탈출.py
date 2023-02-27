from collections import deque

# 상하좌우이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 미로 크기 입력받기
n, m = map(int, input().split())

# 미로 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# BFS 함수 정의


def bfs(x, y):
    # 큐 생성 및 시작 지점 삽입, 방문 표시
    queue = deque([(x, y)])
    visited = set([(x, y)])
    distance = 1

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 정점 하나 꺼내기
        x, y = queue.popleft()

        # 상하좌우로 이동할 수 있는 칸 검사
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위를 벗어나면 다음 칸 검사
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 괴물이 있는 칸이면 다음 칸 검사
            if graph[nx][ny] == 0:
                continue

            # 방문하지 않은 칸이면 큐에 삽입하고 방문 표시
            if (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))

                # (N, M)에 도달하면 현재까지의 이동 거리를 반환
                if nx == n-1 and ny == m-1:
                    return distance+1

        # 현재 거리에서 다음 이동 거리 추가
        distance += 1

    # 큐를 모두 탐색한 경우 (N, M)까지 도달할 수 없는 경우
    return -1


# 시작 지점 (1, 1)에서 BFS 수행
print(bfs(0, 0))
