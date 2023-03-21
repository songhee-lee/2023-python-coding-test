'''
- 일반적인 이진 탐색 알고리즘 문제
- 고정점이란, 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미한다.
- 모든 원소가 오름차순으로 정렬되어 있다.
- 수열에서 고정점이 있다면, 고정점을 출력
'''

import sys

# 이진 탐색
def binary_search():
    l, r = 0, n - 1 # 시작점, 끝점 설정
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == mid:
            return arr[mid]
        elif arr[mid] > mid: # mid의 오른쪽은 자기 인덱스보다 값이 무조건 크다, 왼쪽 부분 탐색
            r = mid - 1
        else: # mid의 왼쪽은 자기 인덱스보다 값이 무조건 작다, 오른쪽 부분 탐색
            l = mid + 1
    return -1

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 이진 탐색 결과 출력
print(binary_search())