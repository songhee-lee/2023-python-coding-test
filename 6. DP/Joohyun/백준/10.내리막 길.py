"""
<< 전체 문제 >>
왼쪽 위 지점에서 오른쪽 아래 지점까지 항상 내리막길로만 이동

<< 부분 문제 >>
이전 위치보다 높이가 낮은 곳으로 이동
"""
def dfs(x,y):
    # 도착지점에 도달하면 1(한 가지 경우의 수)를 리턴
    if x == m-1 and y == n-1 : return 1

    # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
    if dp[x][y] != -1:
        return dp[x][y]
    
    # 방문한 적이 없는 위치라면
    cnt = 0
    for dx,dy in move:
        nx,ny = x+dx, y+dy
        if 0<=nx<m and 0<=ny<n and graph[nx][ny]<graph[x][y]:
            cnt+=dfs(nx,ny)
    
    dp[x][y] = cnt
    return dp[x][y]


m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]

dp = [[-1]*n for _ in range(m)]
move = [(-1,0),(1,0),(0,-1),(0,1)]  # 상하좌우
print(dfs(0,0))