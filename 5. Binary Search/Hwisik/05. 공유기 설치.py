'''
- n개의 집 위치, c개의 공유기
- 가장 인접한 두 공유기 사이의 거리의 최댓값 구하기
- l과 r은 각각 공유기 사이의 거리의 최솟값과 최댓값
- mid는 l과 r은 중간값
    - mid를 조절하면서, 설치한 공유기의 개수가 C개를 넘어가면,
        공유기를 좁게 설치했다는 의미이므로, mid를 늘린다.
    - 설치한 공유기의 개수가 C개가 안된다면,
        공유기를 너무 넓게 설치한 것이므로, mid를 줄인다.

-> ✅다시풀기
'''

import sys

# 이진 탐색
def binary_search():
    l, r = 1, homes[-1] - homes[0] # 시작점, 끝점 설정
    ret = 0
    
    while l <= r:
        install_count = 1 # 공유기 설치 개수
        prev = homes[0] # for문에서 비교 대상
        mid = l + (r - l) // 2 
        
        # 공유기 설치하기
        for home in homes:
            if home - prev >= mid:
                prev = home
                install_count += 1
        
        # 설치한 공유기의 개수가 C개를 넘어간다 -> 더 넓게 설치할 수 있다.
        if install_count >= c:
            l = mid + 1
            ret = mid
        # 더 좁게 설치해야 한다.
        else:
            r = mid - 1
            
    return ret
    
n, c = map(int, sys.stdin.readline().split())
homes = sorted(list(int(sys.stdin.readline()) for _ in range(n)))

# 출력
print(binary_search())