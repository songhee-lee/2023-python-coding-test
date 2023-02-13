
""" Pseudo Code
1. 수 입력 받아 배열에 담기
2. 첫 번째 큰 수와 두 번째 큰 수 구하기
3. (제일 큰 수 K 번, 두번 째 큰수 1번) 더하기 반복
"""

# 1. 입력 받기
_, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

# 2. 가장 큰 수와 두 번째 큰 수 구하기
numbers.sort()
first, second = numbers[-1], numbers[-2]

# 3. 계산
qu = M // (K+1) # 몫 (반복 횟수)
re = M % (K+1)  # 나머지

result = qu * (K * first + second) + re * first
print(result)

