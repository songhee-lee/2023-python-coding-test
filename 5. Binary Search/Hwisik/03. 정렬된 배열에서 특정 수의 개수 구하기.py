'''
- x가 등장하는 시작점과 끝점을 찾아야 한다. -> 하나의 이진탐색으로는 찾기 불가능
- 2개의 이진탐색을 사용한다. -> 각각 시작점과 끝점을 찾는 용도
    - 시작점을 찾을 때 어떻게 판단? (기저조건)
        - mid가 0일 때
        - 또는, seq[mid]가 x와 같을 때 + seq[mid - 1]이 x보다 작을 때
            - 왜냐하면, 문제의 입력이 연속적인 수열이니까
            
    - 끝점을 찾을 때 어떻게 판단? (기저조건)
        - mid가 n - 1일 때
        - 또는, seq[mid]가 x와 같을 때 + seq[mid + 1]이 x보다 클 때
            - 왜냐하면, 문제의 입력이 연속적인 수열이니까
'''

import sys

# 시작점 찾기
def find_first_position(l, r):
    if l > r:
        return None
        
    mid = l + (r - l) // 2
    
    # x의 값을 가지는데 가장 왼쪽에 있는 경우
    if mid == 0 or seq[mid - 1] < x and seq[mid] == x:
        return mid
    
    # x의 값보다 작다면, 오른쪽 탐색
    if seq[mid] < x:
        return find_first_position(mid + 1, r)
    # x의 값보다 크거나 같다면, 왼쪽 탐색
    if seq[mid] >= x:
        return find_first_position(l, mid - 1)

# 끝점 찾기
def find_last_position(l, r):
    if l > r:
        return 0
        
    mid = l + (r - l) // 2
    
    # x의 값을 가지는데 가장 오른쪽에 있는 경우
    if mid == n - 1 or seq[mid + 1] > x and seq[mid] == x:
        return mid
    
    # x의 값보다 작거나 같다면, 오른쪽 탐색
    if seq[mid] <= x:
        return find_last_position(mid + 1, r)
    # x의 값보다 크다면, 왼쪽 탐색
    if seq[mid] > x:
        return find_last_position(l, mid - 1)
    
    
n, x = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))

# 시작점, 끝점 찾아서 저장
first_index = find_first_position(0, n - 1)
last_index = find_last_position(0, n - 1)

# 시작점이 존재하지 않는다 == x가 존재하지 않는다.
if first_index == None:
    print(-1)
# x가 존재한다면
else:
    print(last_index - first_index + 1)