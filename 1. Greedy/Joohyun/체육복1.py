def solution(n, lost, reserve):
	Lost = set(lost)-set(reserve)
	Reserve = set(reserve)-set(lost)
	for l in Lost:
		if l-1 in Reserve:
			Reserve.remove(l-1)
		elif l+1 in Reserve:
			Reserve.remove(l+1)
		else:
			n-=1
	return n
