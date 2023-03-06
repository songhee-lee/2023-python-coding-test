from collections import deque

# 입력 : 미로 정보 (크기, 형태)
N, M = map(int,input().split()) # 미로 크기
maze = []                       # 미로 형태
for n in range(N):
    maze.append(list(map(int,input()))) # 미로 형태 update

def DFS(maze, x,y):
    queue = deque([(x,y)])
    while queue:
        i,j = queue.popleft()
        
        # 상하좌우 탐색
        # 미로 밖을 벗어나지 않고, 다음 칸을 방문한 적이 없을 경우 (값이 1인 경우)
        # 다음 칸 : 현재 위치에서 상,하,좌,우로 한 칸씩 각각 이동한 칸
        # 1) 다음 칸 값 update : 이전 이동 횟수를 다음 칸에 더해준다
        # 2) 다음 칸의 index를 queue에 삽입
        if i-1 >= 0 and maze[i-1][j] == 1 : # 상
            maze[i-1][j]+=maze[i][j]
            queue.append((i-1,j))
        if i+1 < N and maze[i+1][j] == 1 :  # 하
            maze[i+1][j]+=maze[i][j]
            queue.append((i+1,j))
        if j-1 >= 0 and maze[i][j-1] == 1 : # 좌
            maze[i][j-1]+=maze[i][j]
            queue.append((i,j-1))
        if j+1 < M and maze[i][j+1] == 1 :  # 우
            maze[i][j+1]+=maze[i][j]
            queue.append((i,j+1))


DFS(maze,0,0)
print(maze[N-1][M-1])