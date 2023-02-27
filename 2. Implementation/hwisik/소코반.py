'''

'''

from pprint import pprint

def move(x, y):
    for step in movement:
        nx, ny = x + dir[step][0], y + dir[step][1]
        
        if graph[nx][ny] in 'bB':
            nnx, nny = nx + dir[step][0], ny + dir[step][1]
            
            if graph[nnx][nny] in'.+':
                if graph[nnx][nny] == '+':
                     

            
        

dir = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)} # 상, 하, 좌, 우
while 1:
    r, c = map(int, input().split())
    
    if r == 0 and c == 0: break
    
    graph = []
    for _ in range(r):
        data = list(input().rstrip())
        graph.append(data)
    movement = list(input().rstrip())
    
    cx, cy = 0, 0
    just_box, target_box = 0, 0
    dest = []
    
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'w':
                cx, cy = i, j
            elif graph[i][j] == 'W':
                dest.append((i, j))
                cx, cy = i, j
                target_box += 1
            elif graph[i][j] == 'B':
                dest.append((i, j))
                just_box += 1
                target_box += 1
            elif graph[i][j] == 'b':
                just_box += 1
            elif graph[i][j] == '+':
                dest.append((i, j))
                target_box += 1
    