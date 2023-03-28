# 답지 참고
import sys

input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

A.sort()
B.sort()
C.sort(reverse=True)
D.sort(reverse=True)
AB = [a+b for a in A for b in B]
CD = [c+d for c in C for d in D]
AB.sort()
CD.sort(reverse=True)
M = N*N
i = j = res = 0
while i < M and j < M:
    temp = AB[i]+CD[j]
    if temp == 0:
        cnt_ab = cnt_cd = 1
        while i+1 < M and AB[i] == AB[i+1]:
            i += 1
            cnt_ab += 1
        while j+1 < M and CD[j] == CD[j+1]:
            j += 1
            cnt_cd += 1
        res += cnt_ab*cnt_cd
    elif temp > 0:
        j += 1
        continue
    i += 1
print(res)