"""
연도가 주어졌을 때, 윤년이면 1 아니면 0 출력하기
윤년 = 연도가 4의 배수이면서 100의 배수가 아닐 때, 또는 400의 배수일 때
"""

year = int(input())
answer = 0
if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0 :
        answer = 1

print(answer)