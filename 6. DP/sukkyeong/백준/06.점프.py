'''
i == 0 일 때

dp[0][j] = dp[0][j-1] (if maze[0][j-1] != 0)
dp[0][j] = 0 (if maze[0][j-1] == 0)

i가 0일 때, 위쪽에서 올 수 있는 경로가 없기 때문에 왼쪽에서만 올 수 있습니다. 따라서, 왼쪽에서 오는 경로의 수인 dp[0][j-1]이 현재 dp[0][j]에 더해집니다. 단, 이 때 왼쪽 칸이 0이면 dp[0][j]는 0이 됩니다.

j == 0 일 때

dp[i][0] = dp[i-1][0] (if maze[i-1][0] != 0)
dp[i][0] = 0 (if maze[i-1][0] == 0)

j가 0일 때, 왼쪽에서 올 수 있는 경로가 없기 때문에 위쪽에서만 올 수 있습니다. 따라서, 위쪽에서 오는 경로의 수인 dp[i-1][0]이 현재 dp[i][0]에 더해집니다. 단, 이 때 위쪽 칸이 0이면 dp[i][0]는 0이 됩니다.

i > 0 and j > 0 일 때

dp[i][j] = dp[i-1][j] (if maze[i-1][j] != 0)
dp[i][j] += dp[i][j-1] (if maze[i][j-1] != 0)

i > 0이고, j > 0일 때, 위쪽과 왼쪽에서 오는 두 가지 경로가 있습니다. 각 경로의 수를 더한 값이 dp[i][j]가 됩니다. 단, 위쪽 칸이 0이면 위쪽에서 오는 경로는 없으므로 더하지 않습니다. 왼쪽 칸이 0이면 왼쪽에서 오는 경로는 없으므로 더하지 않습니다
'''

import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1  # 초기 값

# 반복문을 통해 갈 수 있는 그래프의 좌표를 탐색
for i in range(n):
    for j in range(n):

        # 현재 탐색하는 좌표가 오른쪽 맨 끝 점이면 반복을 멈춘다.
        if i == n - 1 and j == n - 1:
            print(dp[i][j])
            break

        # 오른쪽으로 이동
        if j + graph[i][j] < n:
            dp[i][j + graph[i][j]] += dp[i][j]

        # 아래로 이동
        if i + graph[i][j] < n:
            dp[i + graph[i][j]][j] += dp[i][j]
