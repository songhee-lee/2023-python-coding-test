"""Psuedo Code
1. N 입력받기
2. N시 59분 59초까지 중 3이 하나라도 포함되는 경우의 수
    - 시 : 3의 배수 시일 때 모두 (60*60개)
    - 분 : 3, 13, 23, 30-39, 43, 53 분 (60개)
    - 초 : 3, 13, 23, 30-39, 43, 53 초 (15개)
"""

# 1. 입력받기
N = int(input())

# 2-1. 시
h = N // 3
result = h * 60 * 60

# 2-2. 분
result += (N - h + 1) * 15 * 60

# 2-3. 초
result += (N - h + 1) * 45 * 15

print(result)



######################
# 완탐으로 하나씩 비교하기 코드
count = 0
for i in range(N+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)