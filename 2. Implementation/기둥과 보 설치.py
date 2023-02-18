'''
실패한 코드
'''

def i_column_check(row, col, n, x, y): # 바닥인지, 아래 기둥있는지, 보 위에 있는지 확인
    if x == n or col[x + 1][y] == 0 or row[x][y - 1] == 1 or row[x][y] == 1:
        return True
    return False
def d_column_check(row, col, x, y): # 위에 기둥이 있는지
    if col[x - 1][y] == 0:
        return False
    if row[x - 1][y + 1] == 1:
        if col[x][y - 1] != 0:
            return False
    if row[x - 1][y] == 1:
        if col[x][y + 1] != 0:
            return False
    return True

def i_row_check(row, col, x, y): # 보의 한쪽 끝 부분이 기둥 위인지, 양쪽 끝 부분이 다른 보와 연결되어 있는지 확인
    if col[x + 1][y] == 0 or col[x + 1][y + 1] == 0:
        return True
    if row[x][y - 1] == 1 and row[x][y + 1] == 1:
        return True
    return False

def d_row_check(row, col, x, y):
    if row[x][y - 1] == 1:
        if col[x + 1][y - 1] != 0 and col[x + 1][y] != 0:
            return False
    if row[x][y + 1] == 1:
        if col[x + 1][y + 1] != 0 and col[x + 1][y + 2] != 0:
            return False
    return True
def solution(n, build_frame):
    col = [[-1] * (n + 1) for _ in range(n + 1)] # 기둥
    row = [[-1] * (n + 1) for _ in range(n + 1)] # 보
    
    for frame in build_frame:
        x, y, a, b = frame
        new_x = n - y - 1
        new_y = x
        if b == 1: # 설치
            if a == 0: # 기둥 이라면
                if i_column_check(row, col, n, new_x, new_y):
                    col[new_x][new_y] = 0
                else:
                    continue
            elif a == 1:
                if i_row_check(row, col, new_x, new_y):
                    row[new_x][new_y] = 1
                else:
                    continue
        elif b == 0: # 삭제
            if a == 0: # 기둥 이라면
                if d_column_check(row, col, new_x, new_y):
                    col[new_x][new_y] = -1
            elif a == 1:
                if d_row_check(row, col, new_x, new_y):
                    row[new_x][new_y] = -1
    print(col)
    answer = [[]]
    return answer