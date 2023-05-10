# 풀이 참조

import sys

input = sys.stdin.readline

n = int(input())
cities = sorted(list(map(int,input().split())))
budgets=int(input())
start,end = 0,cities[-1]

# 이분 탐색
while start <= end :
    mid=(start+end)//2
    total = 0   # 총 지출 양
    for c in cities:
        if c > mid :        # 요청액이 상한액을 초과할 경우, 상한액 배정
            total += mid
        else:               # 요청액이 상한액 이하일 경우, 요청액 배정
            total += c
    if total <= budgets : start = mid+1
    else : end = mid-1

print(end)