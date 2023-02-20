# 사과의 위치를 별도 리스트에 저장
# 뱀의 방향 전환 정볼르 새 리스트에 저장
# 뱀의 초기 위치를 (1,1)로 설정하고, 방향 변수를 0으로 초기화
# 현재 뱀의 머리의 위치, 방향으로 ny, nx를 계산
# ny, nx가 벽에 부딪히거나 자기몸에 부딪히면 게임 종료
# 칸에 사과가 있으면 사과 제거, 없으면 꼬리 자름


from collections import deque

n = int(input())
k = int(input())
apples = []
for _ in range(k):
    row, col = map(int, input().split())
    apples.append((row, col))

l = int(input())
moves = []
for _ in range(l):
    x, c = input().split()
    moves.append((int(x), c))

# 동, 남, 서, 북
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 초기 뱀의 위치와 방향 설정
snake = deque([(1, 1)])
direction = 0

time = 0
move_idx = 0

while True:
    time += 1

    # 다음 칸 위치
    ny = snake[0][0] + dy[direction]
    nx = snake[0][1] + dx[direction]

    # 벽에 부딪히거나 자기 자신의 몸에 부딪힌 경우
    if ny < 1 or ny > n or nx < 1 or nx > n or (ny, nx) in snake:
        break

    # 다음 칸에 사과가 있는 경우
    if (ny, nx) in apples:
        apples.remove((ny, nx))
    else:
        snake.pop()

    snake.appendleft((ny, nx))

    # 방향 전환
    if move_idx < l and time == moves[move_idx][0]:
        if moves[move_idx][1] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        move_idx += 1

print(time)
