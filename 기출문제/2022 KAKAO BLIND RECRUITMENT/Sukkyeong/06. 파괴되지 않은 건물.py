'''
주어진 게임판과 스킬에 따라서 적절히 보드를 조작하여 보드의 값이 양수인 칸의 개수를 구하는 문제

보드는 2차원 리스트로 주어지며, 각 칸의 값은 해당 칸에 위치한 유닛의 체력을 나타냅니다.

skill = [type, r1, c1, r2, c2, degree]

type은 스킬의 종류를 나타내며, 1인 경우 공격, 2인 경우 회복입니다.
r1, c1, r2, c2는 스킬을 적용할 영역을 나타내는 왼쪽 상단, 오른쪽 하단 좌표입니다.
 degree는 스킬의 강도를 나타내며, 공격인 경우에는 음수, 회복인 경우에는 양수입니다.

각 스킬은 적절한 좌표에 대해 diff 리스트를 증감시킴으로써 보드의 값을 갱신합니다.
이후에는 diff 리스트를 누적합을 통해 전체 보드의 값을 계산하고, 이를 통해 양수인 칸의 개수를 계산합니다.

'''

def solution(board, skill):
    # 보드 크기 설정
    R, C = len(board) + 1, len(board[0]) + 1
    # diff 리스트 초기화
    diff = [[0] * C for _ in range(R)]

    # 각 스킬 적용
    for t, r1, c1, r2, c2, d in skill:
        d *= -1 if t == 1 else 1
        set_diff(diff, r1, c1, r2, c2, d)

    # diff 리스트 누적합 계산
    for i in range(1, R):
        diff[i][0] += diff[i - 1][0]
        diff[0][i] += diff[0][i - 1]

    # 보드의 양수 칸 개수 계산
    ans = 0
    for i in range(1, R):
        for j in range(1, C):
            diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
            ans += 1 if board[i - 1][j - 1] + diff[i - 1][j - 1] > 0 else 0
    return ans

def set_diff(diff, r1, c1, r2, c2, d):
    # diff 리스트 갱신
    diff[r1][c1] += d
    diff[r2 + 1][c2 + 1] += d
    diff[r2 + 1][c1] -= d
    diff[r1][c2 + 1] -= d
