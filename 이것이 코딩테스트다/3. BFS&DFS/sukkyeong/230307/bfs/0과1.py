from sys import stdin
from collections import deque

input = stdin.readline

tc = int(input())
visited = [['', 0] for _ in range(20001)]
visited_num = 0


def solv():
    n = input()
    if n.count('1')+n.count('0') == len(n):
        print(0)
        return
    else:
        n = int(n)
        bfs(n)


def bfs(n):
    global visited
    q = deque([1])
    visited[1] = ['1', visited_num]

    while q:
        now = q.pop()

        if len(visited[now][0]) == 100:
            print('BRAK')
            return

        for num in [0, 1]:
            nxt = (now*10+num) % n
            if nxt != 0:
                if visited[nxt][1] != visited_num:
                    visited[nxt] = [visited[now][0]+str(num), visited_num]
                    q.appendleft(nxt)
            else:
                print(visited[now][0]+str(num))
                return


for _ in range(tc):
    visited_num += 1
    solv()
