'''
- 3중 for문을 사용하면 시간초과
- 'x + y + z = k'는 'x + y = k - z'와 동일하다.
    - x와 y의 합을 set()에 저장한다. (주어진 U는 집합이므로)
- 리스트를 오른쪽 끝 부터 순회하면서, 'x + y = k - z'를 만족한다면 k를 return한다.

'''

import sys

# k번째 수 찾기
def find_k():
    ret = 0
    
    # k번째 수가 최대가 되도록 하는 것이 목적이므로
    # 뒤에서 부터 순회한다.
    for i in range(n - 1, -1, -1):
        
        # k, z는 같아도 되므로
        for j in range(i + 1): 
            if nums[i] - nums[j] in nums_set: # x + y = k - z를 만족한다면
                ret = nums[i] 
                return ret

n = int(sys.stdin.readline())
nums = sorted(list(int(sys.stdin.readline()) for _ in range(n)))

# 주어진 U는 집합이므로
nums_set = set()

# x와 y의 합을 저장한다.
for x in nums:
    for y in nums:
        nums_set.add(x + y)

# 수행 & 출력
print(find_k())