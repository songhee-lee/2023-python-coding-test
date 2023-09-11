# a, b => a가 b의 선수과목 ( a < b ) => 선수과목의 번호는 항상 더 작다.
# 1번 과목부터 N번 과목까지 차례대로 최소 몇 학기에 이수할 수 있는지
# n <= 1000, m <= 500000
from collections import deque
import sys

# 위상정렬 사용
def solution1():
  n, m = map(int, input().split())

  indegree = [0] * (n + 1)
  graph = [[] for _ in range(n + 1)]
  ret = [0] * (n + 1)

  for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

  # 위상정렬 : 시간 복잡도 O(V + E)
  def topoloy_sort():
    q = deque()
    
    for i in range(1, n + 1):
      if indegree[i] == 0:
        q.append((i, 1)) # i: 과목 번호
    
    while q:
      now, semester = q.popleft()
      ret[now] = semester
          
      for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
          q.append((nxt, semester + 1))

  topoloy_sort()
  print(*ret[1:]) # 0번 과목은 없으므로 제외

# dp 사용
def solution2():
  input = sys.stdin.readline
  n, m = map(int, input().split())
  graph = [1] * (n + 1)
  arr = []
  
  for i in range(m):
    a, b = map(int, input().split())
    arr.append((a, b))
  
  arr.sort()
  
  for a, b in arr:
    if graph[b] <= graph[a]:
      graph[b] = graph[a] + 1
  
  print(*graph[1:])
  
solution2()