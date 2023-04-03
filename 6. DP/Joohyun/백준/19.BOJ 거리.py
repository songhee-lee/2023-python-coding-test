"""
조건
1. idx는 항상 증가
2. B > O > J 순으로 이동
3. 에너지 양 최소
"""

from sys import stdin
input=stdin.readline

n = int(input())
blocks=list(input().rstrip())
dp = [float('inf')]*n
dp[0]=0
BOJ = ['BO', 'OJ','JB']
for i in range(n):
    for j in range(i+1,n):
        # i -> j 로 점프할 경우, block[i]>block[j]가 BOJ 순이면 UPDATE
        if blocks[i]+blocks[j] in BOJ : dp[j]=min(dp[j], dp[i]+pow(j-i,2))

if dp[n-1] != float('inf'):print(dp[n-1])
else:print(-1)