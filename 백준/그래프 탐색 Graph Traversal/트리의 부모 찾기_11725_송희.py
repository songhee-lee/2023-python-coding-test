"""
루트 없는 트리가 주어진다. 
트리의 루트가 1이라고 정했을 때, 각 노드의 부모를 구하기
2 <= N <= 100,000
"""
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
trees = [[] for _ in range(N+1)]
for _ in range(N-1) :
    a, b = map(int, input().split())
    trees[a].append(b)
    trees[b].append(a)


q = deque([1])
parents = [0 for i in range(N+1)]
while q :
    now = q.popleft()
    for i in trees[now] :
        if parents[i] == 0 and i != 1 :
            parents[i] = now
            q.append(i)

for i in range(2, N+1) :
    print(parents[i])
