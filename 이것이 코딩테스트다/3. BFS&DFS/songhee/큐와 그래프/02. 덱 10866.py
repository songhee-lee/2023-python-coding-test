""" 
[ 제한 사항 ]
- 0.5초 / 256MB

[ 문제 ]
- Deque 구현하고 명령 처리하기
"""
import sys

N = int(input())
d = []
for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == 'push_front':
        d = [order[1]] + d
    elif order[0] == 'push_back':
        d.append(order[1])
    elif order[0] == 'pop_front' :
        x = d[0] if len(d) else -1
        print(x)
        d = d[1:]
    elif order[0] == 'pop_back':
        x = d[-1] if len(d) else -1
        print(x)
        d = d[:-1]
    elif order[0] == 'size':
        print(len(d))
    elif order[0] == 'empty':
        x = 0 if len(d) else 1
        print(x)
    elif order[0] == 'front':
        x = d[0] if len(d) else -1
        print(x)
    elif order[0] == 'back':
        x = d[-1] if len(d) else -1
        print(x)