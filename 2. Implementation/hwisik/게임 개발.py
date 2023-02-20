'''
1. 먼저 현재 방향에서 왼쪽 방향으로 회전한다.
    1.1. 왼쪽 방향의 칸을 방문하지 않았다면 해당 방향으로 한 칸 움직인다.
    1.2. 이미 방문한 칸이라면 회전만 하고 움직이지 않는다.
2. 만약 네 방향 모두 확인했는데, 이미 가본 칸이거나 바다라면, 방향을 유지한 채 뒤로 1칸 움직인다.
    2.1. 뒤의 칸이 바다라면 움직임을 멈춘다.
    2.2. 바다가 아니라면 (1)로 돌아간다.
*** field에서 0은 육지, 1은 바다, -1은 이미 방문한 칸을 의미한다. ***
'''

import collections
import sys

n, m = map(int, sys.stdin.readline().split()) # 세로 n, 가로 m을 공백을 기준으로 입력받는다. (n = 행, m = 열)
x, y, d = map(int, sys.stdin.readline().split()) # x, y: 캐릭터 좌표, d : 캐릭터가 바라보고 있는 방향

field = [] # 맵의 정보
dirs = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)} # 0 : 북, 1 : 동, 2 : 남, 3 : 서

for _ in range(n): # 다음 n개의 줄에
    data = list(map(int, sys.stdin.readline().split())) # 맵의 정보를 입력받는다.
    field.append(data) # 입력받은 맵의 정보를 리스트에 저장한다.

def turn_left(): # 왼쪽으로 회전
    global d
    d -= 1
    if d == -1:
        d = 3

ret = 0 # 캐릭터가 방문한 칸의 수
turn_count = 0 # 왼쪽 방향으로 회전한 횟수
while True:
    turn_left() # 왼쪽 방향으로 먼저 회전한다.
    nx, ny = x + dirs[d][0], y + dirs[d][1] # 다음 위치
    if field[nx][ny] == 0: # 만약, 다음 위치의 칸이 육지라면
        field[nx][ny] = -1 # 방문처리를 한다.(-1로)
        x, y = nx, ny # 현재 위치를 업데이트 한다.
        ret += 1 
        turn_count = 0 # 회전 횟수를 0으로 초기화.
        continue
    else: # 다음 위치의 칸이 바다이거나 이미 방문한 칸이라면
        turn_count += 1 
    if turn_count == 4: # 네 방향 모두 회전한 경우 => 네 방향 모두 갈 수 없는 칸일 때 
        nx, ny = x - dirs[d][0], y - dirs[d][1] # 바라보는 방향 유지한 채로 뒤로 1칸 간다.
        if field[nx][ny] == -1 or field[nx][ny] == 0: # 만약, 뒤의 칸이 방문한 칸이라면
            x, y = nx, ny # 위치 업데이트
        else: # 만약, 뒤의 칸이 바다라면 
            break
        turn_count = 0
        
print(ret) # 결과 출력