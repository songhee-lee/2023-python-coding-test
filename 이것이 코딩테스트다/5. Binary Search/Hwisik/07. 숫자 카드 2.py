'''
- 정렬된 배열에서 특정 수의 개수 구하기.py와 유사
- 풀이 2개
    1. 이분탐색 함수 2개 만들어서 사용
    2. Dictionary 사용
'''

import sys

#-- 풀이 1) 이분탐색 함수 2개 사용

# target이 등장하는 시작 인덱스 찾기 - 이분탐색
def get_first_position(l, r, target):
    while l <= r:
        mid = l + (r - l) // 2
        if target <= cards[mid]:
            r = mid - 1
        else:
            l = mid + 1
            
    return l

# target이 등장하는 끝 인덱스 찾기 - 이분탐색
def get_last_position(l, r, target):
    while l <= r:
        mid = l + (r - l) // 2
        if target < cards[mid]:
            r = mid - 1
        else:
            l = mid + 1
            
    return l      
            
n = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
to_check = list(map(int, sys.stdin.readline().split()))

# 찾기 & 출력
for target in to_check:
    first_index = get_first_position(0, n - 1, target)
    last_index = get_last_position(0, n - 1, target)
    
    print(last_index - first_index, end=' ')
    
#-- 풀이 2) Dictionary 사용


dic = {} # 숫자 카드에 등장하는 수와 개수를 저장하는 딕셔너리

# 수와 개수 저장
for card in cards:
    if card in dic:
        dic[card] += 1
    else:
        dic[card] = 1

# 해당 수가 딕셔너리에 있는지 확인 & 출력
for target in to_check:
    if target in dic:
        print(dic[target], end=' ')
    else:
        print(0, end=' ')