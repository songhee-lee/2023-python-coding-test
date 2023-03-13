import sys

queue = list()
n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline()

    if "push" in cmd:
        queue.append(int(cmd.split(' ')[1]))

    elif "pop" in cmd:
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))
    elif "size" in cmd:
        print(len(queue))

    elif "empty" in cmd:
        if not queue:
            print(1)
        else:
            print(0)

    elif "front" in cmd:
        if not queue:
            print(-1)
        else:
            print(queue[0])

    elif "back" in cmd:
        if not queue:
            print(-1)
        else:
            print(queue[-1])
