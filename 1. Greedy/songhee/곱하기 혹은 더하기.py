
"""Psuedo Code
1. 문자열 입력 받고 숫자 리스트로 변환
2. 두 숫자 중 하나라도 1보다 작으면 더하기, 아니면 곱하기
"""

# 1. 입력 받기
s = [ int(x) for x in input() ]

# 2. 계산
result = s[0]    
for i in s[1:] :      
    if result <= 1 or i <= 0 :    # 1보다 작으면 더하기
        result += i
    else:                         # 아니면 곱하기
        result *= i

print(result)

