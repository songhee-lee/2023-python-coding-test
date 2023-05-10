'''
- A에는 속하지만 B에는 속하지 않는 원소를 쉽게 구하기 위해 set자료구조 사용
- 입력받은 a와 b를 리스트로 받은 후 set으로 변환
- "a - b"(차집합)을 정렬된 리스트로 변환
- 출력
'''

import sys

n, m = map(int, sys.stdin.readline().split())

# Set으로 입력받는다.
a = set(list(map(int, sys.stdin.readline().split())))
b = set(list(map(int, sys.stdin.readline().split())))

# 차집합을 리스트로 변환하고 정렬한다.
a = sorted(list(a - b))

# A에는 속하면서 B에도 속한다.
if not a: 
    print(0)
# A에는 속하면서 B에는 속하지 않는다.
else: 
    print(len(a)) 
    for x in a:
        print(x, end=' ')