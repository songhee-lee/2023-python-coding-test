""" 
- X라는 정수가 존재하는지 알아내기
"""

N = int(input())
numbers = set(map(int, input().split()))
M = int(input())
for x in input().split():
    if int(x) in numbers:
        print(1)
    else:
        print(0)


####################################
# 이진 탐색 활용
####################################
def binary_search(numbers, target):
    s, e = 0, len(numbers)-1
    while s <= e:
        m = (s+e) // 2

        if numbers[m] == target :
            return 1
        elif numbers[m] < target :
            s = m+1
        else:
            e = m-1
    return 0

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
M = int(input())
for x in input().split():
    print(binary_search(numbers, int(x)))
