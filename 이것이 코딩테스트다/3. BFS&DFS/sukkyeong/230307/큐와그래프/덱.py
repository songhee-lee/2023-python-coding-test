import sys
input = sys.stdin.readline
n = int(input())

d = []

for _ in range(n):
    command = input().split()

    if command[0] == 'push_front':
        d.insert(0, command[1])
    if command[0] == 'push_back':
        d.append(command[1])
    elif command[0] == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
    elif command[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif command[0] == 'size':
        print(len(d))
    elif command[0] == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            popN = d.pop(0)
            print(popN)
    elif command[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            popN = d.pop(-1)
            print(popN)
    elif command[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
