""" 
[ 조건 ]
- 절단기 높이 H에 맞춰 떡을 한 번에 절단
- 손님이 요청한 M 만큼의 떡을 얻기 위해 설정할 수 있는 H의 최댓값 구하기

** N : 1,000,000 이고 시간제한 2초
-> 40,000,000 연산 안에 해결

[ Flow ] 
1. h 정하기
2. h 보다 큰 떡의 인덱스 구하기
3. abs(x-h) 합 구한 후 비교
    -> h 보다 큰 떡의 개수 : k 개
    -> h가 1 오를 때마다 +(h보다 큰 떡의 개수)
"""
from bisect import bisect_left

N, M = map(int, input().split())
ricecake_set = set(map(int, input().split()))

# 정렬 O(N)
ricecake = sorted(list(ricecake_set))

# 가져갈 수 있는 떡의 개수 구하기
def calc(ricecake, h):
    return sum([x-h for x in ricecake])

# 이진 탐색
s, e = 0, ricecake[-1]
answer = 0
while s <= e:
    # 1. h 정하기
    h = (s+e) // 2

    # 2. h 인덱스 구하기
    index = bisect_left(ricecake, h)

    # 3. 떡 개수 계산하기
    res = calc(ricecake[index:], h)

    if res == M :     # 개수가 딱 맞는 경우
        answer = h
        break
    # 떡이 부족한 경우
    elif res < M :    
        e = h-1     # 더 많이 자르기     
    # 떡이 더 많은 경우
    else:             
        res = h
        s = h+1

print(answer)