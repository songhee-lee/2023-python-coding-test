n, m = map(int, input().split())
graph = []
orders = []

for _ in range(n):
  graph.append(list(map(int, input().split())))

for _ in range(m):
  orders.append(list(map(int, input().split())))

