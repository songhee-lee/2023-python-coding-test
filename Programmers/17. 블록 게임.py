''' ref
- 검은 블록을 떨어뜨려 없앨 수 있는 블록 개수의 최댓값 구하기
- 모양에 관계 없이 서로 다른 블록은 서로 다른 숫자로 표현.

[Need to Think]
- 없앨 수 없는 블록은 어떻게 판단할까? -> 현재 블록 위에 다른 블록이 있는가? 현재 블록의 모양이 검은 블록이 내려오는 길을 막는가? 블록의 모양을 보면, 애초부터 없앨 수 없는 블록이 존재한다.
- 없앨 수 있는 블록임을 어떻게 판단할까? 2*3, 3*2
- 어떤 블록을 먼저 없앨지 어떻게 판단할까? 
'''

Board = []

# 현재 블록 위에 다른 블록이 있는지 확인
def canFill(r, c):
    for i in range(r):
        if Board[i][c]:
            return False
    return True

# 현재 블록을 없앨 수 있는지 확인
def find(r, c, h, w):
    max_empty_cnt = 0 # 확인하려는 2*3, 3*2 공간에서의 빈 공간의 최대 개수 => 무조건 2개이다.
    same_num = -1 # 현재 블록의 숫자
    for i in range(r, r + h):
        for j in range(c, c + w):
            if Board[i][j] == 0: # 빈 공간이라면,
                if not canFill(i, j): # 현재 블록 위에 다른 블록이 있다면,
                    return False
                max_empty_cnt += 1
                if max_empty_cnt > 2: # 빈 공간의 최대 개수가 2개를 넘어간다면, 확인하려는 공간을 잘못 찾은 것이다.
                    return False
            else: # 빈 공간이 아니라면,
                if same_num == -1:
                    same_num = Board[i][j] # 현재 블록의 숫자를 저장한다.
                elif same_num != Board[i][j]: # 현재 블록의 숫자와 다른 블록의 숫자가 다르다면
                    return False

    # 현재 블록을 없앨 수 있다. => 0으로 만든다.
    for i in range(r, r + h):
        for j in range(c, c + w):
            Board[i][j] = 0

    return True

def solution(board):
    global Board
    Board = board
    n = len(board)
    answer = 0
    while True:
        break_cnt = 0 # 없앨 수 있는 블록의 개수
        
        # 행과 열을 처음부터 마지막까지 확인한다.
        for i in range(n):
            for j in range(n):
                if i <= n - 2 and j <= n - 3 and find(i, j, 2, 3): # 높이 2, 너비 3인 공간 확인
                    break_cnt += 1
                elif i <= n - 3 and j <= n - 2 and find(i, j, 3, 2): # 높이 3, 너비 2인 공간 확인
                    break_cnt += 1
        # 더 이상 없앨 수 있는 블록이 없다면,
        if break_cnt == 0:
            break # 종료한다.
        answer += break_cnt # 없앨 수 있는 블록의 개수를 갱신

    return answer