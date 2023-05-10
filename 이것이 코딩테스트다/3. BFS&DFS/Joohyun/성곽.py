# 출력 3번 구현 못함

# 굵은 선 : 벽
# 점선 : 통로
# 출력 1. 방 개수
# 출력 2. 가장 넓은 방 크기
# 출력 3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기

# 벽 정보 : 한 정수
# 서 : +1 ->    1
# 북 : +2 ->   10
# 동 : +4 ->  100
# 남 : +8 -> 1000
# 7 x 4
# 11  6 11  6  3 10  6
#  7  9  6 13  5 15  5
#  1 10 12  7 13  7  5
# 13 11 10  8 10 12 13
import sys
from collections import deque


N, M = map(int,input().split()) # 성 크기 : M x N
wall = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]  # 성 정보
visited = [[True]*N for _ in range(M)]  # 방문 여부
D = [(0,1,0),(1,0,1),(2,-1,0),(3,0,-1)] # ( 이동방향(남동북서),x,y )
check = [(2,0),(3,1)] # 동서, 남북

# 1. 벽 정보 -> 2진수로 변환: format(수, 'b')
#          -> 4자리로 맞추기 : .zfill(4)
#          -> 문자화 : str
# 2. 동서 / 남북 값이 0이면 -> 한 공간

def bfs(x,y,f):
    q=deque([(x,y)])    # 현재 위치
    visited[x][y]=False # 방문
    cnt = 1             # 방 크기 초기화
    while q:
        x,y=q.popleft()
        print(f'현재 위치 : {wall[x][y]}')
        now = str(format(wall[x][y],'b').zfill(4))  # 현재위치
        i=0
        for d,dx,dy in D: # 인접칸 탐색(상하좌우)
            print(f'이동 방향 : {dir[d]}')
            nx,ny = x+dx, y+dy
            if 0<=nx<M and 0<=ny<N and visited[nx][ny]: # 성 밖을 벗어나지 않고, 방문한 적 없다면
                nxt = str(format(wall[nx][ny],'b').zfill(4))    # 옆칸 (남동북서))
                print(f'now = {now}, {dir[d]}쪽으로 이동 -> nxt={nxt}')
                
                # 남동북서
                if d%2==0: # 남북
                    if now[d]=='0' and nxt[2-d]=='0':  #동서가 마주보면
                        visited[nx][ny]=False # 방문
                        cnt+=1                # 방 크기 증가
                        q.append((nx,ny))

                else: # 동서
                    if now[d]==nxt[4-d]=='0':  # 동서가 마주보면
                        visited[nx][ny]=False # 방문
                        cnt+=1                # 방 크기 증가
                        q.append((nx,ny))

                    
                    
    return cnt

size=[]
for m in range(M):
    for n in range(N):
        if visited[m][n]:
            f=[]    # 경계 담기
            size.append(bfs(m,n,f))

print(len(size))
print(max(size))

