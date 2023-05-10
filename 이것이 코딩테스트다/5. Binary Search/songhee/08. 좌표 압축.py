""" 
xi 를 좌표 압축한 결과 x'i 값은 xi > xj 를 만족하는 서로 다른 좌표의 개수
- 자신보다 작은 좌표들의 개수
"""
import sys

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

# 숫자별 좌표 개수 세기
# (나보다 작은 좌표들의 개수, 나와 같은 좌표 개수)
new_numbers = sorted(numbers)
counting = { new_numbers[0]: [0, 1]}
prev = new_numbers[0]
for num in new_numbers[1:]:
    if num in counting:
        counting[num][1] += 1
    else:
        counting[num] = [ counting[prev][0]+1, 1]
        prev = num

# 구하기
print(*[ counting[x][0] for x in numbers])
