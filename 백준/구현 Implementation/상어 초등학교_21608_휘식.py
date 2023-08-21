n = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
liked = [[] for _ in range(n ** 2 + 1)]

for _ in range(n ** 2):
  a, *b = map(int, input().split())
  liked[a] = b
  
  candidate = []
  
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if graph[i][j] == 0:
        empty_seat = 0
        like_seat = 0
        
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
          nx, ny = i + dx, j + dy
          
          if 1 <= nx < n + 1 and 1 <= ny < n + 1:
            if graph[nx][ny] in liked[a]:
              like_seat += 1
            
            if graph[nx][ny] == 0:
              empty_seat += 1
        
        candidate.append((like_seat, empty_seat, i, j))
  
  candidate.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
  
  graph[candidate[0][2]][candidate[0][3]] = a

result = 0
for i in range(1, n + 1):
  for j in range(1, n + 1):
    like = 0    
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
      nx, ny = i + dx, j + dy
      if 1 <= nx < n + 1 and 1 <= ny < n + 1:
        if graph[nx][ny] in liked[graph[i][j]]:
          like += 1
        
    if like != 0:
      result += 10 ** (like - 1)

print(result)