'''
1. 정수형을 반으로 나누기는 까다로우므로, str타입을 가지는 list로 변환한다.
2. 점수 N을 반으로 나눴을 때 왼쪽, 오른쪽 각각의 합을 구한다.
3. 둘을 비교한다.
'''

import collections
import sys

# solution 1 - TC : O(NK)
n = int(input()) # n 입력받기
tmp = str(n)
n_to_str_list = list(str(n)) # n을 str 타입 리스트로 변환
list_len = len(n_to_str_list) # list의 길이

left, right = sum(map(int, n_to_str_list[:list_len // 2])), sum(map(int, n_to_str_list[list_len // 2:])) # 점수 N을 반으로 나눴을 때 왼쪽, 오른쪽 각각의 합

if left == right: # 합이 같다면 '럭키 스트레이트'!
    print('LUCKY')
else:
    print('READY')

# solution 2 - Time Complexity : O(N^2)
n = input() 
length = len(n) # 점수 N의 총 자릿수
left, right = 0, 0 # 왼쪽, 오른쪽의 합

for i in range(length // 2): # 왼쪽 합 구하기
    left += int(n[i])

for i in range(length // 2, length): # 오른쪽 합 구하기
    right += int(n[i])
    
if left == right: # 왼쪽 합과 오른쪽 합이 동일한지 검사한다.
    print('LUCKY')
else:
    print('READY')