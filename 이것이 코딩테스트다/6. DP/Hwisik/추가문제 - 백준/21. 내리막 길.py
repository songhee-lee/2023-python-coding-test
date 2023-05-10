'''
[문제]
- 지도의 한 칸은 한 지점을 나타내는데 각 칸에는 지점의 높이가 쓰여있다.
- 각 지점 사이의 이동은 상하좌우로 인접한 항상 높이가 더 낮은 지점으로만 가능하다.
- (0, 0)에서 출발해서 (N-1, M-1)에 도착하는데, 항상 내리막길로만 이동하는 경로의 개수를 구하시오.

[점화식]
- 

-> ✅ 다시 풀기
'''
def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1
    
    # 방문한 경우
    if dp[x][y] != -1:
        return dp[x][y]
    
    # 방문하지 않은 경우
    dp[x][y] = 0
        
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and _map[nx][ny] < _map[x][y]:
            dp[x][y] += dfs(nx, ny)
            
    return dp[x][y]

# 세로 : M, 가로 : N
m, n = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]

ret = dfs(0, 0)

print(dp)
print(ret)