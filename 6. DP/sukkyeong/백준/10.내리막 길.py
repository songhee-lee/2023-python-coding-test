'''

DP 를 사용하기 위해서는 dp[i][j] 를 (i,j) 에서 (n,m) 까지 갈 수 있는 경로의 개수라고 정의해야 합니다.
그리고 dp[i][j] 는 (i,j) 에서 왼쪽(i,j-1)과 위쪽(i-1,j)의 경로 개수를 더한 값이 됩니다. 이 때, (i,j) 에서 이동이 가능한 경우에만 더해줍니다.
이동 가능한 경우는, 현재 위치의 값이 이전 위치의 값보다 작아야 합니다.

따라서, DFS 함수에서는 다음과 같이 구현됩니다.
(n-1, m-1) 에 도달한 경우 1을 반환합니다.
이미 계산한 경우, 저장된 값을 바로 반환합니다.
dp 값을 0으로 초기화하고, 상하좌우 탐색을 합니다.
각 위치에서 이동 가능한 경우 dp 값을 갱신합니다.
dp 값을 반환합니다.
'''

import sys

sys.setrecursionlimit(10**6)  # recursion limit 를 설정해줍니다.

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]  # -1 로 초기화

dx = [-1, 0, 1, 0]  # 상하좌우
dy = [0, 1, 0, -1]


def dfs(x, y):
    if x == n-1 and y == m-1:  # 종료 조건
        return 1

    if dp[x][y] != -1:  # 이미 계산한 값이면 바로 반환
        return dp[x][y]

    dp[x][y] = 0  # 처음에는 0으로 초기화

    for i in range(4):  # 상하좌우 탐색
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:  # 지도를 벗어나지 않는 경우
            if graph[x][y] > graph[nx][ny]:  # 현재 위치의 값이 더 클 경우
                dp[x][y] += dfs(nx, ny)  # dp 값 갱신

    return dp[x][y]


print(dfs(0, 0))  # (0, 0) 에서 시작
