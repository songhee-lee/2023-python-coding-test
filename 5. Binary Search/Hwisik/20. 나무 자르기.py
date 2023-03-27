'''
- 적어도 M미터의 나무를 집에 가져가기 위한 절단기의 높이의 최댓값 구하기
    - 절단기의 높이를 최대로 한다 -> 가져가는 나무의 길이를 M에 최대한 가깝게 한다.
    
'''

import sys

# 이진 탐색
def binary_search():
    l, r = 0, trees[-1] # 절단기 높이의 최소, 최대
    while l <= r:
        cutted_tree = 0
        mid = l + (r - l) // 2 # 중간값
        
        for tree in trees:
            if tree >= mid:
                cutted_tree += tree - mid # 몇 미터의 나무를 가져갈 수 있는지 확인
        
        # M보다 크거나 같다면 -> 절단기 높이 더 크게 가능
        if cutted_tree >= m: l = mid + 1
        
        # M보다 작다면 -> 절단기가 너무 높게 설정되어 있음.
        else: r = mid - 1
        
    return r

n, m = map(int, sys.stdin.readline().split())

trees = sorted(list(map(int, sys.stdin.readline().split())))

# 이진 탐색 수행
ret = binary_search()

# 출력
print(ret)
