""" 
- A 부 배열의 합에 B 부 배열 합을 더해서 T가 되는 모든 쌍의 개수 구하기
"""
from collections import defaultdict

T = int(input())
N = int(input())
numa = list(map(int, input().split()))
M = int(input())
numb = list(map(int, input().split()))

sum_a = defaultdict(int)

# A 부분 배열의 합
all_a = 0
for i in range(N-1, -1, -1):
    x = 0
    for j in range(i, -1, -1):
        x += numa[j]
        sum_a[x] += 1

# A 부분합 = T - B 부분합
answer = 0
for i in range(M):
    for j in range(i, M):
        answer += sum_a[ T - sum(numb[i:j+1])]

print(answer)