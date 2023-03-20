'''
n개의 섬
2개의 섬을 잇는 다리, 중량제한
마지막에 두 섬의 번호 입력
bfs(mid)가 true면 mid = start+1
bfs(mid)가 false면 end = mid -1

'''


from collections import deque
import sys
input = sys.stdin.readline


def bfs(weight):  # weight == now
    queue = deque()
    queue.append(one)
    visited = [False] * (n+1)
    visited[one] = True

    while queue:
        x = queue.popleft()  # w == limit

        for i, w in bridges[x]:
            if not visited[i] and w >= weight:
                visited[i] = True
                queue.append(i)

    if visited[two]:
        return True
    else:
        return False


n, m = map(int, input().split())
bridges = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    bridges[a].append([b, c])
    bridges[b].append([a, c])

one, two = map(int, input().split())

start = 1
end = 1000000000

result = 0
while start <= end:
    mid = (start + end) // 2

    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
