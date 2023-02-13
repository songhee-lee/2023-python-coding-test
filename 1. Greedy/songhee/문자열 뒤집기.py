"""Pseudo Code

1. 문자열 입력 받기
2. 0과 1 묶음대로 분할했을 때 더 작은 묶음이 정답

"""

# 1. 입력 받기
s = input()

# 2. 0과 1 묶음대로 분할
zero, one = 0, 0          # 0 묶음 개수, 1 묶음 개수
before = ''               # 이전 숫자
for x in s :     
    if before != x :        # 이전 숫자와 다를 때
        if x == '0' :       # 1 -> 0
            zero += 1
            before = '0'
        else :              # 0 -> 1
            one += 1
            before = '1'

# 더 작은 묶음 수 출력
print(min(zero, one))

        