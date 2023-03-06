from collections import deque
import sys
from copy import *

n = int(input())
queue = []
for _ in range(n):
    order = list(sys.stdin.readline().rstrip().split())
    if order[0] == 'push':
        queue.append(order[1])
    elif order[0] == 'pop':
        if queue:
            out = queue.pop(0)
            print(out)
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        out = 0 if queue else 1
        print(out)
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