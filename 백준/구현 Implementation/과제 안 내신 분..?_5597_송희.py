"""
1~30번의 학생이 있다. 
특별과제를 제출한 학생들의 출석번호가 주어질 때, 제출하지 않은 학생의 번호를 오름차순으로 출력하기
"""

submit = set([int(input()) for _ in range(28)])
numbers = set([i for i in range(1, 31)])
for num in sorted(numbers-submit) :
    print(num)
