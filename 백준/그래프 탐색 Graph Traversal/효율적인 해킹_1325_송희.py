import sys
from collections import deque
input = sys.stdin.readline

def counting(graph, node) :
    q = deque([node])
    cnt = 0
    visited = [False] * (N+1)
    visited[node] = True

    while q :
        node = q.popleft()
        cnt += 1

        for nxt in graph[node] :
            if not visited[nxt] :
                q.append(nxt)
                visited[nxt] = True
    return cnt

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
# 그래프 입력받기
for _ in range(M) :
    a, b = map(int, input().split())
    graph[b].append(a)

# 해킹 가능한 컴퓨터 수 계산하기
answer = [0] * (N+1)
for i in range(1, N+1) :
    answer[i] = counting(graph, i)

# 가장 많이 해킹 가능한 컴퓨터 번호 출력
maximum = max(answer)
for i in range(1, N+1) :
    if answer[i] == maximum :
        print(i, end=' ')