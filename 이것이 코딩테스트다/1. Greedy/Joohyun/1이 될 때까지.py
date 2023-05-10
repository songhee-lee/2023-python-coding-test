N, K = map(int, input().split())
count = 0

while N != 1 :
	count += N%K+1
	N //= K

print(count)
