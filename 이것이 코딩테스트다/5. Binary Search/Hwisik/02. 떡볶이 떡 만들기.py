'''
- 나무 자르기, 랜선 자르기와 유사한 문제
'''
import sys

# 이진 탐색 
def binary_search():
    l, r = 1, dduks[-1] # 시작점, 끝점 설정
    
    max_h = 0
    while l <= r:
        mid = l + (r - l) // 2
        
        h = 0
        # 잘랐을 때 떡의 양 계산
        for dduk in dduks:
            if dduk >= mid:
                h += dduk - mid
        
        # 떡의 양이 충분한 경우, 덜 자르기(오른쪽 부분 탐색)
        if h >= m:
            l = mid + 1
            max_h = mid # 최대한 덜 잘랐을 때가 절단기 높이의 최대값이 된다.
        # 떡의 양이 부족한 경우, 더 많이 자르기(왼쪽 부분 탐색)
        else:
            r = mid - 1
            
    return max_h

n, m = map(int, sys.stdin.readline().split())
dduks = sorted(list(map(int, sys.stdin.readline().split())))

# 이진탐색 결과 출력
print(binary_search())