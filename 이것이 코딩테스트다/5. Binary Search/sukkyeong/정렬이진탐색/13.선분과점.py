'''
점 a를 선분의 왼쪽에 있는 점, 점 b를 선분의 오른쪽에 있는 점이라 생각합니다.

점 a와 점 b의 중간점 m을 구합니다.

l = 점 a와 점 c의 거리

r = 점 b와 점 c의 거리

h = 점 m과 점 c의 거리

를 계산해줍니다.

만약 h가 현재 존재하는 최소값 ans보다 작다면, ans를 h로 갱신해줍니다.

만약 l이 r보다 크다면, c가 a보다 b에 더 가깝게 있다는 뜻이므로 점 a를 점 m으로 바꿔줍니다.

(이분탐색을 진행해야 하므로 더 가까운 쪽으로 범위를 좁혀줘야 하기 때문입니다.)

반대로 r이 l보다 크다면 c가 b보다 a에 더 가깝게 있다는 뜻이므로 점 b를 점 m으로 바꿔줍니다.
'''

ax, ay, az, bx, by, bz, cx, cy, cz = map(int, input().split())

ans = float('inf')

while True:
    mx, my, mz = (ax+bx)/2, (ay+by)/2, (az+bz)/2
    l = ((ax-cx)**2+(ay-cy)**2+(az-cz)**2)**0.5
    h = ((mx-cx)**2+(my-cy)**2+(mz-cz)**2)**0.5
    r = ((bx-cx)**2+(by-cy)**2+(bz-cz)**2)**0.5

    if abs(ans-h) <= 1e-6:
        print('%0.10f' % ans)
        exit()
    if h < ans:
        ans = h
    if l > r:
        ax, ay, az = mx, my, mz
    else:
        bx, by, bz = mx, my, mz
