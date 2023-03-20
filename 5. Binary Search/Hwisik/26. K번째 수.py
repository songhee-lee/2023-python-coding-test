'''
- B[k] : k번 째의 수 => 1 ~ (k - 1)번째 수들은 k번째 수보다 무조건 작다.
    -> 즉, B[k]보다 작은 수가 몇개있는지 확인하면, B[k]를 구할 수 있다.
- e.g. 3 * 3에서 5보다 작은 수 찾기
    - 1*1 ~ 1*3 = 3개
    - 2*1 ~ 2*2 = 2개
    - 3*1 ~ 3*1 = 1개
    -> 즉, 5를 행의 인덱스로 나눈 몫이 개수가 된다.
'''

import sys

# 이진 탐색
def binary_search():
    l, r = 1, k
    
    while l <= r:
        mid = l + (r - l) // 2
        count = 0
        
        # mid 보다 작은 수의 개수 찾기
        for i in range(1, n + 1):
            count += min(mid // i, n)
        
        # 총 개수가 k보다 크거나 같다면, mid가 높게 설정됨 -> 왼쪽 부분 탐색
        if k <= count:
            r = mid - 1
            
        # 총 개수가 k보다 작다면, mid가 낮게 설정됨 -> 오른쪽 부분 탐색
        else:
            l = mid + 1
             
    return l
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

# 이진 탐색 수행
ret = binary_search()

# 출력
print(ret)