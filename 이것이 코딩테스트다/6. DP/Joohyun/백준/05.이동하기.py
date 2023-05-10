"""
<< 이동 action >>
현재 위치 : (r,c)
1. (r+1,c) : 아래
2. (r,c+1) : 오른쪽
3. (r+1,c+1) : 아래+오른쪽 >> 오른쪽 대각선 아래

"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[0] * (M + 1)] * (N + 1)
candy = []

for i in range(N):
    candy.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + candy[i-1][j-1]

print(dp[N][M])



# 시간 초과
# from sys import stdin
# from collections import deque
# from copy import deepcopy
# input = stdin.readline

# n,m=map(int,input().split())
# maze = [list(map(int,input().split())) for _ in range(n)]
# move = [(1,0),(0,1),(1,1)]

# queue = deque([(0,0)])
# candy=deepcopy(maze)
# while queue:
#     x,y=queue.popleft()
#     if x==n-1 and y==m-1 : continue
#     for dx,dy in move:
#         nx,ny = x+dx, y+dy
#         if 0<=nx<n and 0<=ny<m :
#             candy[nx][ny]=max(candy[nx][ny], candy[x][y]+maze[nx][ny])
#             queue.append((nx,ny))
# print(candy[n-1][m-1])