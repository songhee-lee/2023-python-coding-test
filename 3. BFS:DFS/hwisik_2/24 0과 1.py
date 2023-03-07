'''
- 일반적인 BFS를 사용하면, 최악의 경우 경우의 수가 2^99까지 가능해서, 스택 오버플로우가 발생한다.
-> ✅모듈러 연산을 사용 => 범위 줄일 수 있음

[모듈러 연산]
- A mod B = C, 임의의 수 D
-> (A * D) mod B = (C * D) mod B
-> (A + D) mod B = (C + D) mod B
    - ex) 100 mod 8 = 4
            -> (100 * 10 + 1) mod 8 = 1 
            -> (4 * 10 + 1) mod 8 = 1
-> ✅'다시풀기'
'''
from collections import deque
import sys

# 실패 - 수가 100자리까지 가능 => 경우의 수 2^99 => 스택 오버플로우 발생...
def bfs(n):
    queue = deque([1])
    
    while queue:
        cur = queue.popleft()
        if len(str(cur)) > 100:
            return 'BARK'
        if cur % n == 0:
            return cur
        queue.append(cur * 10)
        queue.append(cur * 10 + 1)
        
    return 'BARK'

# 모듈러 연산 
def modular_bfs(n):
    queue = deque([(1, '1')])
    visited = [0] * 20001
    visited[1] = 1
    
    while queue:
        cur_num, cur_str = queue.popleft()
        
        if cur_num == 0:
            return cur_str
        
        # 길이가 100 넘어가면
        if len(cur_str) > 100:
            return 'BARK'
        
        # 뒤에 0 또는 1을 붙였을 때
        _append_zero = cur_num * 10
        _append_one = cur_num * 10 + 1
        
        if not visited[_append_zero % n]:
            visited[_append_zero % n] = 1
            queue.append((_append_zero % n, cur_str + '0'))
        if not visited[_append_one % n]:
            visited[_append_one % n] = 1
            queue.append((_append_one % n, cur_str + '1'))
            
    return 'BARK'

t = int(input())

for _ in range(t):
    n = int(input())
    
    output = modular_bfs(n)
    print(output)