'''
1. 나이트가 이동할 수 있는 방향 8가지를 정의한다.
2. 초기 위치에 각 방향의 값을 더해서 업데이트한다.
3. 업데이트된 위치가 범위를 벗어나지 않았다면 결과 값을 1 증가시킨다.
'''

import collections
import sys

data = sys.stdin.readline() # 현재 나이트가 위치한 곳의 좌표 입력받는다.

init_x = int(data[1]) # 행
init_y = int(ord(data[0]) - ord('a')) + 1 # 열

dirs = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] # 나이트가 이동할 수 있는 8가지 방향

ret = 0 # 결과 return 변수
for dir in dirs:
    next_x, next_y = init_x + dir[0], init_y + dir[1]
    if 1 <= next_x <= 8 and 1 <= next_y <= 8:
        ret += 1
print(ret)