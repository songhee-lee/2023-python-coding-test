""" 
- A에는 속하는데 B에는 속하지 않는 모든 원소 구하기
"""

####################################
# set 활용
####################################
A, B = map(int, input().split())
numa = list(map(int, input().split()))
numb = set(map(int, input().split()))

numbers = set(numa) - numb
res = [ x for x in numa if x in numbers]
if len(res) == 0:
    print(0)
else:
    print(len(res))
    print(*sorted(res))
