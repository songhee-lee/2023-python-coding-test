'''
1. 각 움직임에 대해서 위치를 업데이트 한다.
2. 만약, 업데이트 된 위치가 범위를 벗어난다면, 원래 위치로 되돌린다.
3. 범위를 벗어나지 않는다면, 그대로 진행한다.
'''

import collections
import sys

n = int(sys.stdin.readline()) # n을 입력받는다.
plans = list(sys.stdin.readline().split()) # 공백을 기준으로 움직임을 잘라서 list에 넣는다.
movement = {'L':(0, -1), 'R':(0, 1), 'U':(-1, 0), 'D':(1, 0)} # 각 움직임에 대한 (x, y) 값

def move(op, pos): # op : 움직임(L, R, U, D) , pos : 현재 위치
    return (pos[0] + movement[op][0], pos[1] + movement[op][1]) # 현재 위치에 움직임에 해당하는 (x, y) 값을 더해서 return.

init_pos = (1, 1) # 초기 위치는 (1, 1)

for plan in plans: # 입력받은 움직임에 대해서 순회...
    nxt = move(plan, init_pos) # 업데이트된 위치
    if 0 < nxt[0] < n and 0 < nxt[1] < n: # 범위를 벗어나지 않는다면, 초기 위치를 nxt로 업데이트.
        init_pos = nxt
    else: # 범위를 벗어난다면, 업데이트하지 않고 진행
        continue

print(init_pos[0], init_pos[1]) # 최종 위치 출력