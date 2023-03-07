""" 
1. start ~ dest 사이의 모든 소수 구하기
2. start 부터 차례로 한 자릿수만 바꿔서 이동 가능한 숫자 찾기
3. bfs로 최소 경로 구하기
"""
from collections import deque

# 소수 판별 함수 - 에라토스테네스의 체
def check_prime():
    for i in range(2, 100):
        if prime[i] :
            # 소수의 배수 체크하기
            for j in range(i*2, 10000, i):
                prime[j] = False

# 1. 입력 받기
T = int(input())    # 테스트 케이스

# 2. 1000 ~ 9999 까지 소수 전부 체크
prime = [True for _ in range(10000)]
check_prime()

for _ in range(T):
    start, dest = map(int, input().split())
 
    # 3. start 부터 한 자릿수만 바꿔서 이동 가능한 숫자 찾기
    q = deque([start])
    
    visited = [ -1 for _ in range(10000) ]
    visited[start] = 0

    while q:
        now = q.popleft()
        s_now = str(now)

        if now == dest:
            break
        
        # 각 자릿수별로 숫자 바꾸기
        for i in range(4):
            for j in range(10):
                x = int(s_now[:i] + str(j) + s_now[i+1:])
                
                # 방문 안한 1000 이상인 소수인 경우
                if visited[x] == -1 and prime[i] and x > 1000:
                    visited[x] = visited[now]+1
                    q.append(x)

    if visited[dest] == -1:
        print("Impossible")
    else:
        print(visited[dest])