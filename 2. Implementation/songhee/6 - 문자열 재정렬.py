"""Psuedo Code

1. 문자열 입력받기
2. 알파벳끼리 오름차순 정렬 + 숫자끼리 더하기
"""
import re

# 1. 입력받기
string = input()

# 2. 알파벳끼리 오름차순 정렬 + 숫자끼리 더하기
num = list(map(int, re.sub(r'[^0-9]', '', string))) # 숫자만 남기기
alpha = re.sub(r'[^A-Z]', '', string)   # 알파벳만 남기기

result = ''.join(sorted(alpha)) + str( sum(num))
print(result)
