from collections import deque

def solution(board):
    
    # 로봇 이동
    def move(l, r):
        possible_pos = [] # 로봇의 다음으로 가능한 위치
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        
        # 이동하기
        for i in range(4):
            
            next_left_wing = (l[0] + dx[i], l[1] + dy[i])
            next_right_wing = (r[0] + dx[i], r[1] + dy[i])

            # 다음 위치가 벽이 아닐 경우
            if new_board[next_left_wing[0]][next_left_wing[1]] == 0 and new_board[next_right_wing[0]][next_right_wing[1]] == 0:
                possible_pos.append((next_left_wing, next_right_wing)) # 가능한 위치에 추가
            
        # 회전하기
        # 로봇의 날개가 가로 방향일 경우
        if l[0] == r[0]:
            for d in (-1, 1):
                if new_board[l[0] + d][l[1]] == 0 and new_board[r[0] + d][r[1]] == 0:
                    possible_pos.append((l, (l[0] + d, l[1])))
                    possible_pos.append((r, (r[0] + d, r[1])))
            # 로봇의 날개가 세로 방향일 경우
        else:
            for d in (-1, 1):
                if new_board[l[0]][l[1] + d] == 0 and new_board[r[0]][r[1] + d] == 0:
                    possible_pos.append(((l[0], l[1] + d), l))
                    possible_pos.append(((r[0], r[1] + d), r))
        
        return possible_pos
    
    def bfs():
        q = deque([((1, 1), (1, 2), 0)]) # 왼쪽 날개, 오른쪽 날개, 소요 시간
        visited = set([((1, 1), (1, 2))]) # 방문한 좌표
        
        while q:
            left_wing, right_wing, time = q.popleft()
            if left_wing == (n, n) or right_wing == (n, n): # 어느 한 곳이라도 (n, n)에 도달하면
                return time
            
            # 다음으로 가능한 위치들을 확인
            for nxt in move(left_wing, right_wing):
                if nxt not in visited: # 이미 방문한 위치라면
                    q.append((*nxt, time + 1))
                    visited.add(nxt)
        
    n = len(board)
    
    # 이동 판별을 쉽게하기 위해 외벽을 1로 감싸기
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    cnt = bfs()
    
    return cnt