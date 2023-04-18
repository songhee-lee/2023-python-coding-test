"""

[게임 끝나는 조건]
1. 이동 공간이 없음          -> 현재 턴 패배
2. 같은 공간에 있고 이동 가능   -> 다음 턴에 승리

"""
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
INF = float('inf')
    
def is_range(board, x, y):
    if 0 <= x < len(board) and 0 <= y < len(board[0]) :
        return True
    return False

def is_finished(board, x, y):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if is_range(board, nx, ny) and board[nx][ny] :
            return False
    return True
        
def solve(board, x1, y1, x2, y2):
    
    # 움직일 수 없으면 패배
    if is_finished(board, x1, y1):
        return [False, 0]
    
    # 같은 위치에 있고 이동 가능하면 다음 턴에 승리
    if x1 == x2 and y1 == y2:
        return [True, 1]
    
    # 이동 가능한 보드로 이동
    max_turn, min_turn = 0, INF
    can_win = False
    
    for i in range(4):
        nx, ny = x1+dx[i], y1+dy[i]
        
        if not is_range(board, nx, ny) or not board[nx][ny]:    # 이동 X
            continue
            
        board[x1][y1] = 0
        result = solve(board, x2, y2, nx, ny)
        board[x1][y1] = 1
        
        # 이길 수 있다면 최솟값 기록
        if not result[0] :
            can_win = True
            min_turn = min(min_turn, result[1])
        elif not can_win :
            max_turn = max(max_turn, result[1])
    
    turn = min_turn if can_win else max_turn
    
    return [can_win , turn + 1]
        
def solution(board, aloc, bloc):
    
    answer = solve(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]
    return answer