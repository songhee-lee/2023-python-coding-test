"""
- ShiftRow : i -> i+1 행
    - deque rotate 로 해결 가능
- Rotate : 시계 방향 회전
    - 1행 -> rc[1][0] + rc[0][1:]
    - N행 -> rc[N][1:] + rc[N-1][M]
    - 1열 -> rc[i][0] -> rc[i-1][M]
    - M열 -> rc[i][M] -> rc[i+1][M] 
"""

from collections import deque
                
def solution(rc, operations):
    N, M = len(rc), len(rc[0])
    left_col = deque([rc[i][0] for i in range(N)])
    right_col = deque([rc[i][M-1] for i in range(N)])
    rows = deque([deque(rc[i][1:M-1]) for i in range(N)])
    
    for op in operations:
        if op == "ShiftRow" :
            left_col.appendleft(left_col.pop())
            rows.appendleft(rows.pop())
            right_col.appendleft(right_col.pop())
        else :  # Rotate
            rows[0].appendleft(left_col.popleft())
            right_col.appendleft(rows[0].pop())
            rows[N-1].append(right_col.pop())
            left_col.append(rows[N-1].popleft())
    
    result = []
    for i in range(N):
        result.append( [left_col[i]]+ list(rows[i]) + [right_col[i]])
    return result