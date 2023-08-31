# 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력
# 여러 개일 경우 오름차순으로 출력
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[b].append(a)

def bfs(start):
  q = deque([start])
  visit = [0] * (n + 1)
  visit[start] = 1
  hacked_cnt = 1
  
  while q:
    cur = q.popleft()
    
    for nxt in graph[cur]:
      if not visit[nxt]:
        visit[nxt] = 1
        hacked_cnt += 1
        q.append(nxt)  
        
  return hacked_cnt

max_cnt = 0
answer = []
for node in range(1, n + 1):
  cnt = bfs(node)
  if max_cnt < cnt:
    max_cnt = cnt
    answer.clear()
    answer.append(node)
  elif max_cnt == cnt:
    answer.append(node)

print(*answer)