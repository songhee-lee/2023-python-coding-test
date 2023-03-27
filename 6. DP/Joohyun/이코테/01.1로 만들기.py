"""
정수 X 에 사용할 수 있는 연산 4가지
1. X%5==0 -> 5로 나누기
2. X%3==0 -> 3으로 나누기
3. X%2==0 -> 2로 나누기
4. X-1
"""

# DP - BottomUp

x = int(input())

d = [0]*(x+1)

for i in range(2,x+1):
    d[i] = d[i-1]+1                         # x-1
    if not i%2 : d[i] = min(d[i],d[i//2]+1) # x//2
    if not i%3 : d[i] = min(d[i],d[i//3]+1) # x//3
    if not i%5 : d[i] = min(d[i],d[i//5]+1) # x//5

print(d[x])