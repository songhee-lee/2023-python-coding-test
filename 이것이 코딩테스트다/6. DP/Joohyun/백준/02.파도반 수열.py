from sys import stdin
input = stdin.readline

p=[0,1,1,1,2,2]
for i in range(6,101):
    p.append(p[-2]+p[-3])
for _ in range(int(input())):
    n=int(input())
    print(p[n])