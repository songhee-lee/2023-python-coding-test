
"""Pseudo Code

1. 숫자 입력 받아 배열로 저장
2. 각 배열 정렬해서 min 끼리 새로운 배열 만들기
3. 가장 큰 숫자의 Index 출력

"""

# 1. 입력 받기 + 2. min 끼리 새로운 배열 만들기
N, M = map(int, input().split())
mins = []
for _ in range(N):
    tmp = list(map(int, input().split())) # 입력 받고
    mins.append(min(tmp)) # 가장 작은 수 찾기

# 3. 가장 큰 숫자 출력
print(max(mins))
