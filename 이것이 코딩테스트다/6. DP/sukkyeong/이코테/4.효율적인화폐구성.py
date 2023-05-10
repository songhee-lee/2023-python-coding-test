'''
n = 화폐 종류
m = 가치의 합

'''

n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(int, input())

d = [1001]*(m+1)
d[0] = 0

for i in range(n):
    for j in range(arr[i], m+1):
        if d[j-arr[i]] != 10001:
            d[j] = min(d[j], d[j - arr[i]]+1)

# 방법이 없음
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
