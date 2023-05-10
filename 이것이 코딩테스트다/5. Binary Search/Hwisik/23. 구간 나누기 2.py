'''
[설명]
- N개의 수로 이루어진 1차원 배열이 있다. 이 배열을 M개 이하의 구간으로 나누어서, 구간의 점수의 최댓값을 최소로 하려고 한다.
    - 하나의 구간은 하나 이상의 연속된 수들로 이루어져 있다.
    - 뱁열의 각 수는 모두 하나의 구간에 포함되어 있어야 한다.
- 구간의 점수 : 최대값 - 최솟값

[아이디어]
- 이진탐색을 수행하는데 어떤 것을 mid로 설정할 것인가?

-> ✅ 다시풀기
'''

import sys

# 구간 나누기
def split_sector(mid):
    _min = arr[0]  # 구간에서 가장 작은 값
    _max = arr[0]  # 구간에서 가장 큰 값
    sector_count = 1  # 구간의 개수

    for i in range(1, n):
        _min = min(_min, arr[i])
        _max = max(_max, arr[i])

        # 구간의 점수가 기준값(mid)보다 크면
        # 구간을 나눌 수 있다
        if _max - _min > mid:
            sector_count += 1
            _min = arr[i]
            _max = arr[i]

    return sector_count  # 구간의 개수 반환


# 이진 탐색
def binary_search():
    l, r = 0, max(arr)
    ret = 0
    while l <= r:
        mid = l + (r - l) // 2  # 각 구간의 점수의 최댓값 중 최솟값

        # 구간의 개수가 m과 같거나 작다면 => 구간의 점수가 너무 클 때
        if split_sector(mid) <= m:
            ret = mid
            r = mid - 1  # 구간의 점수 줄인다.(=구간의 개수 늘린다), 왼쪽 부분 탐색

        # 구간의 개수가 m보다 크다면 => 구간의 점수가 너무 작을 때
        else:
            l = mid + 1  # 구간의 점수 늘린다.(=구간의 개수 줄인다), 오른쪽 부분 탐색

    return ret


n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

ret = binary_search()

print(ret)