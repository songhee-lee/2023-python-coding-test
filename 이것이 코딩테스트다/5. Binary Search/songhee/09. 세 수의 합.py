""" 
- N개의 자연수가 있는 U 집합에서 3개의 수를 골라 더한 합이 U 안에 포함되는 경우
- 가장 큰 숫자 찾기
"""

N = int(input())
numbers = [ int(input()) for _ in range(N) ]
numbers.sort()

two_sum = set()
for x in numbers:
    for y in numbers:
        two_sum.add(x+y)

# x+y = k-z
# 큰 숫자부터 K가 될 수 있는지 확인한다.
answer = []
for k in numbers:
    for z in numbers:
        if k - z in two_sum:  
            answer.append(k)

print(sorted(answer)[-1])

