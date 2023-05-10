'''
- 'key=lambda' 를 사용해서 문제의 조건에 맞게 정렬을 수행한다.
'''

import sys

n = int(sys.stdin.readline())

# 원소 : (이름, 국어, 영어, 수학)
students = []

for _ in range(n):
    input_data = list(sys.stdin.readline().split())
    
    name, korean, english, math = input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])
    
    students.append((name, korean, english, math))

# 1. 국어 점수 내림차순
# 2. 영어 점수 오름차순
# 3. 수학 점수 내림차순
# 4. 이름 오름차순(= 증가하는 사전 순)
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 출력
for i in range(n):
    print(students[i][0])