"""
<< 이동 가능 범위 >>
바로 아래 : (+1,0)
오른쪽 아래 : (+1,+1)

현재 위치 (i,j)의 합 : max((i-1,j)까지의 합, (i-1,j-1)까지의 합) + (i,j)의 값
"""
from sys import stdin
input = stdin.readline
n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int,input().split())))
d=[[0]*n for _ in range(n)]
d[0][0] = tri[0][0]

for i in range(1,n):
    for j in range(i+1):
        if j == 0 :
            d[i][j] = d[i-1][j]+tri[i][j]
        else :
            d[i][j] = max(d[i-1][j],d[i-1][j-1])+tri[i][j]
print(max(d[n-1]))