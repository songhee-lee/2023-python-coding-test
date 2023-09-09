"""
NxM 미로에서 1은 이동 가능하고 0은 이동할 수 없는 칸이다.
(1, 1)에서 출발해서 (N, M)으로 가는 최소의 칸 수 구하기
이동은 서로 인접한 칸으로만 이동할 수 있다.

칸을 셀 때는 시작 위치와 도착 위치도 포함한다.
1 <= N, M <= 100
"""
import sys
sys.setrecursionlimit(10**6)

"""BFS 풀이"""
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

dx = (1, -1, 0, 0)  # 상, 하, 좌, 우
dy = (0, 0, -1, 1)
q = deque([(0, 0)])
while q :
    x, y = q.popleft()
    if x == N-1 and y == M-1 :
        break

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 :
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

print(graph[N-1][M-1])


"""DFS 풀이 => 시간 초과
def dfs(x, y) :
    if x == N-1 and y == M-1 :  # 마지막 위치 도달
        return
    
    # 상, 하, 좌, 우 이동하기
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < M :  
            # 한 번도 이동한적 없는 곳이거나
            # 더 적은 횟수로 이동 가능할 때만 확인
            if graph[nx][ny] == 1 or graph[nx][ny] >= graph[x][y]+1 :
                graph[nx][ny] = graph[x][y]+1
                dfs(nx, ny)

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

dx = (1, -1, 0, 0)  # 상, 하, 좌, 우
dy = (0, 0, -1, 1)

dfs(0, 0)
print(graph[N-1][M-1])

"""