""" 
- K번 바꿔치기 했을 때 A의 합이 최대가 되도록 하기 
"""

N, K = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

for i in range(K):
    if a[i] >= b[i] : break
    a[i] = b[i]

print(sum(a))