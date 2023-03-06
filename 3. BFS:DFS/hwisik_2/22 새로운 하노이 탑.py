'''
- 방문 표시를 set() 자료구조로 만든다.
- 
- 현재 막대들의 상태와 이동횟수를 방문하지 않았다면, 각 막대들의 상태와 이동횟수를 set()에 넣는다.
    - (막대A의 상태, 막대B의 상태, 막대C의 상태, 이동횟수)
- 각 막대에 원판이 있는 경우에만, 다음 상태를 큐에 넣는다.
    - 막대A : A의 마지막 원판 -> B로 이동 or C로 이동
    - 막대B : B의 마지막 원판 -> A로 이동 or C로 이동
    - 막대C : C의 마지막 원판 -> A로 이동 or B로 이동
- 만약, 막대A 에는 원판 A만, 막대B에는 원판B만, 막대C에는 원판C만 있다면 BFS를 종료한다.
'''

from collections import deque

def bfs():
    queue = deque([(init_state[0], init_state[1], init_state[2], 0)])
    
    while queue:
        a, b, c, count = queue.popleft()
        cur_state = a + '/' + b + '/' + c
        
        if a == 'A' * len(a) and b == 'B' * len(b) and c == 'C' * len(c):
            return count

        if cur_state not in visited:
            visited.add(cur_state)

            if len(a) > 0:
                queue.append((a[:-1], b + a[-1], c, count + 1))
                queue.append((a[:-1], b, c + a[-1], count + 1))
            
            if len(b) > 0:
                queue.append((a, b[:-1], c + b[-1], count + 1))
                queue.append((a + b[-1], b[:-1], c, count + 1))
            
            if len(c) > 0:
                queue.append((a, b + c[-1], c[:-1], count + 1))
                queue.append((a + c[-1], b, c[:-1], count + 1))
    

visited = set()
init_state = []

for _ in range(3):
    input_data = input().split()
    if len(input_data) > 1:
        init_state.append(input_data[-1])
    else:
        init_state.append('')
        
ret = bfs()

print(ret)