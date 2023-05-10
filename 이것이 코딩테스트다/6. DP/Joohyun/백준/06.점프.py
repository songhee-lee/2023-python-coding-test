"""
게임판 : nxn
각 칸 : 현재 칸에서 갈 수 있는 거리
이동 방향 : 오른쪽 (0,1), 아래쪽 (1,0)
종착점 : 0
이동할 수 있는 경로의 수
"""
""" 점화식

"""

import sys
# from collections import deque # bfs
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

d = [[0]*n for _ in range (n)]
d[0][0]=1
for x in range(n):
    for y in range(n):
        if x==n-1 and y==n-1 : 
            print(d[x][y])
            exit(0)
        dx,dy = x+board[x][y],y+board[x][y]
        if dx < n : d[dx][y]+=d[x][y]
        if dy < n : d[x][dy]+=d[x][y]


# # bfs 이용 : 메모리 초과
# queue = deque([(0,0)])
# result = 0
# while queue:
#     x,y=queue.popleft() # 현재 위치
#     print(f'현재 위치 : ({x},{y})')

#     # 종착지인지 확인
#     if x == n-1 and y == n-1 : 
#         result += 1  # 가능한 이동 경로 개수 증가
#         print(f'끝에 도달! 지금까지 종착지에 도달한 경우의 수 :{result}')
#         continue

#     # 이동 방향 정하기
#     dx,dy = x+board[x][y],y+board[x][y] # 현재 위치에서 이동할 수 있는 거리
#     print(f'현재 위치에서 이동할 수 있는 만큼 이동 : ({dx},{dy})')
#     if dx < n : queue.append((dx,y))
#     if dy < n : queue.append((x,dy))

# print(result)