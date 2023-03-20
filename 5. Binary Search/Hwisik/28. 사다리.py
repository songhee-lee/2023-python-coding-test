'''
- 수학 공식 & 이진 탐색 사용
- 두 빌딩이 교차하는 지점의 크기(높이)를 이분탐색의 mid(기준)으로 설정
- 교차 지점을 계산하면서, 계산한 결과와 c를 비교해서 l과 r을 조절한다.
'''

import sys

# 이진 탐색
def binary_search():
    l, r = 0, min(x, y)
    ret = 0 # 두 빌딩 사이의 너비가 되는 수치
    
    while r - l > 1e-6: # 0.000001
        mid = l + (r - l) / 2 # 두 빌딩 사이의 너비
        
        # 주어진 c와 높이가 같거나 크다면
        if calc(x, y, mid) >= c:
            ret = mid # 너비 저장
            l = mid # 너비가 좁다는 의미, 오른쪽 부분 탐색 
        else:
            r = mid # 너비가 넓다는 의미, 왼쪽 부분 탐색
            
    return ret

# 두 사다리가 교차하는 지점 찾기
def calc(x, y, z):
    hx = (x ** 2 - z ** 2) ** 0.5
    hy = (y ** 2 - z ** 2) ** 0.5
    h = (hx * hy) / (hx + hy)
    
    return h

x, y, c = map(float, sys.stdin.readline().split())

# 이진 탐색 수행
ret = binary_search()

# 출력
print(ret)