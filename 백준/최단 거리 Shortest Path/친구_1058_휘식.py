# '2-친구'의 조건 -> 두 사람이 친구거나 / 친구의 친구거나: 플로이드 와샬
# 목표: 2-친구의 수가 가장 많은 사람의 2-친구의 수 찾기
from pprint import pprint
n = int(input())
graph = []
friends = [[0] * n for _ in range(n)]

for _ in range(n):
  _input = list(input())
  graph.append(_input)

for k in range(n):
  for i in range(n):
    for j in range(n):
      if i == j: continue
      if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] == 'Y'):
        friends[i][j] = 1

max_friends = 0
for i in range(n):
  max_friends = max(max_friends, sum(friends[i]))

print(max_friends)