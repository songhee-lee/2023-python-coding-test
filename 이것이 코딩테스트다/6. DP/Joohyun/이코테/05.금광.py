"""
금광 : n x m

<< 이동 가능 범위 >>
1. 오른쪽 위 : (-1,1)
2. 오른쪽 : (0,1)
3. 오른쪽 아래 : (1,1)

<< FLOW >>
현 위치 : (x,y)
오른쪽 위로 이동하기 전 : (x+1,y-1)
오른쪽으로 이동하기 전 : (x,y-1)
오른쪽 아래로 이동하기 전 : (x-1,y-1)

(x,y)까지 캔 금 =  max((x+1,y-1) , (x,y-1) , (x-1,y-1)) + (x+y)에 있는 금광

"""

t=int(input()) # testcase
for _ in range(t) :
    n,m=map(int,input().split())
    golds = list(map(int,input().split()))
    gold = []
    for i in range(n):
        gold.append(golds[m*i:m*(i+1)])
    d=[[0]*m for _ in range(n)]

    d[0][0],d[1][0],d[2][0] = gold[0][0],gold[1][0],gold[2][0]
    for y in range(1,m):
        for x in range(n):
            if x > 0 and x < n-1:
                d[x][y]=max(d[x+1][y-1],d[x][y-1],d[x-1][y-1])+gold[x][y]
            if x == 0 :
                d[x][y]=max(d[x+1][y-1],d[x][y-1])+gold[x][y]
            if x == n-1 :
                d[x][y]=max(d[x][y-1],d[x-1][y-1])+gold[x][y]
    print(max(list(zip(*d))[m-1]))