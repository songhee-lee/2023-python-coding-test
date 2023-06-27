from collections import defaultdict, deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#조각 찾는 함수 
#mode =1 : 색칠된 부분 찾기
#mode =0 : 색칠안된 부분 찾기
def search(x, y, table , visited, mode = 1) :
    result = [(0,0)]
    visited[y][x] = True
    table_len = len(table)
    
    #모든 퍼즐 좌표는 (0, 0) 기준으로 저장
    q = deque([(0, 0)])
    while q :
        cur_x, cur_y = q.popleft() 
        for k in range(4) :
            ax, ay = x + cur_x + dx[k], y + cur_y + dy[k]
            if -1 < ax < table_len and -1 < ay < table_len :
                if table[ay][ax] == mode and not visited[ay][ax] :
                    visited[ay][ax] = True
                    q.append((cur_x + dx[k], cur_y + dy[k]))
                    result.append((cur_x + dx[k], cur_y + dy[k]))
    #print(result, mode)
    return result

def rotate(original) :
    result = [original.copy()]
    
    for k in range(3) :
        temp = []
        for x, y in result[-1] :
            #좌표가 (x, y)라고 할 때 90도 회전 시 (-y, x)를 만족
            temp.append((-y, x))
        #print(temp," temp")
        result.append(temp)
        
    return result

    

def possible(g_board, piece, x, y) :
    g_board_len = len(g_board)
    for px, py in piece :
        ax, ay = x + px, y + py
        if ax < 0 or ay < 0 or ax >= g_board_len or ay >= g_board_len or g_board[ay][ax] :
            return False
    return True

def dfs(piece, g_board) :    
    gboard_len = len(g_board)
    piece_len = len(piece)
    
    piece_visited = [False] * piece_len
    visited = [[False]*gboard_len for _ in range(gboard_len)]
    result = 0
    for i in range(gboard_len) :
        for j in range(gboard_len) :
            if visited[i][j] or g_board[i][j] :
                continue
            
            #보드에서 빈칸 구하기
            empty = search(j, i, g_board, visited, 0)
            empty_len = len(empty)
            
            for ex, ey in empty :
                flag = False
                x, y = j + ex, i + ey
                
                #빈칸에 모든 조각 껴보기
                for k in range(piece_len) :
                    #이미 사용한 조각
                    if piece_visited[k] :
                        continue
                        
                    #빈칸과 크기가 맞지 않는 조각
                    if piece[k][0] != empty_len :
                        continue
                    
                    
                    for _piece in piece[k][1:] :
                        if possible(g_board, _piece, x, y) :
                            result += piece[k][0]
                            piece_visited[k] = True
                            flag = True
                            break
                    if flag :
                        break
                if flag :
                    break

    return result

def solution(game_board, table):
    #piece_list = make_piece_list(table)
    table_len = len(table)
    visited = [ [False] * table_len for _ in range(table_len)]
    piece = []
    
    #table에서 조각 잘라내서 list로 만들기
    #회전 시킨 조각 추가
    for i in range(table_len):
        for j in range(table_len):
            if table[i][j] and not visited[i][j]:
                temp = search(j,i, table, visited)
                #print(temp)
                #조각의 크기, 원래 조각, 회전 조각 3개 저장
                piece.append([len(temp)] + rotate(temp))
    
    #게임 보드 각 빈칸에 모든 퍼즐을 한 번씩 끼워서 확인
    answer = dfs(piece, game_board)
    
    return answer