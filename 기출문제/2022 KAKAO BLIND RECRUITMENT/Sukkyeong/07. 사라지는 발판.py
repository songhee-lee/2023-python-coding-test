'''
주어진 보드에서 시작점(0,0)에서 도착점(N-1, N-1)까지 이동할 때 최소 비용을 구하는 문제입니다.
이동은 상하좌우로 이루어지며, 이동하는 방향에 따라서 보드 위에 놓인 발판이 다르게 동작합니다.

보드 위에 놓인 발판은 가로 또는 세로로 놓일 수 있습니다. 따라서 각 발판은 두 칸을 차지합니다.
만약, 현재 위치에서 이동할 위치에 발판이 놓여져 있지 않다면 새로운 발판을 놓을 수 있습니다.

이 문제를 해결하기 위해서는 BFS 탐색을 사용할 수 있습니다.
이 때, 방문한 적이 있는 발판을 또 방문하지 않도록 visited 집합에 저장해둡니다.
그리고 이동할 때, 현재 발판이 가로인지 세로인지에 따라서 다른 조건문을 사용하여 이동합니다.

'''

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321


def solution(board, aloc, bloc):
    return solve(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]


def in_range(board, y, x):
    if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]):
        return False
    return True


def is_finished(board, y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if in_range(board, ny, nx) and board[ny][nx]:
            return False
    return True


def solve(board, y1, x1, y2, x2):
    if is_finished(board, y1, x1):
        return [False, 0]

    # 서로 두 위치가 같을 때 이번 턴에 움직이면 무조건 이기므로
    if y1 == y2 and x1 == x2:
        return [True, 1]

    min_turn = INF
    max_turn = 0
    can_win = False

    # dfs
    for i in range(4):
        ny = y1 + dy[i]
        nx = x1 + dx[i]
        if not in_range(board, ny, nx) or not board[ny][nx]:
            continue

        board[y1][x1] = 0
        result = solve(board, y2, x2, ny, nx)  # 차례가 바뀌기 때문에 위치를 바꿔준다.
        board[y2][x2] = 1

        # 이 시점에서는 result[0]이 False여야만 현재 턴에서 내가 이길 수 있다.
        if not result[0]:
            can_win = True
            min_turn = min(min_turn, result[1])
        elif not can_win:
            max_turn = max(max_turn, result[1])

    turn = min_turn if can_win else max_turn

    return [can_win, turn + 1]