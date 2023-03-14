'''
두 소수 사이의 변환에 필요한 최소 횟수 찾기 -> ✅'BFS'
    - 각 자리마다, 0 ~ 9까지의 수를 넣어보면서 소수인지 판별한다.
    - 소수라면, 변환 횟수를 저장한다. (단, 자릿수 만족해야하고, 방문한 적 없어야 함)
'''
from collections import deque
import sys

# BFS
def bfs():
    change_count = [-1] * 10000 # 두 소수 사이의 변환에 필요한 횟수(=방문 배열 + 거리 배열)
    queue = deque([a])
    change_count[a] = 0
    
    while queue:
        cur = queue.popleft()
        cur_to_str = str(cur) # 자릿수 비교를 위해, str로 타입 변환
        
        # 변환됐다면
        if cur == b: 
            return change_count[b]
        
        for i in range(4): # 각 자리에 대해
            for j in range(10): # 0 ~ 9의 숫자로 바꾼다.
                nxt = int(cur_to_str[:i] + str(j) + cur_to_str[i + 1:])
                
                if nxt < 1000 or nxt >= 10000: continue
                if not is_prime[nxt]: continue
                if change_count[nxt] != -1: continue
                
                # 소수이고, 1000 ~ 10000사이의 수 이며, 방문한 적이 없는 경우
                if is_prime[nxt] and change_count[nxt] == -1:
                    change_count[nxt] = change_count[cur] + 1 # 변환 횟수 + 1
                    queue.append(nxt)
                    
    return -1

# 에라토스테네스의 체
def make_eratosthenes():
    for i in range(2, 10000):
        if is_prime[i]: # 소수라면,
            for j in range(2 * i, 10000, i): # j는 i의 배수
                is_prime[j] = False # i의 배수는 소수가 안된다.

t = int(input())

is_prime = [False, False] + [True] * 9998 # 소수 판별 배열

# 에라토스테네스의 체 수행
make_eratosthenes() 

# 각 테스트 케이스에 대해서...
for _ in range(t):
    a, b = map(int, input().split())
    
    # BFS
    ret = bfs() 
    
    # 출력
    if ret == -1: 
        print('Impossible')
    else:
        print(ret)