col, row = input()
column = ['a','b','c','d','e','f','g','h']
col = column.index(col)
row = int(row)

col_move = [2,2,-2,-2,1,-1,1,-1]
row_move = [1,-1,1,-1,2,2,-2,-2]
moved_col = [c+col for c in col_move]
moved_row = [r+row for r in row_move]

count = 0
for c, r in zip(moved_col,moved_row):
	if c>=0 and c<=7 and r>=1 and r<=8 : count+=1

print(count)