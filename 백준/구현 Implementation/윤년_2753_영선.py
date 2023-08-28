#입력1 : 연도
#윤년 : 연도가 4의 배수이면서, (100의 배수가 아닐때 or 400의 배수일때)

#출력 : 윤년이면 1 아니면 0
import sys

k = int(input())

if k % 4 == 0:
    if not(k % 100 == 0) or (k % 400 == 0):
        print("1")
    else:
        print("0")
else:
    print("0")
