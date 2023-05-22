answer = float('inf')

# 행 뒤집기
def flip(ary, row, col):
    for j in range(col) :
        ary[row][j] = 1 - ary[row][j] 

# 각각의 열이 0 또는 1로만 이루어져 있는지 확인하기
def check(ary, row, col):
    cnt = 0
    for j in range(col):
        tmp = set([ ary[i][j] for i in range(row)])	# j 열
        if len(tmp) == 2 :	# 0과 1이 섞여있는 경우
            return -1			# 목표 상태로의 도달 불가능
        elif 1 in tmp:		# 1로만 이루어진 경우 = 뒤집어야 하는 경우
            cnt += 1
    return cnt			

def dfs(ary, depth, cnt, row, col):
    global answer
    
    # 모든 행 확인한 경우
    if depth == row :
        # 열 확인하기
        ret = check(ary, row, col)
        if ret >= 0 :
            answer = min(answer, cnt+ret)	# 최솟값 저장하기
        return
    
    dfs(ary, depth+1, cnt, row, col)    # 행을 뒤집지 않는 선택
    flip(ary, depth, col)   
    dfs(ary, depth+1, cnt+1, row, col)  # 행을 뒤집는 선택
    flip(ary, depth, col)  
            
def solution(beginning, target):
    row, col = len(beginning), len(beginning[0])
    # beginning과 target 차이
    # 뒤집어야 하면 1, 그대로 둬야하면 0
    board = [[1 if beginning[i][j] != target[i][j] else 0 for j in range(col)] for i in range(row)]
    
    dfs(board, 0, 0, row, col)

    if answer == float('inf') :
        return -1
    return answer