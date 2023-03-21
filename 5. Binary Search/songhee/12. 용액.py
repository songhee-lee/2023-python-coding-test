""" 
- 용액의 특성값 : -1,000,000,000 ~ 1,000,000,000
- 특성값이 0에 가장 가까운 용액 만들기
"""

N = int(input())
numbers = list(map(int, input().split()))

s, e = 0, N-1
answer = (2e9, 0, 0)

while s < e:
    x = numbers[s] + numbers[e]     # 두 용약 특성값의 합

    # 최솟값 갱신
    if answer[0] > abs(x) : 
        answer = (abs(x), numbers[s], numbers[e])
        if x == 0:
            break
    
    # 0보다 작으면 - 가 더 큰 것
    if x < 0 :
        s += 1
    # 0보다 크면 + 가 더 큰 것
    else:
        e -= 1

print(f"{answer[1]} {answer[2]}")


# 메모리 초과
"""
N = int(input())
numbers = list(map(int, input().split()))

mixed = []
for i in range(N):
    for j in range(i+1, N):
        mixed.append((abs(numbers[i]+numbers[j]), numbers[i], numbers[j]))

mixed = sorted(mixed, key=lambda x: x[0])

print(f"{mixed[0][1]} {mixed[0][2]}")
"""