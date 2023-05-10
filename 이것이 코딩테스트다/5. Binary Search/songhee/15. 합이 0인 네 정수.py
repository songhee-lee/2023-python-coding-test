""" 
- 정수 배열 A B C D
- A[a] + B[b] + C[c] + D[d] = 0 인 (a,b,c,d) 개수 구하기

*** pypy 안하면 시간 초과
"""
from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())
alst, blst, clst, dlst = [], [], [], []
for _ in range(N):
    a,b,c,d = map(int, input().split())
    alst.append(a)
    blst.append(b)
    clst.append(c)
    dlst.append(d)

# a+b+c+d = 0
# a+b = -c-d
ablst = defaultdict(int)
for a in alst:
    for b in blst:
        ablst[ a+b ] += 1

answer = 0
for c in clst:
    for d in dlst:
        x = -1 * (c+d)
        if x in ablst:
            answer += ablst[x]

print(answer)