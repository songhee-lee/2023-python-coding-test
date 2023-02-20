input_data = input()
row = int(input_data[1])
col = ord(input_data[0]) - ord('a') + 1

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
         (1, -2), (1, 2), (2, -1), (2, 1)]

count = 0
for r, c in steps:
    next_row = row + r
    next_col = col + c
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        count += 1

print(count)
