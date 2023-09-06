#입력1 : n 서 있는 사람의 수
#입력2(n개의 줄) : 각 사람이 주려고 하는 팁

#출력 : 강호가 받을 수 있는 팁의 최대값
'''
팁 : 원래 팁 - (받은 등수 - 1)
음수면 0원
'''
import sys

n = int(input())
tips = []
for _ in range(n):
    tips.append(int(input()))

tips.sort(reverse=True)
answer = 0
for i in range(n):
    tip = tips[i] - i
    if tip < 0:
        break
    answer += tip
  
print(answer)
