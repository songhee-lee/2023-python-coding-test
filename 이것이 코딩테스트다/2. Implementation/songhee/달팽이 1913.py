"""Psuedo Code

1. 크기 N과 찾고 싶은 수 M 입력 받기
2. 달팽이 모양으로 숫자 입력하기
    - 맨 위, 맨 왼쪽은 N*N -> (N-1)*(N-1) +1 -> (N-1)*(N-1) +2 ...
    - 그 다음 행은 N*N-1 -> (N-1)*(N-1) -> (N-2)*(N-2) + 1 -> +2 + 3 ..
3. 맵과 M의 위치 출력
"""
# 1. 입력 받기
N = int(input())
M = int(input())

# 2. 달팽이 모양으로 입력하기
maps = [ [9, 2, 3], [8, 1, 4], [7, 6, 5]]
for i in range(5, N+1, 2):

    # 추가되는 첫 행 : N*N -> (N-1)*(N-1) +1 -> (N-1)*(N-1) +2 ...
    first = [ i*i, ]
    first += [ x for x in range( (i-2)*(i-2)+1, (i-2)*(i-2)+ i)]

    # 중간 행은 처음과 끝에만 숫자 추가
    for j in range(i-2):
        maps[j].insert(0, i*i - (j+1))  
        maps[j].append(i*i - 3*i + 4 +j)

    # 추가되는 마지막 행 : N*N - N+1 ->  N*N - N -> N*N - N-1, ...
    last = [ x for x in range( i*i - i+1, i*i - 2*i + 1, -1)]

    maps.insert(0, first)
    maps.append(last)


# M 찾기
for i in range(N):
    if M in maps[i]:
        loc = (i+1, maps[i].index(M)+1)
        break

for i in range(N):  
    for j in range(N):
        print(maps[i][j], end = " ")
    print("")

print(loc[0], loc[1])



###################3
### 직접 달팽이 채우기 코드

# 1. 입력 받기
N = int(input())
M = int(input())

# 2. 달팽이 모양으로 입력
maps = [ [ 0 for _ in range(N)] for _ in range(N)]

dx = (-1, 0, 1, 0, -1)  # 상, 우, 하, 좌, 상
dy = (0, 1, 0, -1, 0)

x, y = N//2, N//2   # 시작 위치
maps[x][y] = 1
num = 1             # 채울 숫자

for i in range(3, N+1, 2):
    moves = [1, i-2, i-1, i-1, i-1]

    for m, nx, ny in zip(moves, dx, dy):
        for _ in range(m):
            x, y = x+nx, y+ny
            num += 1
            maps[x][y] = num

            if num == M :
                loc = (x+1, y+1)

for i in range(N):  
    for j in range(N):
        print(maps[i][j], end = " ")
    print("")

print(loc[0], loc[1])



