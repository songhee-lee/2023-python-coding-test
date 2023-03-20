'''
1) 가장 짧은 길이 1을 start로, 랜선 중 가장 긴 길이를 end로 둔다.

2) 이분탐색이 끝날 때까지 while 문을 돌린다.

3) mid를 start와 end의 중간으로 두고, 모든 랜선 값을 mid로 나누어 총 몇개의 랜선이 나오나 살펴본다.

4-1) 랜선이 목표치 이상이면 mid+1을 start로 두고 다시 while문 반복

4-2) 랜선이 목표치 이하면 mid-1을 end로 두고 다시 while문 반복

5) start와 end가 같아지면: 조건을 만족하는 최대의 랜선길이를 찾으면 탈출한다.

6) 결과값인 end출력
'''

import sys

k, n = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1, max(lan)

while start <= end:
    mid = (start + end)//2
    lines = 0
    for i in lan:
        lines += i // mid
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
