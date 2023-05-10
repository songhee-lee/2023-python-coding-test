""" 
- 캠프 때 쓸 N개의 랜선 만들기
- K개 랜선을 모두 N개의 같은 랜선으로 만들기
- 
"""

K, N = map(int, input().split())    # 가진 랜선 개수, 필요한 랜선 개수
lines = [ int(input()) for _ in range(K) ]

lines.sort()

# 랜선 자르기 함수
def cutting(lines, target):
    cnt = 0
    for x in lines:
        cnt += x // target
    return cnt

# 잘라야할 랜선 길이 구하기
s, e = 1, lines[-1]
answer = 0
while s <= e:
    h = (s+e) // 2

    cnt = cutting(lines, h)
    if cnt >= N :
        answer = h
        s = h+1
    else:
        e = h-1

print(answer)

