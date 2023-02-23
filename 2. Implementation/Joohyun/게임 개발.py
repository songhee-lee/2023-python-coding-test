N, M = map(int, input().split())
x, y, d = map(int, input().split())
Map = []
for n in range(N):
	Map.append(list(map(int, input().split())))

move = [(0,-1), (1,0), (0,1), (-1,0)]
count = 0

while True:
	exception = 0
	for i in range(4):
		X, Y = x, y
		d = (d+1) % 4
		dx, dy = move[d]
		X += dx
		Y += dy

		if Map[X][Y]==0:
			Map[X][Y]=-1
			x, y = X, Y
			count+=1
			exception=1
			break
		else:continue

	if exception==0:
		D=(d+2)%4
		X,Y=move[D]
		x+=X
		y+=Y
		
		if Map[x][y]==1:break
		else:continue

print(count)