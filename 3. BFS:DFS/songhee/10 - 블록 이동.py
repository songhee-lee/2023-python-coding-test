"""
- 2x1 크기의 로봇을 (N, N) 위치로 이동시키기
- 0 빈칸 1 벽
- 로봇은 90도씩 회전 가능
- 앞으로, 아래로만 이동 가능하게 하면 실패 -> 뒤로 이동해야 하는 경우 있음
"""

from collections import deque

def move(tail, head, board):

    tX, tY = tail[0], tail[1]
    hX, hY = head[0], head[1]
    locs = []   # 이동 가능한 위치

    # 앞, 뒤, 위, 아래로 이동
    dx = (0, 0, -1, 1)  
    dy = (-1, 1, 0, 0)
    for i in range(4):
        n_tX, n_tY = tX+dx[i], tY+dy[i]
        n_hX, n_hY = hX+dx[i], hY+dy[i]

        if board[n_tX][n_tY] == 0 and board[n_hX][n_hY] == 0:
            locs.append( ((n_tX, n_tY),(n_hX, n_hY)) )
    
    # 가로 회전
    if tX == hX :
        for d in [-1, 1]:   # 위로 회전, 아래로 회전 방향
            if board[tX+d][tY] == 0 and board[hX+d][hY] == 0:
                locs.append( (tail, (tX+d, tY)) )   # Tail 기준
                locs.append( ((hX+d, hY), head) )   # Head 기준
    # 세로 회전
    else:
        for d in [-1, 1]:   # 좌로 회전, 우로 회전 방향
            if board[tX][tY+d] == 0 and board[hX][hY+d] == 0:
                locs.append( ((tX, tY+d), tail) )     # Tail 기준
                locs.append( ((hX, hY+d), head) )     # Head 기준
    
    return locs
    
    
def solution(board):

    N = len(board)
    q = deque([ ((1,1), (1,2), 0) ])    # 로봇 뒤, 앞, 시간
    check = set([ ((1,1), (1,2)) ])        # 로봇이 갔던 위치 체크

    # board 에 외벽 추가
    tmp = [ [1]*(N+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            tmp[i+1][j+1] = board[i][j]
    board = tmp

    # 로봇 이동하기
    while q:
        tail, head, times = q.popleft()

        # (N, N) 도착하면 종료
        if tail == (N, N) or head == (N, N):
            return times

        # 이동 가능한 위치로 모두 이동해보기
        for next in move(tail, head, board):
            if next not in check:
                q.append( (next[0], next[1], times+1) )
                check.add(next)
