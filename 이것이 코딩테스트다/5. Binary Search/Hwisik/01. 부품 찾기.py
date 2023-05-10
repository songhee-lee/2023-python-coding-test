'''
- 이진탐색을 수행한다.
- 배열의 중간값(mid)과 필요한 부품의 크기가 같다면, return
- 필요 부품의 크기가 더 작다면, 왼쪽 부분 탐색
- 필요 부품의 크기가 더 크다면, 오른쪽 부분 탐색
'''
import sys

# 이진 탐색
def binary_search(need):
    l, r = 0, n - 1 # 시작점과 끝점 설정
    
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == need:
            return 'yes'
        elif arr[mid] > need:
            r = mid - 1
        else:
            l = mid + 1
            
    return 'no'
    
n = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
needs = list(map(int, sys.stdin.readline().split()))

for need in needs:
    print(binary_search(need), end=' ')