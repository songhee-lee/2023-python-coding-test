#입력1 : n 개 컴퓨터, m개의 신뢰 관계 
#입력2(m개의 줄): A B

#출력 : 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호 출력(오름차순)
'''
신뢰관계인 컴퓨터는 동시에 해킹 가능하나는 의미
A가 B를 신뢰하는 경우 B를 해킹하면, A도 해킹할 수 있다.
'''
import sys
from collections import deque

def bfs(cur,n):
    visited = [False] * (n+1)
    que= deque([cur])
    visited[cur] = True
    cnt = 1
    while que:
        cur = que.popleft()
        cnt += 1
        for i in graph[cur]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
    return cnt
    

n,m  = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

#해당 컴퓨터를 해킹했을 때 몇 대를 해킹할 수 있는지 담는 배열
cnt = [0] * n

#단방향
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

possible = []
for i in range(1, n+1):
    possible.append(bfs(i,n))

_max = max(possible)
for i in range(n):
    if _max == possible[i]:
        print(i+1, end=' ')

