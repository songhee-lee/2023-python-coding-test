N = int(input())

coins = [500,100,50,10]
sum = 0
for coin in coins:
	sum += N // coin
	N %= coin
print(sum)
