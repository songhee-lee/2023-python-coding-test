'''
- 해설 참고: https://tech.kakao.com/2022/07/13/2022-coding-test-summer-internship/
'''
from collections import deque

def solution(rc, operations):
    def shiftRow():
        rows.appendleft(rows.pop())
        out_cols[0].appendleft(out_cols[0].pop())
        out_cols[1].appendleft(out_cols[1].pop())
    
    def Rotate():
        rows[len_r - 1].append(out_cols[1].pop())
        out_cols[0].append(rows[len_r - 1].popleft())
        rows[0].appendleft(out_cols[0].popleft())
        out_cols[1].appendleft(rows[0].pop())
        
    len_r, len_c = len(rc), len(rc[0])
    rows = deque(deque(row[1:-1]) for row in rc)
    out_cols = [deque(rc[r][0] for r in range(len_r)),
                deque(rc[r][len_c - 1] for r in range(len_r))]
    
    for operation in operations:
        if operation == 'ShiftRow': shiftRow()
        else: Rotate()
        
    answer = []
    for r in range(len_r):
        answer.append([])
        answer[r].append(out_cols[0][r])
        answer[r].extend(rows[r])
        answer[r].append(out_cols[1][r])
    
    return answer