# 1. 0과 1로만 이루어져있다
# 2. 1이 적어도 하나 있어야 한다
# 3. 수의 길이가 100 이하
# 4. 0으로 시작하지 않는다
# 자연수 N의 배수 중 위의 조건을 만족하는 수
import re
from collections import deque

T = int(input()) # 테스트 케이스 개수 (T<10)
N = [int(input()) for t in range(T)]
visited=[[1,1] for _ in range(100)]
v_num = 0

"""
def solv(n):
    if not re.findall('[2-9]',n) :
        return
    else:
        num = int(n)
        bfs(num)

def bfs(num):
    global visited
    q = deque([1])
    visited[1] = ['1', v_num]

    while q:
        now = q.pop()

        if len(visited[now][0])==100:
            print('BARK')
            return
        
        for i in [0,1] :
            nxt = (now*10+i)%num
            if nxt != 0:
                if visited[nxt][1] != v_num:
                    visited[nxt] = [visited[now][0]+str(i),v_num]
                    q.appendleft(nxt)
                else:
                    print(visited[now][0]+str(num))
                    return
for n in N:
    v_num += 1
    solv(n)
"""


"""
def dfs (cur, n,i,j): # i : len(cur)-1 , j : '0' 또는 '1'
    # cur이 n의 배수인지 확인
    if int(cur)%n==0 and not visited[i][j] : 
        #print(f'{cur}은 {n}의 배수이다')
        visited[i][j] = True
        like.append(int(cur))
    # 길이가 100 미만 인지 확인
    if len(cur) < 100 :
        dfs(cur+'0',n,len(cur)-1,0)
        dfs(cur+'1',n, len(cur)-1,1)
"""

def bfs (n):
    q = deque(['1'])

    while q:
        cur=q.popleft()
        i, j = len(cur[:-1]), int(cur[-1])
        visited[i][j]=0
        if int(cur)%n==0 :
            like.append(cur)
        if len(cur) < 5 :
            if visited[len(cur)][0] : q.append(cur+'0')
            if visited[len(cur)][1] : q.append(cur+'1')
        

like = []
for n in N:
    cur = '1'

    bfs(n)
print(like)

"""
for n in N:
    print(f'현재 수 : {n}')
    m = []
    i = 0
    num = copy.deepcopy(n)
    while len(str(num)) <= 100:    # 수의 길이가 100 이하인지
        i+=1
        num = i*n
        n_ = str(num)
        # n이 0과 1로만 이루어져있는지 확인
        if not re.findall('[2-9]',n_) : 
            print('0과 1로만 이루어짐')
            # 1의 개수가 1 이상인지
            if n_.count('1') : 
                print(f'1이 1개 이상임, {num}')
                like.append(num)
"""

