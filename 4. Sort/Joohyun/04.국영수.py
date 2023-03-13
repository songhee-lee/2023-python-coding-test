from sys import stdin,stdout
input=stdin.readline

n = int(input())
std=[input().split() for i in range(n)] # 이름,국어,영어,수학
std.sort(key=lambda std:(-int(std[1]),int(std[2]),-int(std[3]),std[0]))     


for i in range(n):
    print(std[i][0])