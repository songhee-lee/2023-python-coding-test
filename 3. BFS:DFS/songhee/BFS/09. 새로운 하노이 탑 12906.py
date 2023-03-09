""" 
- 막대/원판 a b c
- 움직임의 최소 횟수 구하기

"""

from collections import deque

# 입려 받기
sticks = [ [], [], []]
for i in range(3):
    disc = input().split()
    sticks[i] = disc[-1] if len(disc) > 1 else ''

visited = set() # 방문한 막대 표시
q = deque()     # 방문할 막대 표시
q.append((sticks[0], sticks[1], sticks[2], 0))

while q:
    a, b, c, count = q.popleft()    # 막대 a, b, c, 이동 횟수
    now = a + '/' + b + '/' + c

    # 정렬 완료되면 종료
    if a == 'A'*len(a) and b == 'B'*len(b) and c == 'C'*len(c) :
        print(count)
        break

    if now not in visited :
        visited.add(now)

        if len(a) > 0:
            q.append((a[:-1], b+a[-1], c, count+1)) # a -> b
            q.append((a[:-1], b, c+a[-1], count+1)) # a -> c
        
        if len(b) > 0:
            q.append((a+b[-1], b[:-1], c, count+1)) # b -> a
            q.append((a, b[:-1], c+b[-1], count+1)) # b -> c
        
        if len(c) > 0:
            q.append((a+c[-1], b, c[:-1], count+1)) # c -> a
            q.append((a, b+c[-1], c[:-1], count+1)) # c -> b