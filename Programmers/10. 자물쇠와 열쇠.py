#잠겨있는 자물쇠 N x N (lock) <=20
#열쇠 모양 M x M (key) <=20
# M은 항상 N 이하

#홈 : 0 / 돌기 : 1
#열쇠는 회전과 이동이 가능
#딱 맞으면 자물쇠 열림

#자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 영향 X
# 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야함
# 열수 있으면 true 불가능하면 false

'''
1. M*2 + N 크기의 보드를 만들고 중앙에 자물쇠 배치
2. key rotate + 이동
3. 열쇠 이동 시 중앙의 키가 모두 1이되면 True
'''

import copy

def possible(x,y,rkey,board,key_len,lock_len):
    #push
    _rkey = copy.deepcopy(rkey)
    _board = copy.deepcopy(board)
    
    for i in range(key_len):
        for j in range(key_len):
            _board[x+i][y+j] += _rkey[i][j]
    #print(_board)
    #check
    for k in range(lock_len):
        for l in range(lock_len):
            if _board[key_len+k][key_len+l] != 1:
                return False
    return True

def rotate_key(r_key, M) :    
    temp = [[0] * (M) for _ in range(M)]
    for x in range(M):
        for y in range(M):
            temp[x][y] = r_key[M-y-1][x]
    return temp

def solution(key, lock):
    M = len(key)
    N = len(lock)
    
    board = [[0] * (M*2+N) for _ in range(M*2+N)]
    #자물쇠 배치
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]
    #print(board)
    rkey = key.copy()
    for _ in range(4):
        rkey = rotate_key(rkey, M)
        #print(rkey)
        
        for x in range(1, M*2+N):
            for y in range(1, M*2+N):
                if (possible(x, y, rkey, board, M, N)):
                    return True
        
    return False
