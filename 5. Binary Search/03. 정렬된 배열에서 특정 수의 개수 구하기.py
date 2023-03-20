""" 
- 오름차순 정렬된 수열에서 x가 등장하는 횟수 계산하기
"""

from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
numbers = list(map(int, input().split()))

# bisect 패키지 이용
res = bisect_right(numbers, x) - bisect_left(numbers, x)
print(res) if res else print(-1)

####################################
# 계수 정렬 활용
####################################
counting_sort = [0] * 1000001
for i in input().split():
    counting_sort[int(i)] += 1

print(-1) if counting_sort[x] == 0 else print(counting_sort[x])

####################################
# 이진 탐색 활용
####################################

# x 왼쪽, 오른쪽 찾는 함수
def find(numbers, m, x):
    left, right = 0, 0
    for i in range(m, 0, -1):
        if numbers[i] != x:
            left = i+1
    for i in range(m, N):
        if numbers[i] != x:
            right = i-1
    return left, right

# x 탐색하기
s, e = 0, N-1
left, right = 0, 0
while s <= e:
    m = (s+e) // 2

    if numbers[m] == x :
        left, right = find(numbers, m, x)
        break
    elif numbers[m] < x :
        s = m+1
    else:
        e = m-1

print(-1) if left == right else print(right-left)