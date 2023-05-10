"""
덱 구현
1. push_front x : 정수 x를 덱 앞에 넣는다
2. push_back x  : 정수 x를 덱 뒤에 넢는다
3. pop_front    : 덱 가장 앞에 있는 수를 빼고 출력, 없으면 -1 출력
4. pop_back     : 덱 가장 뒤에 있는 수를 빼고 출력, 없으면 -1 출력
5. size         : 정수 개수 출력
6. empty        : 덱 비어있으면 1, 아니면 0 출력
7. front        : 덱 가장 앞에 있는 수 출력, 없으면 -1 출력
8. back         : 덱 가장 뒤에 있는 수 출력, 없으면 -1 출력
"""
from sys import stdin,stdout
from collections import deque

input = stdin.readline
print = stdout.write

q = deque()
for i in range(int(input())):
    cmd=input().rstrip()

    if cmd=='pop_front': print(q.popleft()+'\n') if q else print('-1\n')
    elif cmd=='pop_back':print(q.pop()+'\n') if q else print('-1\n')
    elif cmd=='size':print(str(len(q))+'\n')
    elif cmd=='empty':print('0\n') if q else print('1\n')
    elif cmd=='front':print(q[0]+'\n') if q else print('-1\n')
    elif cmd=='back':print(q[-1]+'\n') if q else print('-1\n')
    else:
        if cmd.split()[0]=="push_front":q.appendleft(cmd.split()[1])
        else:q.append(cmd.split()[1])
