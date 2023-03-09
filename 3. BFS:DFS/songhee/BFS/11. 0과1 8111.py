""" 
- 모듈러 연산으로 수의 범위 줄이는 것이 핵심

A mod B = C 이고, 임의의 수 D 라고 할 때
(A x D) mod B = (C x D) mod B
(A + D) mod B = (C + D) mod B

-> 임의의 수를 더하거나 곱해도 결과가 같으므로,
나머지에 0과 1 덧붙인 후 다시 N으로 나누면 몫에 0과 1을 붙여 나눈 것과 동일하다.
"""
from collections import deque

def check(N):
    q = deque([(1, '1')])   # 숫자와 문자형
    visited = [False] * 20001
    visited[1] = True

    while q:
        num, num_s = q.popleft()

        if num == 0:
            return num_s
        if len(num_s) > 100 :
            return 'BRAK'
        
        # X mod N = (X mod N) mod N
        x = (num * 10) % N
        if not visited[x]:
            visited[x] = True
            q.append((x, num_s+'0'))
        x = (num * 10 +1 ) % N
        if not visited[x]:
            visited[x] = True
            q.append((x, num_s+'1'))
    return 'BRAK'
    
T = int(input())    # 테스트 케이스

for _ in range(T):
    print(check(int(input())))
            