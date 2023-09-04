#입력1 : n
#입력2(n^2개의 줄) : 학생의 번호 그 학생이 좋아하는 4명

#출력 : 학생의 만족도의 총 합
'''
교실은 nxn 크기의 격자 / 학생수 n^2
모든 학생에게 번호가 있음 (r,c)는 r행 c열 (1,1) ~ (N,N)
한 칸에는 학생 한 명의 자리
|r1-r2| + |c1-c2| =1 을 만족하는 두칸이 (r1,c1)과 (r2,c2)를 인접함
1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리
2. 1을 만족하는 칸이 여러 개면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로
3. 2를 만족하는 칸도 여러 개면, 행의 번호가 가장 작은 칸으로
4. 3을 만족하는 칸도 여러 개면, 열의 번호가 가장 작은 칸으로

만족도 : 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수 구하기
good
0명 : 0
1명 : 1
2명 : 10
3명 : 100
4명 : 1000
'''
import sys


class struct():
    x = -1
    y = -1
    blank = 0
    cnt = 0


    
n = int(input())

student =[]
for _ in range(n*n):
    student.append(list(map(int, sys.stdin.readline().split())))

board = [[0 for _ in range(n)] for _ in range(n)]

for k in range(n*n):
    order = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                order.append(bfs(student[k][0],i,j)   

        #정렬 규칙에 따라 정렬(매칭수, 빈칸수, 행)
        board[order[0].x][order[0].y] = student[k][0]



def bfs(num, r, c):
    cur = struct()
    cur.x, cur.y = r,c
    cur.blank, cur.cnt = 0,0
    
    dx =[0,0,-1,1]
    dy =[1,-1,0,0]
    
    for i in range(4):
        if r+dx[i] < 1 or r+dx[i] > n or c+dy[i] < 1 or c+dy[i] > n :
            continue

        #blank
        if board[r+dx[i]][c+dy[i]] == 0 :
            cur.blank += 1
            continue

        #좋아하는 사람
        for j in range(1,5):
            if board[r+dx[i]][c+dy[i]] == stduent[k]:
                cur.cnt +=1

    return cur



#BFS




print(student)
