"""Pseudo Code
1. 맵 크기 N과 이동 계획서 입력 받기
2. x, y를 1~N 까지로 제한을 두고, 이동 계획서에 따라 더하고 빼기
    - 맵을 벗어나는 이동은 무시된다.
"""

# 1. 입력 받기
N = int(input())
moves = list(input().split())

# 2. 이동 계획서 따라 더하고 빼기
x, y = 1, 1
for m in moves :
    if m == 'L' and x > 1:
        x -= 1
    elif m == 'R' and x < N:
        x += 1
    elif m == 'U' and y > 1:
        y -= 1
    elif m == 'D' and y < N:
        y += 1

print(y, x)
