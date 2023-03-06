"""
[ 제한 사항 ]
- 0.5초 / 256MB

[ 문제 ]
- 정수 저장하는 큐 구현한 다음 명령어 처리하기

"""
import sys

N = int(input())

q = []
for _ in range(N):
    order = sys.stdin.readline().split()
    
    if order[0] == 'push':
        q.append(order[1])
    elif order[0] == 'pop':
        x = q[0] if len(q) else -1
        q = q[1:]
        print(x)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        x = 0 if len(q) else 1
        print(x)
    elif order[0] == 'front':
        x = q[0] if len(q) else -1
        print(x)
    elif order[0] == 'back':
        x = q[-1] if len(q) else -1
        print(x)
        
        
    
