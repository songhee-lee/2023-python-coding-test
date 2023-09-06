# 강호가 받을 수 있는 팁의 최댓값 구하기
# 팁: 원래 주려고 생각했던 돈 - (받은 등수 - 1)
# 팁이 최대가 되려면, (받은 등수 - 1)이 최소가 되야하므로, 가장 돈을 많이 주는 손님을 맨 앞에 배치해야 함. 
import sys
n = int(sys.stdin.readline())
tips = list(int(sys.stdin.readline()) for _ in range(n))

tips.sort(reverse=True)

total_tips = 0

for i, tip in enumerate(tips):
  cur_tip = tip - (i + 1 - 1) # 팁 계산
  if cur_tip < 0:
    continue
  total_tips += cur_tip

print(total_tips)