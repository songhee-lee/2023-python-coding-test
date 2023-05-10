# 구슬 탈출  : 빨1 빼기 (빨1, 파1 넣고)
# 보드 : 세로 N, 가로 M
#       가장 바깥 행, 열은 모두 막혀있음
#       구멍 1개
# 구슬 크기 = 보드 한칸 (1x1)
# 기울기 방향 : 동서남북
# 구슬 움직임 : 동시에 움직임

# 보드 정보
# . : 빈칸
# # : 장애물, 벽
# O : 구멍
# R,B : 빨 파 구슬 위치
import sys
from collections import deque
import copy

n,m = map(int,input().split()) # 보드 크기 : n x m (3이상 10이하)
board = [list(sys.stdin.readline()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
print(board)
print(visited)
found = 0

# 위치 찾기
def location(str):
    for i in range(n):
        try:
            found = (i,board[i].index(str))
        except :
            continue
    return found
D = [(-1,0), (1,0), (0,-1), (0,1)]  # 상하좌우

zero = location('O')
rx,ry = location('R')
bx,by = location('B')
dir = ['상','하','좌','우']
#def bfs(zero, R, B):
zx,zy=zero
print(f'구멍 위치 : ({zx},{zy})')
q=deque([(rx,ry,bx,by)])
while q:
    rx,ry,bx,by=q.popleft() # R의 현위치
    print(f'현재 빨간 공 위치 : ({rx},{ry}), 현재 파란 공 위치 : ({bx},{by})')
    if not rx==zx and ry==zx : print('아직 도달 못함')
    #else : 
    i = 0
    for dx, dy in D:    # 상하좌우로 이동
        nrx,nry,nbx,nby=copy.deepcopy(rx),copy.deepcopy(ry),copy.deepcopy(bx),copy.deepcopy(by)
        print(f'빨간 공 현 위치 : ({rx},{ry}) => {dir[i]}쪽으로 이동 : ({dx},{dy}) 이동 => 이동 위치 : ({nrx+dx},{nry+dy})')
        i+=1
        success = 0
        if board[nrx+dx][nry+dy] == '#' :         # 빨간구슬이 움직이지 못하면 다른 방향으로 기울인다
                print('R이 벽을 만남')
                continue
        while board[nrx+dx][nry+dy]!='#':
            if board[nrx+dx][nry+dy] == 'O':    # 빨간 구슬이 구멍으로 빠져나갈경우
                success+=1
                break
                #print(visited[rx][ry]+1)        # 이동 횟수출력
                #exit(0)                         # 프로그램 종료
            #while board[nrx+dx][nry+dy]!='#':   
            nrx,nry = nrx+dx,nry+dy         # 벽을 만날 때까지 이동
            print(f'board[nrx][nry]=board[{nrx}][{nry}]={board[nrx][nry]}')
                
                
            
        if board[nrx+dx][nry+dy] == '#' :           # 파란 구슬이 벽을 만나면 그 자리 그대로
                print('B가 벽을 만남')
        else :                                    
            while board[nbx+dx][nby+dy]!='#':       # 파란 구슬이 벽을 안만날때까지 이동
                nbx,nby = nbx+dx,nby+dy
                if board[nbx][nby] == 'O':
                    success-=1
                    break    # 파란구슬이 구멍으로 들어가면 이동 멈춤
        if success : 
            print(visited[rx][ry]+1)        # 이동 횟수출력
            exit(0)                         # 프로그램 종료
                


        print(f'이동할 위치 >> 빨간공 위치 : ({nrx},{nry}), 현재 파란 공 위치 : ({nbx},{nby}) // 구멍 위치 : ({zx},{zy})')
        # if 0<=nrx<n and 0<=nbx<n and 0<=nry<m and 0<=nby<m :    # 1) 벽 안에 위치하고
        #     print('벽안위치')
        if not board[nbx][nby]=='O' :                        # 2) B가 구멍으로 안빠지고
            print('B구멍 안빠짐')
            if not (nrx==nbx and nry==nby) :                  # 3) R, B가 다른 위치에 있고
                print('R,B 다른 위치')
                print(f'visited[nrx][nry]=visited[{nrx}][{nry}]={visited[nrx][nry]}')
                if not visited[nrx][nry]:                       # 4) R이 방문하지 않은 위치일 경우
                    q.append((nrx,nry,nbx,nby))
                    print(f'이동! : q={q}')
                    visited[nrx][nry]=visited[rx][ry]+1
                    print(f'UPDATE!!!!!!! visited[nrx][nry]=visited[{nrx}][{nry}]={visited[nrx][nry]}')
                else : print('이동 실패!')
            else : print('R,B 같은 위치에 있음')
print(-1)
