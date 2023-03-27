""" 
- 3차원 좌표 평면위 선분 AB 와 점 C 사이의 거리 최솟값 구하기
"""

ax, ay, az, bx, by, bz, cx, cy, cz = list(map(int, input().split()))
ans = float('inf')

while True:
    mx, my, mz = (ax+bx)/2, (ay+by)/2, (az+bz)/2
    l = ((ax-cx)**2+(ay-cy)**2+(az-cz)**2)**0.5  
    h = ((mx-cx)**2+(my-cy)**2+(mz-cz)**2)**0.5 
    r = ((bx-cx)**2+(by-cy)**2+(bz-cz)**2)**0.5

    if abs(l-r) <= 1e-6:     # 최솟값 업데이트
        print(h)
        exit(0)
    
    # 왼쪽 선분이 더 길면 A를 앞으로
    if l > r:
        ax, ay, az = mx, my, mz
    # 오른쪽 선분이 더 길면 B를 앞으로
    else:
        bx, by, bz = mx, my, mz