import sys
sys.setrecursionlimit(10**7)

T = int(input())


def dfs(V):
    visited[V] = 1  # 방문한 곳 1로 표시
    next = arr[V]
    if visited[next] == 0:  # 아직 방문하지 않은 곳인 경우
        dfs(next)


for i in range(T):
    answer = 0
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (N + 1)

    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)
            answer += 1
    print(answer)
