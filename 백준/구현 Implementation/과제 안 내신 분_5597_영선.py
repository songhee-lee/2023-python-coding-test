#입력 : 28줄, 제출자의 출석번호

#출력 : 1번째 줄 - 제출하지 않은 번호 중 작은 것
#       2번재 줄 - 그 다음 출석번호


import sys

student  = [False] * 31

for _ in range(28):
    student[int(input())] = True

for i in range(1, 31):
    if student[i] == False:
        print(i)
