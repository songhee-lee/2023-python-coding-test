""" 
- N개의 부품 중 M개가 모두 있는지 확인하기
"""
import sys

N = int(input())
components = set(map(int, sys.stdin.readline().split()))
M = int(input())
offers = list(map(int, sys.stdin.readline().split()))

# 확인 O(1) * N
for x in offers :
    if x in components:
        print("yes", end=" ")
    else:
        print("no", end=" ")

print()
####################################
# 이진 탐색을 활용한 방법
####################################

# 1. 정렬
components = sorted(list(components))

# 2. 이진 탐색 함수
def binary_search(array, target, start, end):
    if start > end:
        return None   

    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target :
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

# 3. 찾기
for x in offers:
    if binary_search(components, x, 0, N-1) :
        print("yes", end=" ")
    else:
        print("no", end=" ")

print()
####################################
# 계수 정렬을 활용한 방법
####################################

# 1. 부품 기록하기
counting_sort = [False] * 1000001
for x in components:
    counting_sort[x] = True

# 2. 찾기
for x in offers:
    if counting_sort[x] :
        print("yes", end=" ")
    else:
        print("no", end=" ")
