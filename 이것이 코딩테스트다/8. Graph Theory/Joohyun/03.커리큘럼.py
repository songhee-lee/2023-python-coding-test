from collections import deque
from copy import deepcopy

n = int(input())    # 들어야하는 강의 수
indegree = [0]*(n+1)    # 진입차수
edges = [[] for _ in range(n+1)] # 선수과목
times = [0]*(n+1)       # 강의 시간

for i in range(1,n+1):
    info = list(map(int,input().split()))    # i:현재과목  info[0]:강의시간  info[:-1]:선수과목  info[-1]:종료
    times[i]=info[0]   # i번째 강의 시간
    info_len=len(info) 
    for j in info[1:-1]:
        indegree[i]+=1      # i번째 과목의 진입차수 1 증가
        edges[j].append(i)  # j->i

q = deque()
# 진입차수가 0인 과목은 q에 삽입
for i in range(1,n+1):
    if not indegree[i]:q.append(i)

result = deepcopy(times)

while q:
    now=q.popleft()
    for next in edges[now]:
        result[i] = max(result[i], result[now]+times[i])
        indegree[next]-=1
        if indegree[next] == 0:
            q.append(next)

for i in range(1,n+1):
    print(result[i])