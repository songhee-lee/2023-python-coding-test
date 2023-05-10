'''
- a + b + c + d = 0을 만족하는 경우의 수를 구해야 한다.
    - (a + b) + (c + d)로 볼 수 있다.
- 따라서, a와 b의 모든 원소를 더한 리스트와 c와 d의 모든 원소를 더한 리스트를 새로 만든다.
- 이진 탐색을 수행한다.
    - ab의 인덱스를 l, cd의 인덱스를 r로 설정한다.(ab가 작은수, cd가 큰수)
    - ab[l] + cd[r] == 0
        - ab[l]와 cd[r]이 여러개 있을 수 있다. 따라서, 이를 모두 구해줘야 한다.
        - 모두 구했으면 각각의 경우의 수를 곱해서 더해준다.
    - ab[l] + cd[r] < 0
        - ab[l]이 작은 경우이므로, 크게 해준다. => l += 1
    - ab[l] + cd[r] > 0
        - cd[r]이 큰 경우이므로, 작게 해준다. => r -= 1
        
-> ✅ 다시풀기
-> ❌ PyPy3로 성공함. (Python3는 시간초과)
'''

import sys
import bisect

# 이진 탐색
def binary_search():
    l, r = 0, n * n - 1
    total_same_count = 0 # 합이 0이 되는 쌍의 개수
    
    # 서로 다른 두 배열에서의 투 포인터이므로
    # while의 조건이 l <= r 또는 l < r이면 안된다.
    while l < n * n and r >= 0:
        sum_ab = ab[l] # a와 b의 합
        sum_cd = cd[r] # c와 d의 합
        ab_same_count, cd_same_count = 0, 0 # 동일한 수의 개수
        
        if sum_ab + sum_cd == 0: # (a + b) + (c + d) == 0이라면
            while l < len(ab) and ab[l] == sum_ab: # ab와 같은 수가 있다면
                ab_same_count += 1
                l += 1
            
            while r >= 0 and cd[r] == sum_cd: # cd와 같은 수가 있다면
                cd_same_count += 1
                r -= 1
            
            # 같은 수까지 고려해서 더해준다.
            total_same_count += ab_same_count * cd_same_count 
        
        # 0보다 작다면, l을 늘린다.
        elif sum_ab + sum_cd < 0: 
            l += 1
        # 0보다 크다면, r을 줄인다.
        else:
            r -= 1
            
    return total_same_count

n = int(sys.stdin.readline())
total_list = [[] for _ in range(4)]

# 입력 저장
for _ in range(n):
    input_data = list(map(int, sys.stdin.readline().split()))
    idx = 0
    for i in range(4):
        total_list[i].append(input_data[idx])
        idx += 1

# a와 b의 모든 합을 저장하는 리스트 
# c와 d의 모든 합을 저장하는 리스트        
ab, cd = [], []

# 각각의 리스트의 가능한 모든 합을 구해서 저장한다.
for i in range(n):
    for j in range(n):
        ab.append(total_list[0][i] + total_list[1][j])
        cd.append(total_list[2][i] + total_list[3][j])

# 이진 탐색을 위해 정렬
ab.sort()
cd.sort()

# 이진 탐색 수행
ret = binary_search()

# 출력
print(ret)