def solution(n, lost, reserve):
	Lost1 = []
	Lost2 = []

	while len(lost) != 0:
		l = lost.pop()
		if l in reserve:
			reserve.remove(l)
		else: Lost1.append(l)
	Lost1.sort()
	while len(Lost1) != 0:
		l = Lost1.pop()
		if l+1 in reserve :
			reserve.remove(l+1)
		elif l-1 in reserve :
			reserve.remove(l-1)
		else : Lost2.append(l)
	return n - len(Lost2)
