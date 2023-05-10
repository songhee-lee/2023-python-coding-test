import sys
from collections import deque
from itertools import combinations


# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

input = sys.stdin.readline
answer = float("inf")  # 최솟값을 찾기 위해 초깃값을 inf로 설정


def bfs(v):
    queue = deque(v)
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    m = 0  # 최소 횟수를 찾기 위한 변수
    for x, y in queue:
        visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < N and 0 <= ay < N:
                if visited[ax][ay] == -1 and board[ax][ay] != 1:
                    queue.append([ax, ay])
                    visited[ax][ay] = visited[x][y] + 1
                    m = max(m, visited[x][y] + 1)  # 최소 횟수로 갱신

    # bfs가 끝난 이후 바이러스에 감염되지 않은 빈 칸이 있다면 감염시킬수 없는 경우
    # 따라서 inf를 리턴해줌
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 and board[i][j] != 1:
                return float("inf")
    return m


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
virus = []

# 바이러스의 좌표 찾기
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append([i, j])

# 바이러스의 좌표들 중 M개를 뽑은 모든 경우에 대해서 bfs 수행하며 최솟값 갱신
for v in combinations(virus, M):
    answer = min(bfs(v), answer)

# 탐색하지 못하는 경우 answer에는 inf값이 들어있다
if answer == float("inf"):
    print(-1)
else:
    print(answer)
