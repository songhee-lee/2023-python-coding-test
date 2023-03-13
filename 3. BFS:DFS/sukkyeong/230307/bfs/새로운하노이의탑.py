import collections

arr = [input()[2:] for _ in range(3)]
# visited = set()
visited = collections.defaultdict(int)
q = collections.deque()

q.append((arr[0], arr[1], arr[2], 0))

while q:
    a, b, c, count = q.popleft()
    cont_str = a + "/" + b + "/" + c

    if 'B' not in a and 'C' not in a:
        if 'A' not in b and 'C' not in b:
            if 'A' not in c and 'B' not in c:
                print(count)
                exit(0)

    # if not cont_str in visited:
        # visited.add(cont_str)
    if not visited[cont_str]:
        visited[cont_str] += 1

        if len(a) > 0:
            q.append((a[:-1], b + a[-1], c, count + 1))
            q.append((a[:-1], b, c + a[-1], count + 1))
        if len(b) > 0:
            q.append((a, b[:-1], c + b[-1], count + 1))
            q.append((a + b[-1], b[:-1], c, count + 1))
        if len(c) > 0:
            q.append((a, b + c[-1], c[:-1], count + 1))
            q.append((a + c[-1], b, c[:-1], count + 1))

print(-1)
