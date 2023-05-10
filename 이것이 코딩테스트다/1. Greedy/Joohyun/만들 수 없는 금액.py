N = int(input())
coins = sorted(list(map(int,input().split())))
result = 1
for coin in coins:
	if result < coin:
		break
	result+=coin
print(result)
