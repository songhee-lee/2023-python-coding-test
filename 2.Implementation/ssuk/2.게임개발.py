# 입력값 받아서 지도와 캐릭터의 위치, 방향 초기화
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# 이동 방법 구현 함수


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


def simulate():
    global x, y, direction
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = 1
    turn_time = 0
    while True:
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]
        if board[nx][ny] == 0 and visited_board[nx][ny] == 0:
            visited += 1
            visited_board[nx][ny] = 1
            x, y = nx, ny
            turn_time = 0
            continue
        else:
            turn_time += 1
        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            if board[nx][ny] == 0:
                x, y = nx, ny
            else:
                break
            turn_time = 0
    return visited


# 함수 실행, 결과 확인
visited_board = [[0] * m for _ in range(n)]
visited_board[x][y] = 1
print(simulate())
