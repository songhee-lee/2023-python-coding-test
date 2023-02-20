N = int(input())
Move = input()
Row, Col = 1,1

while Move:
	LRUD = set(Move)
	
	# 1) 이동 방향 및 이동 횟수 구하기
	if len(LRUD) == 1 : # 예외처리 : 이동 방향이 한 종류일 경우
		fir = Move[0]
		move = len(Move)
		if fir in 'LU' : move *= -1
		
	else : 
		m = {}
		# 이동방향 우선순위
		for i in LRUD:
			m[i] = Move.index(i)

		# 이동방향 : fir, 이동횟수 : move
		fir, sec = sorted(m, key=lambda i:m[i])[0:2]
		move = m[sec]-m[fir]
		if fir in 'LU' : move *= -1

	
	# 2) 이동시키기
	if fir in 'LR':
		Col += move
		if Col < 1 : Col = 1
		elif Col > N : Col = N
	else:
		Row += move
		if Row < 1 : Row = 1
		elif Row > N : Row = N

	Move = Move[abs(move):]

print(Row,Col)
