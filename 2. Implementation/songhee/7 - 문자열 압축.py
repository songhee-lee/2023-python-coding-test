"""Psuedo Code

1. 문자열 입력받기
2. 문자열의 절반 만큼 연속된 문자의 반복 확인하기
    - 1번 반복될 때는 숫자를 붙이지 않는다.
"""

# 1. 입력 받기
string = input()

# 2. 문자열 반복 확인하기
length = len(string)
result = len(string)   # 현재 문자열의 길이

#  1개 ~ 문자열 절반 크기만큼의 연속된 문자열 반복 확인하기
for i in range(1, length // 2 + 1): 
    prev = string[:i]   # 이전 문자열
    c = 1               # 반복 횟수
    tmp = ''            # 압축된 문자열

    for j in range(i, length, i):
        now = string[j:j+i]
        if prev == now :    # 문자열 반복이면 횟수 추가
            c += 1
        else :
            tmp += str(c) + prev if c >= 2 else prev
            prev = now
            c = 1
    
    tmp += str(c) + now if c >= 2 else prev # 마지막 문자열 추가
    result = min(result, len(tmp))

print(result)
