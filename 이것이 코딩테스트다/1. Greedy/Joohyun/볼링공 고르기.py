N, M = map(int,input().split())
balls = list(map(int, input().split()))
count = 0
b = balls.pop()
while balls:
	count += len(balls)
	if not balls.count(b) == -1:
		count -= balls.count(b)
	b = balls.pop()
print(count)
