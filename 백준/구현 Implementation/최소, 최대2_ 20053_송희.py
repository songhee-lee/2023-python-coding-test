"""
N개의 정수가 주어질 때, 최솟값과 최댓값 구하기

1 <= 테스트 케이스 <= 10
1 <= N <= 1,000,000
"""

for _ in range(int(input())) :
    N = int(input())
    numbers = sorted(list(map(int, input().split())))
    print(f"{numbers[0]} {numbers[-1]}")