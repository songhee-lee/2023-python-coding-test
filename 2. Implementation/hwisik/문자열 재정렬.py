'''
1. 입력값을 리스트로 변환한다.
2. 숫자와 알파벳을 구분하여 각 변수에 따로 저장한다.
3. 둘을 규칙에 맞게 더한다.
'''
'''
** 비슷한 함수의 다른 성질 **
    isdigit() : 해당 문자열이 '숫자'로 이루어져 있는지 확인한다. 예를 들어, 제곱수 3^2도 숫자로 취급한다.
    isdecimal() : 해당 문자열이 '0~9까지의 수'로 이루어진 것인지 확인한다. 즉, int()로 변환할 수 있는지 확인한다.
    isnumeric() : 위의 두 함수보다 좀 더 폭넓은 의미를 가진다. '수로 볼 수 있는 것'인 경우 True를 return.
'''

import collections
import sys

# 정렬을 하기 위해 list로 변환
s = list(sys.stdin.readline().rstrip()) # 입력 맨 끝에 '\n'이 들어오므로 rstrip() 수행

s.sort() # 오름차순 정렬

numeric_sum = 0 # 모든 숫자를 더한 변수
alpha_string = '' # 알파벳을 이은 변수

for x in s:
    if x.isdecimal(): # 만약 숫자라면 
        numeric_sum += int(x) 
    else: # 알파벳이라면
        alpha_string += x

ret = alpha_string + str(numeric_sum) # 문자열 재조합
print(ret)

