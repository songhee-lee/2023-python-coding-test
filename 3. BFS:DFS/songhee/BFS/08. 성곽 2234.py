
""" 

- 서쪽 1, 북쪽 2, 동쪽 4, 남쪽 8 더한 값

- 방의 개수
- 가장 넓은 방의 넓이
- 하나의 벽을 제거해 얻을 수 있는 가장 넓은 방의 크기
"""
from collections import deque

def bfs(x, y, cnt):
    q = deque([(x, y, cnt)])
    rooms_list = set([(x, y)])
    visited[x][y] = cnt

    while q:
        x, y, cnt = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx <0 or nx >= N or ny <0 or ny>=M : continue
            
            # 방문한적 없고, 벽이 없으면 이동
            if visited[nx][ny] == -1 and (wall[i] & ~maps[nx][ny]):
                visited[nx][ny] = cnt
                q.append((nx, ny, cnt))
                rooms_list.add((nx, ny))
    return rooms_list

# 1. 입력 받기
M, N = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))


# 상하좌우 이동
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
wall = (8, 2, 4, 1)     # (x,y) -> (nx, ny) 일 때 nx 기준으로 봄

# 2. 방 구하기
rooms_loc = dict()
visited = [ [-1] * M for _ in range(N) ]
cnt = 1
for i in range(N):
    for j in range(M):
        if visited[i][j] == -1 :
            rooms_loc[cnt] = bfs(i, j, cnt)
            cnt += 1
rooms_cnt = len(rooms_loc)
print(rooms_cnt)   # 방의 개수

# 각 방의 넓이 구하기
rooms_area = [0, ]
for r in rooms_loc.keys():
    rooms_area.append(len(rooms_loc[r]))
print(max(rooms_area))   # 가장 넓은 방의 크기

# 3. 하나의 벽을 제거해 얻을 수 있는 가장 넓은 방의 크기
# 벽 하나 제거
room_max = [[-1] * (rooms_cnt+1) for _ in range(rooms_cnt+1) ]  
for r in rooms_loc.keys():
    for now in rooms_loc[r]:
        x, y = now
        for i in range(4) :
            if maps[x][y] & wall[i]: # 벽이 있고,
                nx, ny = x-dx[i], y-dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    nxt_r = visited[nx][ny]

                    if nxt_r != r : # 다른 방과 연결되면
                        room_max[r][nxt_r] = rooms_area[r] + rooms_area[nxt_r]               
                                  
print( max( [ max(x) for x in room_max ])) # 벽 하나 제거했을 때 가장 넓은 방의 크기