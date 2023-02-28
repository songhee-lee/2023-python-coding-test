""" 
https://www.acmicpc.net/problem/18428

1. 입력 받기
    - 선생님 T 학생 S 장애물 O 빈칸 X
2. 장애물 3개 설치
3. 선생님 감시 확인 : 상하좌우 감시 (장애물 투시 불가)
4. 모든 학생이 감시 피할 수 있는지 여부 출력
"""
from itertools import combinations

def check(maps, i, j):
    # 3. 선생님 감시 확인 : 상하좌우 감시 (장애물 투시 불가)
    # 학생 발견하면 True
    
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    
    for k in range(4):
        nx, ny = i+dx[k], j+dy[k]
        
        while 0 <= nx < N and 0 <= ny < N:
            x = maps[dx][dy]
            if  x == 'O':
                break
            elif x == 'S':
                return True
            
            nx, ny = nx+dx[k], nx+dy[k]

def check_all(teachers):
    for x, y in teachers:
        # 한 선생님이라도 학생 발견하면 False 리턴
        if check(maps, x, y):
            return False
    return True

# 1. 입력 받기
N = int(input())    # 맵 크기
maps = []           # 맵 정보
empty_space = []    # 빈 공간 위치 정보
teachers = []       # 선생님 위치 정보
for i in range(N):
    line = input().split()
    maps.append(line)
    
    for j in range(N):  
        if line[j] == 'X' :     # 빈 공간 정보 입력하기
            empty_space.append((i, j))
        elif line[j] == 'T':    # 선생님 정보 입력하기
            teachers.append((i, j))

# 2. 장애물 3개 설치
result = "NO"
for empty in combinations(empty_space, 3):
    # 장애물 설치
    for i, j in empty:
        maps[i][j] = 'O'
    
    # 3. 선생님 감시 확인
    if check_all(teachers):
        result = "YES"
        break
    
    # 장애물 되돌리기
    for i, j in empty:
        maps[i][j] = 'X'

# 4. 모든 학생이 감시 피할 수 있는지 여부 출력
print(result)


