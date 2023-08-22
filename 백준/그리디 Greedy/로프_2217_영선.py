#입력1 : N 로프 개수
#입력2 : N개의 줄에 각 로프가 버틸 수 있는 최대 중량

#병렬 연결하면 w/k  ==> min(로프) * k
#출력 : 최대 중량 구하기 (모든 로프를 사용하지 않아도 된다)
import sys

n = int(input())

rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse = True)

answer = -1
cnt = 0
for i in range(n):
    cnt += rope[i] * (i+1)
    if answer < cnt:
        answer = cnt
    cnt = 0

print(answer)
