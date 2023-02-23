'''
[매 초마다 뱀의 이동 규칙]
1. 뱀은 몸길이를 늘려서 머리를 다음칸에 위치시킨다.
2. 만약 이동한 칸에 사과가 있다면, 그 칸의 사과를 없애고 꼬리를 움직이지 않는다.(= 몸 길이가 늘어난다.)
3. 만약 이동한 칸에 사과가 없다면, 몸 길이를 줄여서 꼬리가 위치한 칸을 비워준다(= 몸 길이에 변화가 없다.)

** 벽은 보드의 상하좌우 끝에 존재한다.
** 뱀이 벽 or 자기 자신의 몸에 부딪히면 게임이 끝난다.
** 뱀의 초기 위치는 (1, 1) 이고 길이는 "1"이다.(= 즉, 초기에는 머리와 꼬리의 위치가 같다.)
** 뱀은 초기에 오른쪽을 향한다(즉, 이동할 경우 위치는 (x, y) -> (x, y + 1)로 변한다.)


=> 상, 하, 좌, 우에 맞는 이동 위치? 설정이 필요해 보인다.
=> 회전시키는 함수가 필요해 보인다.
=> 뱀의 위치(머리, 꼬리)를 어떻게 저장할지?
=> 뱀의 방향 변환 정보를 어떻게 저장할지?
'''
import sys
from collections import deque

n = int(sys.stdin.readline()) # 보드의 크기
k = int(sys.stdin.readline()) # 사과의 개수

board = [[0] * (n + 1) for _ in range(n + 1)] # 보드 배열   

# 방향 정보 - 오른쪽, 아래, 왼쪽, 위 (초기 방향은 오른쪽 and 90도 회전에 맞춰서 배열의 값 초기화 한다.)
dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]

for _ in range(k):
    x, y = map(int, sys.stdin.readline().split()) # 사과의 행, 열 위치 정보 입력받기
    board[x][y] = 2 # 사과 배치

l = int(sys.stdin.readline()) # 뱀의 방향 변환 횟수

rotate_info = dict() # 뱀의 방향 변환 정보
for _ in range(l):
    x, c = sys.stdin.readline().split() # 방향 정보 입력받기
    rotate_info[int(x)] = c
    
    
snake = deque() # 뱀의 위치 정보
snake.append((1, 1)) # 초기는 머리 = 꼬리임

time = 0 # 흐른 시간
direction = 0 # 현재 방향
head_x, head_y = 1, 1 # 초기 머리의 x, y 위치
board[head_x][head_y] = 1 # 뱀의 정보는 1로 설정

def rotate(c): # 뱀의 방향을 회전시킨다.
    global direction
    if c == 'L': # 왼쪽
        direction = 4 if direction == 0 else direction # 사실 필요 없긴 함
        direction = (direction - 1) % 4
    elif c == 'D': # 오른쪽
        direction = (direction + 1) % 4

while True:
    time += 1
    head_x += dx[direction] # x 위치 업데이트
    head_y += dy[direction] # y 위치 업데이트
    
    if head_x < 1 or head_x > n or head_y < 1 or head_y > n: # 벽에 부딪힐 경우
        break
    
    if board[head_x][head_y] == 2: # 이동한 칸에 사과가 있다면
        board[head_x][head_y] = 1 # 사과를 비워준다.(=뱀의 정보로 업데이트)
        snake.append((head_x, head_y)) # 머리의 위치를 추가한다(= 꼬리는 움직이지 않는다.)
        
        if time in rotate_info: # 회전해야 한다면
            rotate(rotate_info[time])
    elif board[head_x][head_y] == 0: # 이동한 칸에 사과가 없다면
        board[head_x][head_y] = 1 # 뱀의 정보로 업데이트
        snake.append((head_x, head_y)) # 머리의 위치를 추가한다.
        tail_x, tail_y = snake.popleft() # 사과가 없을 때는 꼬리를 줄인다.
        board[tail_x][tail_y] = 0 # 아무것도 없는 칸으로 업데이트
        
        if time in rotate_info: # 회전해야 한다면
            rotate(rotate_info[time])
    else: # 뱀의 머리가 뱀의 몸에 부딪힐 경우
        break
    
print(time) # 게임이 몇 초에 끝나는지 출력한다.