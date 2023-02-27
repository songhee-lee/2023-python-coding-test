from itertools import combinations

n = int(input())
board = [list(input().split()) for _ in range(n)]

# 빈 칸 위치 찾기
empty = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 'X':
            empty.append((i, j))

# 장애물을 3개 놓는 모든 경우의 수 생성
obstacle_comb = combinations(empty, 3)

# 학생이 감지될 수 있는지 확인


def is_detected(board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'S':
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    while 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] == 'O':
                            break
                        if board[nx][ny] == 'T':
                            return True
                        nx += dx[k]
                        ny += dy[k]
    return False


# 장애물을 3개 놓는 모든 경우에 대해 감지 여부 확인
detected = False
for comb in obstacle_comb:
    for x, y in comb:
        board[x][y] = 'O'
    if not is_detected(board):
        detected = True
        break
    for x, y in comb:
        board[x][y] = 'X'

print('YES' if detected else 'NO')
