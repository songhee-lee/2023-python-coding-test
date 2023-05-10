# 체스판 크기 NxN
# 체스판 각 칸에 정수 (1 ~ N^2, 한 번씩)
# 체스 말 : 나이트, 비숏, 룩
# 1 > 2 > ... > N^2 까지 도착하는 데 걸리는 시간의 최솟값
# 다음 수로 이동 전에 다른 수가 적힌 칸을 방문할 수도 있다
# 같은 칸을 여러 번 방문 가능
# 1초 동안 가능한 행위
# 1. 말 이동
# 2. 다른 말로 바꾸기
"""
<나이트 이동 로직>
L자 이동
직선으로 두칸 -> 옆으로 한칸

< 비숍 이동 로직 >
거리 제한 없이 대각선으로 움직임

< 룩 이동 로직 > 
거리 제한 없이 상하좌우 직선으로 움직임
"""

"""
< FLOW >
1. 두 정수 간 이동 거리를 구한다
2. 다음 정수로 이동하기 위해 어떤 말을 써야하는지 구한다
3. 최소 이동 횟수를 총 이동횟수에 더해준다
"""

"""
1. 말을 먼저 정한다
    1.1) 현재 말과 사용할 말이 같으면 시간+=0
    1.2) 현재 말과 사용할 말이 다르면 시간+=1
2. 그 말을 다음 칸으로 보낼 때 
"""
from collections import deque

n = int(input())    # 체스판 크기 : nxn
board = [list(map(int,input().split())) for _ in range(n)]  # 체스판 정보


# 체스말 이동 로직
pieces = [0,1,2]    # 체스말, 1:나이트, 2:비숍, 3:룩
D = [[(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(1,-2),(-1,2),(1,2)], [(-1,-1),(-1,1),(1,1),(1,-1)], [(-1,0), (1,0), (0,-1), (0,1)]]
# move[0]==knight , move[1]==bishop , move[2]==rook
# knight = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(1,-2),(-1,2),(1,2)]  # 나이트 : L자 이동, 상하좌우 순
# bishop = [(-1,-1),(-1,1),(1,1),(1,-1)]                              # 비숍 : 대각선, (북서/북동/남동/남서) 순
# rook = [(-1,0), (1,0), (0,-1), (0,1)]                               # 룩 : 상하좌우 직선



# 정수 num의 위치 찾기
def findLocation (num):
    for i in range(board):
        try:
            y=board[i].index(num)
            x=i
        except : continue
    return (x,y)

def bfs(sml, big, cur_piece):  # sml:n번쨰 정수, big:n+1번째 정수, cur_piece:현재 체스말
    # 1. sml과 big 위치 구하기
    sml_loc = findLocation(sml) # sml의 위치
    big_loc = findLocation(big) # big의 위치
    sml2big = (big_loc[0]-sml_loc[0],big_loc[1]-sml_loc[1]) # sml 에서 big 까지 이동하기 위한 이동 거리
    q = deque([sml_loc])  

    change, move = 0,0  # change : 체스말 바꾼 횟수, move : 체스말 이동 횟수  
    # 2. 한 번만 이동하는 경우
    # 1) 나이트
    if (abs(sml2big[0])==2 and abs(sml2big[1])==1) or (abs(sml2big[0])==1 and abs(sml2big[1])==2):
        if cur_piece==0:    # 현재말이 나이트면 말을 바꾸지 않아도 된다
            return 1        # 이동 횟수만 반환
        else : return 2     # 현재 말이 나이트가 아니면, 말을 바꾸고 이동 횟수 횟수 반환
    # 2) 비숍
    elif abs(sml2big[0])==abs(sml2big[1]) :
        used_piece = 1  # 사용할 말 : 비숍
        move = 1
    # 3) 룩
    elif not sml2big[0]*sml2big[1] :
        used_piece = 2  # 사용할 말 : 룩
    
    if 

    # 3. 두번 이상 이동하는 경우
    visited = [[True]*n for _ in range(n)]  # 체스칸 방문 확인, 정수1 -> 정수2 할 떄마다 초기화
    
    while q:
        x,y = q.popleft()   # 현재 위치
        visited[x][y] == False # 현재 위치 방문 기록

        if sml2big[0]==sml2big[1] : # 비숍만 사용
            change, move = change+1, move+1
        if 


for i in range(n**2):
    # 1. 1과 2사이의 거리를 구한다
    # 2. 사용할 체스말을 선택한다
    # 3. 총 이동횟수에 1과 2사이의
    bfs(i+1,i+2)