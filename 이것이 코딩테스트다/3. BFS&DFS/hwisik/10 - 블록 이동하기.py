'''

'''

from collections import deque

# 로봇 이동
def move(l, r, board): 
    ret = []
    
    # 로봇의 방향 정보(상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    
    for i in range(4):
        nl = (l[0] + dx[i], l[1] + dy[i])
        nr = (r[0] + dx[i], r[1] + dy[i])
        
        # 로봇 이동
        if board[nl[0]][nl[1]] == 0 and board[nr[0]][nr[1]] == 0: # 이동하고자 하는 위치에 벽이 없다면
            ret.append((nl, nr))
    
    # 회전(가로 방향)
    if l[0] == r[0]:
        for d in (-1, 1):
            if board[l[0] + d][l[1]] == 0 and board[r[0] + d][r[1]] == 0: # 벽이 없다면
                ret.append((l, (l[0] + d, l[1])))
                ret.append((r, (r[0] + d, r[1])))
    # 회전(세로 방향)
    else:
        for d in (-1, 1):
            if board[l[0]][l[1] + d] == 0 and board[r[0]][r[1] + d] == 0: # 벽이 없다면
                ret.append(((l[0], l[1] + d), l))
                ret.append(((r[0], r[1] + d), r))
    
    return ret
    
def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)] # 지도의 바깥에 벽을 세우기 위한 새로운 지도 생성
    
    # 지도의 바깥에 벽을 새로 세운다.
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    
    queue = deque([((1, 1), (1, 2), 0)])
    check = set([((1, 1), (1, 2))])
    
    while queue:
        l, r, cnt = queue.popleft()
        if l == (n, n) or r == (n, n): # 도착 지점에 도달한다면
            return cnt
        
        for nxt in move(l, r, new_board): # 로봇을 이동시킨다.
            if nxt not in check:
                queue.append((*nxt, cnt + 1))
                check.add(nxt)