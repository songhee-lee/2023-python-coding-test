# 시간초과

# 그림 = NxN 그리드
# 각 칸에 R,G,B 중 하나를 색칠
# 그림은 여러 구역으로 구성, 구역 내 같은 색
# 같은 구역 : 같은 색상이 상하좌우로 인접해 있는 경우
# 적록색약, 비적록색약이 봤을 때의 구역 수
from collections import deque

N = int(input()) # 그리드 크기 : NxN
grid=[list(input()) for _ in range(N)]  # 그림 정보

D = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y]=False # 시작위치 방문
    while q:
        x,y=q.popleft() # 현위치

        for dx,dy in D:
            nx,ny = x+dx, y+dy  # 상하좌우로 이동
            if nx<0 or nx>=N or ny<0 or ny>=N : continue    # 이동위치가 그리드 밖이면 PASS
            if visited[nx][ny] :    # 이동 위치에 방문한 적 없으면
                # 이동위치색과 현위치색이 같으면 방문표시 후 bfs
                if grid[nx][ny] == grid[x][y] :
                    visited[nx][ny]=False   # 방문
                    q.append((nx,ny))         # bfs

# 구역 세기
def counting(n,cnt):
    for i in range(n):
        for j in range(n):
            # 방문한 적 없는 위치에서 구역 시작
            if visited[i][j] :
                bfs(i,j)
                cnt+=1
    return cnt

# 적록색약이 아닌 경우
visited = [[True]*N for _ in range(N)]  # 방문 정보
cnt_3 = counting(N,0)

# 적록색약인 경우
# R -> G
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'R': grid[i][j]='G'

visited = [[True]*N for _ in range(N)]  # 방문 정보 reset
cnt_2 = counting(N,0)

print(cnt_3, cnt_2)

