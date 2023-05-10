'''
💢 주의해야 할 것 -> 배열 A와 B는 정렬하면 안된다?

- 처음에, 두 배열의 합을 일일히 구해 비교했음 -> 시간초과 가능성 많음.
    -> '부분합' 사용
- 부 배열의 합 == 부분합
- a의 부분합 + b의 부분합 = t 이므로 a, b의 부분합을 모두 구해서 리스트로 만든다.
    -> t - a의 부분합 = b의 부분합
- a, b의 부분합 리스트를 정렬한다.
- t - a의 부분합이 b의 부분합 리스트에 존재하는지, 존재한다면 몇개가 있는지 세주면 된다.

-> ✅다시풀기
⭕️ 투 포인터 != 이분탐색
⭕️ bisect!!!
'''

import sys, bisect

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

sum_of_sub_a = []
sum_of_sub_b = []

# 리스트 a의 부 배열의 합 구하기
for i in range(n):
    s = a[i]
    sum_of_sub_a.append(s)
    for j in range(i + 1, n):
        s += a[j]
        sum_of_sub_a.append(s)
        
# 리스트 b의 부 배열의 합 구하기
for i in range(m):
    s = b[i]
    sum_of_sub_b.append(s)
    for j in range(i + 1, m):
        s += b[j]
        sum_of_sub_b.append(s)

sum_of_sub_a.sort()
sum_of_sub_b.sort()

ret = 0
# a의 부 배열의 합 + b의 부 배열의 합 = t
# 즉, 't - a의 부 배열의 합 = b의 부 배열의 합'
for i in range(len(sum_of_sub_a)):
    l = bisect.bisect_left(sum_of_sub_b, t - sum_of_sub_a[i]) # 값이 등장하는 왼쪽 위치
    r = bisect.bisect_right(sum_of_sub_b, t - sum_of_sub_a[i]) # 값이 등장하는 오른쪽 위치
    ret += r - l

# 출력
print(ret)