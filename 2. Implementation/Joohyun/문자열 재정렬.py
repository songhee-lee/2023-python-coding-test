S = list(input())
Numbers = ['0','1','2','3','4','5','6','7','8','9']
alph,num = [],0
while S :
	s = S.pop()
	if s in Numbers : num += int(s)
	else : alph.append(s)
print('{0}{1}'.format(''.join(sorted(alph)),num))