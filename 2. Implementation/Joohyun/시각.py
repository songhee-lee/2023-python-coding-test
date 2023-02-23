N = int(input())

hours = [3, 13, 23]
h_3, not_3 = 0,0

for h in hours :
	if N >= h : h_3 += 1

print( h_3*3600 + (N+1-h_3)*1575 )