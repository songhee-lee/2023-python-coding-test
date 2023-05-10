""" 
- 집 N개가 있을 때 C개의 공유기 설치
- 가장 인접한 두 공유기의 거리를 최대로 하기

*** sys 입력 안받으면 시간 초과
"""
import sys

N, C = map(int, input().split())
houses = []
for i in range(N):
    houses.append(int(sys.stdin.readline()))

# 정렬
houses.sort()

# 예외 처리
if C == 2:
    print(houses[-1] - houses[0])
    exit(0)

# 공유기 설치
s, e = 1, houses[-1] - houses[0]    # 최소 거리, 최대 거리
answer = 0

while s <= e:
    m = (s+e) // 2      # 중간 거리
    cur = houses[0]     # 시작점
    cnt = 1             # 공유기 개수

    # 설치 가능한 공유기 개수 구하기
    for i in range(1, N):
        if houses[i] - cur >= m :
            cnt += 1
            cur = houses[i]
    
    # 공유기 설치 다 됐으면 통과
    if cnt >= C :
        s = m+1
        answer = m
    else:
        e = m-1
    
print(answer)
