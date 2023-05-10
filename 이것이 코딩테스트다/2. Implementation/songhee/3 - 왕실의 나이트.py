"""Psuedo Code
1. 현재 나이트 좌표 입력 받기
2. 이동할 수 있는 경우의 수 세기
    - 수평(좌, 우) -> 수직(위, 아래)
    - 수직(위, 아래) -> 수평(좌, 우)
"""

# 1. 입력 받기
loc = input()
x, y= ord(loc[0]) - ord('a') + 1, int(loc[1])

# 2. 경우의 수 세기
dx = (-2, -2, 2, 2, -1, 1, -1, 1)
dy = (-1, 1, -1, 1, -2, -2, 2, 2)
result = 0

for i, j in zip(dx, dy):
    if 0 < x+i < 9 and 0 < y+j < 9 :
        result += 1

print(result)