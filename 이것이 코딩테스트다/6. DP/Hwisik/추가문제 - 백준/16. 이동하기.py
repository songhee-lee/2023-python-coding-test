'''
[문제]
- N×M 크기의 배열로 표현되는 미로가 있다. 
- 미로의 가장 왼쪽 윗 방은 (1, 1)이고, 가장 오른쪽 아랫 방은 (N, M)이다.
- 준규는 (1, 1)에 있고, (N, M)으로 이동하려고 한다.
- 준규가 (r, c)에 있을 때, (r + 1, c), (r, c + 1), (r + 1, c + 1)로 이동할 수 있다.
- 미로 밖으로 나갈 수는 없다.
- 준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수의 최댓값을 구하시오.

[점화식]
- dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + _map[i - 1][j - 1]
    -> 자기 자신의 값 + 왼쪽, 위, 왼쪽 위 중 최댓값
    
✅ BFS는 메모리 초과
'''
from collections import deque

    
n, m = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j] = (i, j)까지 이동할 때, 가져올 수 있는 사탕 개수의 최댓값
# 1-index
dp = [[0] * (m + 1) for _ in range(n + 1)]

# 점화식
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 왼쪽, 위, 왼쪽 위 중 최댓값
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + _map[i - 1][j - 1]

# 출력
print(dp[n][m])