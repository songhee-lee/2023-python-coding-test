"""
풀이 참조
n과 k의 관계
"""
n,k=map(int,input().split())

d=[[1]*(k+1) for _ in range(n+1)] # 행:n, 열:k
for i in range(2,k+1):
    d[1][i]=i
for i in range(1,n+1):
    for j in range(2,k+1):
        d[i][j]=d[i-1][j]+d[i][j-1]

print(d[n][k]%1000000000)

