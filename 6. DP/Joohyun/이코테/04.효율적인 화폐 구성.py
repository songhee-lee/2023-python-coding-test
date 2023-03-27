"""
화폐종류 : n 가지
최소한의 화폐 개수로 M원 만들기
"""
"""
금액 i를 만들 수 있는 최소한의 화폐 개수 : a_i
a_{i-k} : i-k원을 만들 수 있는 최소한의 화폐 개수
"""
from sys import stdin
input=stdin.readline
n,m=map(int,input().split())
money=[int(input()) for _ in range(n)]

d=[10001]*(m+1)

d[0]=0
for i in range(n):
    for j in range(money[i],m+1):
        if d[j-money[i]]!=10001:
            d[j]=min(d[j],d[j-money[i]]+1)

if d[m]==10001:print(-1)
else:print(d[m])