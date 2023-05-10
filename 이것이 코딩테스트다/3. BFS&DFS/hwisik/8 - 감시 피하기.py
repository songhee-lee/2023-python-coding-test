'''
1. 완전 탐색으로 벽 3개를 세울 수 있는 모든 경우의 수를 탐색한다.
2. 벽 3개를 다 세웠다면, 모든 학생이 선생님의 감시를 피할 수 있는지 확인한다.
3. 단 하나의 경우라도 감시를 피할 수 있다면 'YES'를 출력.
    그렇지 않으면, 'NO'를 출력
'''
from collections import deque
from copy import deepcopy

# 벽 세우기
def set_wall(wall_cnt):
    global is_student_safe
    if wall_cnt == 3: # 벽을 다 세웠다면
        if bfs(): # BFS 수행
            is_student_safe = True
        return
    
    # 완전탐색으로 벽 세우기
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                set_wall(wall_cnt + 1) # 재귀호출
                graph[i][j] = 'X'

# BFS
def bfs():
    for t in teacher: 
        for i in range(4):
            tx, ty = t # 선생님의 위치
            while 0 <= tx < n and 0 <= ty < n: # 상, 하, 좌, 우 확인한다.
                
                # 학생이 보인다면
                if graph[tx][ty] == 'S':
                    return False
                # 벽 뒤는 학생을 볼 수 없다.
                if graph[tx][ty] == 'O':
                    break
                
                tx += dx[i]
                ty += dy[i]
    # 모든 학생이 선생님의 감시를 피할 수 있다면
    return True

n = int(input())

graph = []
teacher = []

# 선생님의 방향 정보(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 모든 학생이 감시를 피할 수 있는지
is_student_safe = False

for _ in range(n):
    data = list(input().split())
    graph.append(data)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append((i, j))

set_wall(0) # 벽 세운다.

ret = 'YES' if is_student_safe else 'NO'
print(ret)