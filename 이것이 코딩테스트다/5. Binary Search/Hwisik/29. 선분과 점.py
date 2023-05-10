'''
- 점 a와 점 b의 중간점 m을 설정한다.
- 점 a와 점c의 거리를 찾는다. -> a_to_c
- 점 b와 점c의 거리를 찾는다. -> b_to_c
- a_to_c > b_to_c 라면...
    - 점 c가 점 b에 더 가까이 있는 것 -> 점 a를 점 m으로 바꾼다.
- a_to_c < b_to_c 라면...
    - 점 c가 점 a에 더 가까이 있는 것 -> 점 b를 점 m으로 바꾼다.
'''

import sys

# 점 a와 점 b에 대한 이진탐색
def binary_search(ax, ay, az, bx, by, bz):
    ret = float('inf')
    
    while True:
        # 점 m : 점 a와 점 b의 중간점
        mx, my, mz = (ax + bx) / 2, (ay + by) / 2, (az + bz) / 2
        
        # a - c, b - c, m - c 거리 구하기
        a_to_c = calc(ax, ay, az, cx, cy, cz)
        b_to_c = calc(bx, by, bz, cx, cy, cz)
        m_to_c = calc(mx, my, mz, cx, cy, cz)
        
        if abs(ret - m_to_c) <= 1e-6:
            return ret
        
        ret = min(ret, m_to_c)
        
        # a - c가 b - c 보다 크다면
        # 점 c가 점 b에 가까이 있다.
        if a_to_c > b_to_c:
            ax, ay, az = mx, my, mz
            
        # 점 c가 점 a에 가까이 있다.
        else:
            bx, by, bz = mx, my, mz
            
    return ret


# 두 점 사이의 거리 계산
def calc(x1, y1, z1, x2, y2, z2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5    

# 입력
ax, ay, az, bx, by, bz, cx, cy, cz = map(int, sys.stdin.readline().split())

# 이진 탐색 수행
ret = binary_search(ax, ay, az, bx, by, bz)

print('%0.10f' %ret)