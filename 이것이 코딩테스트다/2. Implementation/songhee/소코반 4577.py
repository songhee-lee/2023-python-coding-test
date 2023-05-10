"""Psuedo Code

1. 입력 받기
    - 행 R, 열 C 
    - 맵
    - 플레이어 입력 순서

2. 플레이어 이동
    - 지시 방향이 빈칸이면 이동
    - 지시 방향에 박스 있으면 박스 밀기 (박스가 이동할 칸도 비어 있어야 함)
    - 지시 방향이 벽이거나 박스 이동 불가시 이동 안함
    - 모든 박스를 목표점으로 이동시키면 게임 끝
3. 목표지점 + 캐릭터 추가하고,
4. 출력하기
"""

def check(targets, maps):
    for tx, ty in targets:
        if maps[tx][ty] != 'b':
            return False
    return True

game = 0   # 게임 순서
dir = {'U':(-1, 0), 'D': (1, 0), 'L':(0, -1), 'R':(0, 1)}   # 방향

while True:
    game += 1
    maps = []       # 전체 맵
    targets = []    # 목표점 위치
    x, y = 0, 0     # 캐릭터 위치
    result = ""     # 게임 결과

    # 1. 입력 받기
        # 1-1. 행 R, 열 C
    R, C = map(int, input().split())
    
    if R == C == 0 :     # 게임 종료 조건
        break

        # 1-2. 맵
            # 맵에 # . b 만 남기기
    maps.append(list(input()))
    for i in range(1, R-1):
        line = list(input())
        for j in range(C):
            c = line[j]
            if c == 'w' or c == 'W':  # 캐릭터
                x, y = i, j
                line[j] = '.'
                if c == 'W':
                    targets.append((i, j))
            elif c == '+':    # 목표점
                targets.append((i, j))
                line[j] = '.'
            elif c == 'B':    # 목표점 위 박스
                targets.append((i, j))
                line[j] = 'b'
        maps.append(line)
    maps.append(list(input()))

        # 1-3. 플레이어 입력 순서
    orders = list(input())

    # 2. 플레이어 이동
    for order in orders:
        dx, dy = dir[order][0], dir[order][1]
        nx, ny = x+dx, y+dy     # 다음 위치
        bx, by = x+2*dx, y+2*dy # 박스의 다음 위치

        next = maps[nx][ny]     # 다음 칸
        # 2-1. 빈칸이면 이동
        if next == '.' :  
            x, y = nx, ny

        # 2-2. 박스가 있는 경우
        elif next == 'b' and maps[bx][by] == '.': # 박스 다음 칸이 빈칸일 때만 이동 가능
            maps[bx][by] = 'b'
            maps[nx][ny] = '.'
            x, y = nx, ny

        # 2-3. 목표지점에 다 넣었는지 확인
        if check(targets,maps):
            result = "complete"
            break

    # 3. 목표지점 넣기 + 다 넣었는지 확인
    if result :
        for tx, ty in targets:
            maps[tx][ty] = 'B'
    else :
        for tx, ty in targets:
            if maps[tx][ty] == 'b':
                maps[tx][ty] = 'B'
            else :
                maps[tx][ty] = '+'
                result = "incomplete"

    # 4. 캐릭터 위치 넣기
    if maps[x][y] == '+':
        maps[x][y] = 'W'
    else :
        maps[x][y] = 'w'
    
    # 출력
    print(f"Game {game}: {result}")
    for i in range(R):
        for j in range(C):
            print(maps[i][j], end="")
        print("")