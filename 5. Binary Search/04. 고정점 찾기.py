""" 
- 고정점 : 수열의 원소 중 그 값이 인덱스와 동일한 원소
- O(logN) 으로 설계해야 함
"""

N = int(input())
numbers = list(map(int, input().split()))

# 고정점 찾기
answer = -1
s, e = 0, N-1
while s <= e:
    m = (s+e) // 2

    if numbers[m] == m :
        answer = m
        break
    elif numbers[m] > m :
        e = m-1
    else:
        s = m+1

print(answer)