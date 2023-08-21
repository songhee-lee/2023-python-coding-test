from pprint import pprint

N, M = map(int, input().split())
beads = []
for _ in range(N) :
    beads.append(list(map(int, input().split())))

# 소용돌이 순서대로 구슬 위치 추가하기
dx = [0, 1, 0, -1, 0]       # 소용돌이 방향 (좌, 하, 우, 상, 좌)
dy = [-1, 0, 1, 0, -1]
x = y = N // 2              # 상어 좌표 
board = []                  # 격자 칸 별 번호 저장                   
for i in range(1, N//2+1) : # N//2 번 반복
    for d in range(5) :     # 소용돌이의 방향 변화
        nx, ny = x+dx[d], y+dy[d]
        # 소용돌이 방향이 변해야될 때까지 (다음 네모의 범위로 가기 전까지) 반복
        while N//2-i <= nx <= N//2+i and N//2-i <= ny <= N//2+i :
            board.append((nx, ny)) # 격자 칸 번호 저장
            x, y = nx, ny
            nx, ny = x+dx[d], y+dy[d]

# 블리자드 M번 반복
boom = [0, 0, 0, 0]         # 폭발한 구슬 개수 
dx = [0, -1, 1, 0, 0]          # 블리자드 방향
dy = [0, 0, 0, -1, 1]
for _ in range(M) :
    # 1. 블라자드로 구슬 파괴
    D, S = map(int, input().split())    # 블리자드 방향, 거리
    x = y = N//2            # 상어 위치
    for i in range(1, S+1) :
        nx, ny = x+dx[D], y+dy[D]
        beads[nx][ny] = 0
        x, y = nx, ny

    # 2. 구슬 폭발
    flag_boom = True
    while flag_boom :
        prev = cnt = 0  # 구슬 번호, 구슬 개수
        flag_boom = False
        removes = []
        for idx, (i, j) in enumerate(board) :
            now = beads[i][j]
            if now == 0 : continue
            elif prev == now :
                cnt += 1
                removes.append(idx)
            else :
                if cnt >= 4:
                    boom[prev] += cnt
                    for r in removes :
                        x, y = board[r]
                        beads[x][y] = 0
                    flag_boom = True
                prev = now
                cnt = 1
                removes = [idx, ]
        if len(removes) >= 4 :
            boom[prev] += cnt
            for r in removes :
                x, y = board[r]
                beads[x][y] = 0
            flag_boom = True


    # 3. 구슬 그룹화
    prev = now = cnt = 0  # 구슬 번호, 구슬 개수
    groups = []
    for (i, j) in board :
        now = beads[i][j]
        if now == 0 : continue
        elif prev == now :
            cnt += 1
        else:
            groups += [cnt, prev]
            prev = now
            cnt = 1
    groups = groups[2:] + [cnt, prev]  # 마지막 구슬 그룹
    
    beads = [[0]*N for _ in range(N)]
    for idx in range(min(len(groups), N**2-1)) :
        i, j = board[idx]
        beads[i][j] = groups[idx]

# 폭발한 구슬 개수 구하기
answer = 0
for i in range(1, 4) :
    answer += i * boom[i]
print(answer)