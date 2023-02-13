N = int(input())
guild = sorted(list(map(int,input().split())))
count = 0

for mem in guild:
	if mem > N or guild[mem-1] > N:
		break
	count += 1
	N -= guild[mem-1]
	guild = guild[guild[mem-1]:]

print(count)
