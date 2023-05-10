'''
[문제]
- n*n의 게임판이 있다. 각 칸에는 정수가 쓰여있다.
- 규칙은 현재 칸에 쓰여있는 수만큼 오른쪽이나 아래로 점프를 한다.
- 게임판의 상태가 주어졌을 때, (0, 0)에서 (n - 1, n - 1)로 갈 수 있는 경우의 수를 구하라.
- 항상 현재 칸에 쓰여있는 수만큼 오른쪽이나 아래로 점프를 할 수 있다.

[점화식]
- dp[i][j] = (i, j)에서 (n - 1, n - 1)로 갈 수 있는 경우의 수

✅ BFS -> 메모리 초과
✅ 다시 풀어보기
'''

from collections import deque
        
n = int(input())
_map = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j] = (i, j)에서 (n - 1, n - 1)로 갈 수 있는 경우의 수
dp = [[0] * n for _ in range(n)]

# 디폴트 값- > (0, 0)에서 시작하므로
dp[0][0] = 1 

# 점화식
# dp[0][0] = 1이고 나머지는 모두 0이므로, 
# 시작점을 제외한 모든 칸의 dp값은 0이므로, (n - 1, n - 1)칸으로 이동했을 때 경우의 수는 0으로 처리된다.
for i in range(n):
    for j in range(n):
        
        # 목표 칸에 도착한 경우
        if i == n - 1 and j == n - 1:
            break
        
        # 아래로 가는 경우, 오른쪽으로 가는 경우
        down, right = i + _map[i][j], j + _map[i][j]
        
        # 범위를 만족한다면
        if down < n:
            dp[down][j] += dp[i][j]
            
        if right < n:
            dp[i][right] += dp[i][j]   

# 출력
print(dp[-1][-1])