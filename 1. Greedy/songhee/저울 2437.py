
"""Psudo Code

1. 입력 받아 배열에 저장
2. 저울추 정렬 후 카운팅

"""

# 1. 입력 받기
N = int(input())
weighs = list(map(int, input().split()))

# 2. 정렬 후 카운팅
weighs.sort()

target = 1
for w in weighs:
    if target < w :
        break
    target += w

print(target)