'''

[설명]
- N * N 배열이 있다. 
- 이 배열의 (1, 1) -> (N, N)까지 이동하려고 한다. 
- 이동할 때는 상, 하, 좌, 우로만 가능하다.
- 이동할 때 배열에서 몇 개의 수를 거쳐서 이동하게 된다. 
- 이동하기 위해 거쳐 간 수들 중 최댓값과 최솟값의 차이가 가장 작아지는 경우를 구하라

[아이디어]
- 

-> 이해 안됨...
-> ✅ 다시 풀기
'''

import sys
from collections import deque


def bfs(l, r):
    q = deque([(0, 0)])
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        if x == n - 1 and y == n - 1:
            return True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if l <= _list[nx][ny] <= r and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return False


def binary_search():
    ret = float('inf')

    l, r = l_min, r_min

    while l_min <= l <= l_max and r_min <= r <= r_max:
        l_flag, r_flag = False, False
        if bfs(l, r):
            ret = min(ret, r - l)
            l += 1
            l_flag = True
        else:
            if l_flag and r_flag:
                l += 1
                r += 1
            else:
                r += 1
                r_flag = True

    return ret


n = int(input())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

_list = []

l_min = 200
r_max = 0

for _ in range(n):
    input_data = list(map(int, sys.stdin.readline().split()))
    _list.append(input_data)
    l_min = min(l_min, min(input_data))
    r_max = max(r_max, max(input_data))

l_max = min(_list[0][0], _list[n - 1][n - 1])
r_min = max(_list[0][0], _list[n - 1][n - 1])

ret = binary_search()

print(ret)