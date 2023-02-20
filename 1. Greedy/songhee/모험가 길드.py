"""Pseudo Code

1. 수 입력 받아 배열로 저장
2. 공포도 정렬해서 그룹 만들기

"""

# 1. 입력 받기
N = int(input())
fear = list(map(int, input().split()))

# 2. 정렬 후 그룹 만들기
fear.sort()

result = 0 # 총 그룹 수
cnt = 0    # 현재 그룹의 모험가 수
for i in fear :
    cnt += 1         
    if cnt >= i :    # 현재 그룹의 모험가 수가 공포도 이상이면 그룹핑 가능
        result += 1
        cnt = 0

print(result)