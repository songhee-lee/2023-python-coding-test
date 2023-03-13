import sys
from itertools import combinations
from collections import deque

c, r = map(int, sys.stdin.readline().rsplit())
castle = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(r)]

dirs = {}
dirs[0] = [[0, 1], [0, -1], [1, 0], [-1, 0]]
for i in range(1, 5):
    for case in tuple(combinations((1, 2, 4, 8), i)):
        v = []
        if 1 not in case:
            v.append([0, -1])
        if 2 not in case:
            v.append([-1, 0])
        if 4 not in case:
            v.append([0, 1])
        if 8 not in case:
            v.append([1, 0])
        dirs[sum(case)] = v


def bfs(sy, sx, visited):
    q = deque()
    q.append((sy, sx))
    cnt = 1

    while q:
        y, x = q.popleft()
        num = castle[y][x]

        for dy, dx in dirs[num]:
            ny = y + dy
            nx = x + dx

            if -1 < ny < r and -1 < nx < c:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    cnt += 1
                    q.append((ny, nx))

    return cnt


def solve12():
    visited = [[False for _ in range(c)] for _ in range(r)]
    ans1 = 0
    ans2 = 0
    for i in range(r):
        for j in range(c):
            if not visited[i][j]:
                visited[i][j] = True
                ans1 += 1
                total = bfs(i, j, visited)
                if ans2 < total:
                    ans2 = total

    return '\n'.join((str(ans1), str(ans2)))


def solve3():
    ans = 0
    for i in range(r):
        for j in range(c):
            num = castle[i][j]
            for k in (1, 2, 4, 8):
                if num - k < 0:
                    break
                _num = num - k
                castle[i][j] = _num
                visited = [[False for _ in range(c)] for _ in range(r)]
                for y in range(r):
                    for x in range(c):
                        if not visited[y][x]:
                            visited[y][x] = True
                            total = bfs(y, x, visited)
                            if ans < total:
                                ans = total

                castle[i][j] = num

    return ans


print(solve12())
print(solve3())
