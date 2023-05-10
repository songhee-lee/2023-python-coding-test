'''
- 문제의 설명에 충실히 구현
'''
from collections import deque
import sys

n = int(input())
queue = deque()

# 명령어 N개 입력
for _ in range(n):
    order = list(sys.stdin.readline().rstrip().split())
    if order[0] == 'push_front':
        queue.appendleft(order[1])
    elif order[0] == 'push_back':
        queue.append(order[1])
    elif order[0] == 'pop_front':
        if queue:
            out = queue.popleft()
            print(out)
        else:
            print(-1)
    elif order[0] =='pop_back':
        if queue:
            out = queue.pop()
            print(out)
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if queue:
            out = queue[0]
            print(out)
        else:
            print(-1)
    elif order[0] == 'back':
        if queue:
            out = queue[-1]
            print(out)
        else:
            print(-1)