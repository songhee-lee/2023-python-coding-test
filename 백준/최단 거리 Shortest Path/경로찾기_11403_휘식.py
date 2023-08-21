n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
  

for k in range(n):
  for i in range(n):
    for j in range(n):
      if graph[i][k] and graph[k][j]:
        graph[i][j] = 1

for i in range(n):
  print(*graph[i])