"""
식량창고 선택적 약탈
식량창고는 일직선으로 위치
인접한 식량창고가 공격받으면 바로 알아챈다
최소한 한 칸 이상 떨어진 식량창고 약탈
"""

n = int(input())
array = list(map(int,input().split()))

d = [0]*n

d[0] = array[0]
d[1] = max(d[0], array[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])