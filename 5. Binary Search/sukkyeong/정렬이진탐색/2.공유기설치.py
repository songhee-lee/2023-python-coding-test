'''
공유기 사이의 거리를 가장 크게 설치
1. array라는 리스트에 집들의 좌표를 입력받은 후에 정렬

2. start = 1, end = array[-1] - array[0] 으로 설정( 시작값은 최소 거리, 끝 값은 최대 거리 )

3. 앞 집부터 공유기 설치

4. 설치할 수 있는 공유기 개수가 c개를 넘어가면 더 넓게 설치할 수 있다는 이야기 이므로 설치거리를 mid + 1로 설정하여 다시 앞집부터 설치

5. c개를 넘어가지 않는다면 더 좁게 설치해야 한다는 이야기 이므로 mid - 1로 설정
'''
import math
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
h = [int(input()) for i in range(n)]
h.sort()
start, end = 1, h[n-1] - h[0]
# 집 사이의 최소 거리, 최대 거리
result = 0

if c == 2:
    print(h[n-1] - h[0])
    # 집이 2개라면 무조건 처음, 마지막 집 사이의 거리
else:
    while (start < end):
        mid = (start + end)//2

        count = 1
        ts = h[0]
        # 마지막으로 설치된 공유기의 위치
        for i in range(n):
            if h[i] - ts >= mid:
                count += 1
                ts = h[i]
        if count >= c:
            result = mid
            start = mid + 1
        elif count < c:
            end = mid
    print(result)
