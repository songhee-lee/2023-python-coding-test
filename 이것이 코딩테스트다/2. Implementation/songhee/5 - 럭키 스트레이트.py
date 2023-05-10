"""Psuedo Code

1. 점수 N 입력받기
2. 반을 나누고 각 자릿수 합 더하기
"""

# 1. 입력받기
N = input()

# 2. 반 나누고 각 자릿수 합 더하기
length = len(N) // 2
left = sum(list(map(int, N[:length])))  # 왼쪽 합
right = sum(list(map(int, N[length:]))) # 오른쪽 합

if left == right :
    print("LUCKY")
else:
    print("READY")
