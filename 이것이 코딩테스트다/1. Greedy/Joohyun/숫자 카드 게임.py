N, M = map(int,input().split())
cards = []

for i in range(N):
	cards.append(min(list(map(int,input().split()))))

print(max(cards))
