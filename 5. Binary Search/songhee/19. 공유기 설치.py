
import sys

N, C = map(int, input().split())
houses = [ int(sys.stdin.readline()) for _ in range(N) ]

houses.sort()

# 공유기 설치가 2개 일 때
if C == 2:
    print(houses[-1] - houses[0])
    exit(0)

# 공유기 설치하기
s, e = 1, houses[-1] - houses[0]
answer = 0
while s <= e:
    m = (s+e) // 2      # 거리
    cur = houses[0]     # 시작점
    cnt = 1             # 공유기 개수

    for i in range(1, N):
        if houses[i] - cur >= m :
            cnt += 1
            cur = houses[i]
        
    # 공유기 설치가 가능하면 정답 
    if cnt >= C:
        s = m+1
        answer = m
    # 공유기 설치 불가능하면 범위 좁히기
    else:
        e = m-1

print(answer)
    
