"""
- 내구도 0이하면 파괴
- [type, r1, c1, r2, c2, degree]
- 파괴되지 않은 건물 개수 리턴

- 2차원 리스트 누적합
"""
from pprint import pprint

def solution(board, skill):
    
    n, m = len(board), len(board[0])
    # 누적합 기록
    sub_sum = [[0]*(m+1) for _ in range(n+1)]
    for t, r1, c1, r2, c2, degree in skill:
        sub_sum[r1][c1] += degree if t == 2 else -degree
        sub_sum[r1][c2+1] += -degree if t == 2 else degree
        sub_sum[r2+1][c1] += -degree if t == 2 else degree
        sub_sum[r2+1][c2+1] += degree if t == 2 else -degree
    
    
    # 행 기준 누적합
    for i in range(n):
        for j in range(m):
            sub_sum[i][j+1] += sub_sum[i][j]
    
    # 열 기준 누적합
    for j in range(m):
        for i in range(n):
            sub_sum[i+1][j] += sub_sum[i][j]
    

    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + sub_sum[i][j] > 0 :
                answer += 1

    return answer

"""
def solution(board, skill):
    
    n, m = len(board), len(board[0])

    for t, r1, c1, r2, c2, degree in skill:
        if t == 1: degree = (-degree)
        
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                board[i][j] += degree
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0 :
                answer += 1

    return answer
"""
