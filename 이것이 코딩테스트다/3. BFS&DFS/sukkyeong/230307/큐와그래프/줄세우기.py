from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

student_adj_list = [[] for _ in range(N + 1)]
in_degree = [0 for _ in range(N + 1)]
que = deque()

for i in range(M):
    x, y = map(int, input().rstrip().split())
    student_adj_list[x].append(y)
    in_degree[y] += 1

for i in range(1, N + 1):
    if in_degree[i] == 0:
        que.append(i)

while que:
    node = que.popleft()
    print(node, end=' ')
    for student in student_adj_list[node]:
        in_degree[student] -= 1
        if in_degree[student] == 0:
            que.append(student)
print()
